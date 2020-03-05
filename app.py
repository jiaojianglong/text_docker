# -*- coding:utf-8 -*-
#  author :  焦江龙
#  time   :  2020/3/5  14:59


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()