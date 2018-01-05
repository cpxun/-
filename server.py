import socket
import time
import urllib
import threading

from views import route_views
from utils import log


class Request(object):
    """定义请求类包含请求信息"""

    def __init__(self):
        self.method = 'GET'
        self.path = '/'
        self.content = ''
        self.host = ''
        self.port = 3000


def request_parse(req, request, address):
    req = req.decode('utf-8')
    print(req)
    request.host, request.port = address
    method = req.split()[0]
    request.method = method

    path = req.split()[1]
    request.path = path

    content = req.split('\r\n\r\n')[1]
    content = urllib.parse.unquote(content)
    content = content.replace('+', " ")
    request.content = content
    if request.content.startswith('message='):
        content = request.content.split('message=', 1)[1]
        if content != '':
            print(request.host, content)
            with open('liuyan.txt', 'a', encoding='utf-8') as f:
                format = '%Y-%m-%d %H:%M:%S'
                value = time.localtime(int(time.time()))
                dt = time.strftime(format, value)
                f.write('<p style="color:blue">'+request.host +
                        ':<br></p>'+content+'------'+str(dt)+'<br>')

    return request


def response_with_connection(connection, address):
    request = Request()
    buffer_size = 1024
    req = ''.encode('utf-8')
    while True:
        req_ = connection.recv(1024)
        req += req_
        if len(req_) < 1024:
            break
    if len(req) != 0:
        request = request_parse(req, request, address)
        path = request.path
        view = route_views.get(path, None)
        if view is not None:  
            response = view(request)
            connection.sendall(response)
            connection.close()


def server(host='', port=5000):
    log('启动服务器，端口号：{}'.format(port))
    s = socket.socket()
    s.bind((host, port))
    while True:
        s.listen(5)
        connection, address = s.accept()
        t = threading.Thread(target=response_with_connection,
                             args=(connection, address,))
        t.start()


if __name__ == "__main__":
    server()
