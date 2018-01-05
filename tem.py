from jinja2 import Environment, FileSystemLoader
import os
import hashlib
import urllib

#得到用于加载模版的目录
path = '{}/templates/'.format(os.path.dirname(__file__))
#创建一个加载器，jiaja2 会从这个目录中加载模板
loader = FileSystemLoader(path)
env = Environment(loader = loader)
template = env.get_template('index1.html')

liuyan = {
  'a':156323,
  'b':956566,
  }
response = template.render(liuyan=liuyan)

pwd = 'cpxsdn123'
p = pwd.encode('ascii')
s = hashlib.sha256(p)
pwd1 = 'cpxsdn123'
p1 = pwd.encode('ascii')
s1 = hashlib.sha256(p)
a= urllib.parse.unquote('file:///E:/my/%E8%90%A7%E4%BA%95%E9%99%8C/web/liuyan%20-%20%E5%89%AF%E6%9C%AC.html')
print(a)
