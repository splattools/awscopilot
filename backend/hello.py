import os
from flask import Flask

server = Flask(__name__)
conn = None

@server.route('/')
def listBlog():
    response = 'from flask!'
    return response

if __name__ == '__main__':
    server.run()
