from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Vinícius Gabriel - 2201703  Renato Martin - 2201795   Ryan Victor - 2201845'