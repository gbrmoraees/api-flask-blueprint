from flask import Flask
from main import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
app.run(host='127.0.0.1', port=5000, debug=True)