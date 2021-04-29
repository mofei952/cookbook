import webbrowser
from time import sleep


webbrowser.open('http://www.python.org?1')
webbrowser.open_new('http://www.python.org?2')
webbrowser.open_new_tab('http://www.python.org?3')


c = webbrowser.get('windows-default')
c.open('http://www.python.org?4')
sleep(2)
