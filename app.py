from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, world'


@app.route('/predict')
def predict():
    return 'predicciones'


if __name__ == "__main__":
    app.run()
