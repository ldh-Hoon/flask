from flask import Flask
from flask import request

import requests
import re
import socket

app = Flask(__name__)

# 컴퓨터 이름, ip
hostname = socket.gethostname()
hostip = socket.gethostbyname(socket.gethostname())

#외부 IP, 아래 사이트 호출 후 결과에서 추출
req = requests.get("http://ipconfig.kr")
out_ip = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

@app.route("/")
def home():
    return  '컴퓨터 이름 : {0}<br>내부 IP : {1}<br>외부 IP : {2}<br><br> 당신의 IP :{3}<br><br>Hello'.format(hostname, hostip, out_ip, request.remote_addr)

@app.route("/hello")
def hello():
    return render_template("page.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, True)
