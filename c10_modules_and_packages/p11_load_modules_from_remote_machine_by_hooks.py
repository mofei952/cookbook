import imp
from urllib.request import urlopen
import sys
import logging
from html.parser import HTMLParser
import importlib


# 使用imp.new_module()来创建一个新的模块对象
m = imp.new_module('spam')
print(m)
print(m.__name__)

# 模块对象通常有一些期望属性，包括__file_（运行模块加载语句的文件名）和__package__（包命）
m.__file__ = '/project/spam.py'
m.__package__ = 'project'
print(m.__file__)
print(m.__package__)

# 模块会被解释器缓存起来，模块缓存可以在字典sys.modules中被找到，通常可以将缓存和模块的创建通过一个步骤完成
m = sys.modules.setdefault('spam', imp.new_module('spam'))
print(m)
print()

# 如果给定模块已经存在那么会直接获得已经创建的模块
m = sys.modules.setdefault('math', imp.new_module('math'))
print(m)
print(m.sin(2))


# 将一些文件作为模块被远程访问
# cd c10_modules_and_packages\p11
# python -m http.server 15000


# 加载远程模块
# 该函数会下载源代码，并使用compile()将其编译到一个代码对象中，然后在一个新创建的模块对象的字典中来执行它。
def load_module(url):
    u = urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


# fib = load_module('http://localhost:15000/fib.py')
# print(fib)
# for i in range(10):
#     print(fib.fib(i), end=',')
# print()

# spam = load_module('http://localhost:15000/spam.py')
# print(spam)
# spam.hello('Guido')


# 自定义导入的第一种方法是创建一个元路径导入器
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))
    links = set()
    try:
        log.debug('Getting links from %s', url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))
    except Exception as e:
        log.debug('Could not get links. %s', e)
    log.debug('links: %r', links)
    return links


class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links = {}
        self._loaders = {baseurl: UrlModuleLoader(baseurl)}

    def find_module(self, fullname, path=None):
        log.debug('find_module: fullname=%r, path=%r', fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]
        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl=%r, basename=%r', baseurl, basename)

        if baseurl not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        if basename in self._links[baseurl]:
            log.debug('find_module: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            # Attempt to load the package (which accesses __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug('find_module: package %r loaded', fullname)
            except Exception as e:
                log.debug('find_module: package failed. %s', e)
                loader = None
            return loader

        filename = basename + '.py'
        if filename in self._links[baseurl]:
            log.debug('find_module: module %r found', fullname)
            return self._loaders[baseurl]
        else:
            log.debug('find_module: module %r not found', fullname)
            return None


class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module):
        return '<urlmodule %r from %r>' % (module.__name__, module.__file__)

    def load_module(self, fullname):
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod

    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')

    def get_data(self, path):
        pass

    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + '.py'

    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug('loader: reading %r', filename)
        if filename in self._source_cache:
            log.debug('loader: cached %r', filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode('utf-8')
            log.debug('loader: %r loaded', filename)
            self._source_cache[filename] = source
            return source
        except () as e:
            log.debug('loader: %r failed. %s', filename, e)
            raise ImportError("Can't load %s" % filename)


class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [self._baseurl]
        mod.__package__ = fullname

    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'


_installed_meta_cache = {}


def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug('%r installed on sys.meta_path', finder)


def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache[address]
        sys.meta_path.remove(finder)
        log.debug('%r removed from sys.meta_path', finder)


# install_meta('http://localhost:15000')
# import fib
# print(fib)
# print(fib.fib(1))
# import spam
# import grok.blah
# print(grok.blah)
# print(grok.blah.__file__)


# 自定义导入的第二种方法是编写一个钩子直接嵌入到sys.path变量中去
class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname):
        log.debug('find_loader: %r', fullname)
        parts = fullname.split('.')
        basename = parts[-1]

        if self._links is None:
            self._links = []
            self._links = _get_links(self._baseurl)

        if basename in self._links:
            log.debug('find_loader: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                log.debug('find_loader: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_loader: %r is a namspace package', fullname)
                loader = None
            return (loader, [fullurl])

        filename = basename + '.py'
        if filename in self._links:
            log.debug('find_loader: module %r found', fullname)
            return (self._loader, [])
        else:
            log.debug('find_loader: module %r not found', fullname)
            return (None, [])


_url_path_cache = {}


def handle_url(path):
    if path.startswith(('http://', 'https://')):
        log.debug('Handle path? %s. [Yes]', path)
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug('Handle path? %s. [No]', path)


def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handle_url')


def remove_path_hook():
    sys.path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Remving handle_url')


# install_path_hook()
# import sys
# sys.path.append('http://localhost:15000')
# import fib
# print(fib.__name__)
# print(fib.__file__)
# print(fib.fib(2))
# import grok.blah
# print(grok.blah.__file__)
