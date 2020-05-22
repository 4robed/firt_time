from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "ALO ALO 1234"
"""
thêm vài dòng vào đây cho nó 
có thông báo :D
"""
