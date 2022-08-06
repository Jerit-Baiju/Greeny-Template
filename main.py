from flask import Flask
from liveserver import LiveServer
from pyflit import Page

app = Flask(__name__)
ls = LiveServer(app)

@app.route('/')
def index():
    return ls.render_template('index.html')

@app.route('/test')
def test():
    page = Page('index')
    return ls.render_template(page.export())


ls.run("192.168.43.21",7000, debug=True)