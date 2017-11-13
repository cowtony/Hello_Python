from flask import Flask
app = Flask(__name__)

from flask_script import Manager
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    manager.run()
#if __name__ == '__main__':
#    app.run(debug=True)
