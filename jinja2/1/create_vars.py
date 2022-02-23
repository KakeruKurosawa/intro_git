#!/usr/bin/env python
# -*- coding:utf-8 -*-
  
from jinja2 import Environment, FileSystemLoader
 
env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tmpl = env.get_template('create_vars.tmpl')
 
if __name__ == "__main__":
 
    f = open('vars_list.txt', 'r')
    param = []
     
    for i in f.readlines():
        i=i.strip()
        i=i.split(' \t')
        param=param+i
 
yml = tmpl.render(key=param[0],group=param[1],type=param[2],img=param[3],region=param[4],num=param[5],zone=param[6])
playbook = "ec2up_vars.yml"
 
f = open(playbook,"w")
f.write(yml)
 
f.close()
