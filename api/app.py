from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Khangesh You have reached to the API!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

