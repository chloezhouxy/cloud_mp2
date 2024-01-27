from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip_address():
    return str(socket.gethostname())

@app.route('/', methods=['POST'])
def trigger():
   subprocess.Popen('Python3 stress_cpu.py', shell=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
