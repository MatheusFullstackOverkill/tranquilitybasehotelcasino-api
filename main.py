from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Take it easy for a litle while, come on stay with us!'