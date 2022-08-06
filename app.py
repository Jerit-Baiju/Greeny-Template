from flask import Flask
from liveserver import LiveServer

app = Flask(__name__)
ls = LiveServer(app)

@app.route('/')
def index():
    return ls.render_template('index.html')

@app.route('/test')
def test():
    return ls.render_template('out.html')


ls.run("192.168.43.21",5000, debug=True)