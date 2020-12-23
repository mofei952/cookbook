# 另外一个解决GIL的策略是使用C扩展编程技术。
# 主要思想是将计算密集型任务转移给C，跟Python独立，在工作的时候在C代码中释放GIL。
# 这可以通过在C代码中插入下面这样的特殊宏来完成：

"""
#include "Python.h"
...

PyObject *pyfunc(PyObject *self, PyObject *args) {
   ...
   Py_BEGIN_ALLOW_THREADS
   // Threaded C code
   ...
   Py_END_ALLOW_THREADS
   ...
}
"""

# 如果使用其他工具访问C语言，比如对于Cython的ctypes库，你不需要做任何事。
# 例如，ctypes在调用C时会自动释放GIL。
