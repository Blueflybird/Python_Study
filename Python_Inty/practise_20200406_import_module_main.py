#import practise_20200406_import_module
#from Practise_Module import practise_20200406_import_module3

#practise_20200406_import_module3.eat()

#shift+shift -> terminal -> pip install requests

import requests # python -m pip install --user requests
                # requests 是一个http的包

text=requests.get('http://www.baidu.com')
print(text.content)


