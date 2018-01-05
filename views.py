from jinja2 import Environment, FileSystemLoader
import os
import time
import cv2
import numpy

from utils import log
from models import insertToliuyan


path = '{}/templates'.format(os.path.dirname(__file__))
env = Environment(loader=FileSystemLoader(path))


def index(request):
    template = env.get_template('index.html')
    with open('liuyan.txt', 'r', encoding='utf-8') as f:
        liuyan = f.read()
    template = template.render(liuyan=liuyan)
    response = 'HTTP/1.1 200 ok\r\ncontent-type:text/html\r\n\r\n'+template+'\r\n'
    response = response.encode('utf-8')
    return response


def Login(request):
    template = env.get_template('login.html')
    template = template.render()
    response = 'HTTP/1.1 200 ok\r\ncontent-type:text/html\r\n\r\n'+template+'\r\n'
    response = response.encode('utf-8')
    return response


def favicon(request):
    with open('static/img/favicon.ico', 'rb') as f:
    	img = f.read()
    response = 'HTTP/1.1 200 ok\r\ncontent-type:img/x-ico\r\n\r\n'.encode('utf-8')+img+'\r\n'.encode('utf-8')
    return response


def bg(request):
    with open('static/img/bg.gif', 'rb') as f:
    	img = f.read()
    response = 'HTTP/1.1 200 ok\r\ncontent-type:img/x-ico\r\n\r\n'.encode('utf-8')+img+'\r\n'.encode('utf-8')
    return response

def vide(request):
    with open('e:/1.mp4', 'rb') as f:
    	img = f.read()
    response = 'HTTP/1.1 200 ok\r\ncontent-type:video/mpeg4\r\n\r\n'.encode('utf-8')+img+'\r\n'.encode('utf-8')
    return response

route_views = {
    '/': index,
    '/login': Login,
    '/favicon.ico': favicon,
    '/static/img/bg.gif': bg,
}
