# -*- coding:utf-8 -*-
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
 
tmpl = env.get_template('jinja2_test.tmpl')

#ここで shop に入る文字を指定している
html = tmpl.render(shop=u"アマズン",)

with open('jinja2_test.html',mode='w') as f:
    f.write(str(html))
    
print(html)