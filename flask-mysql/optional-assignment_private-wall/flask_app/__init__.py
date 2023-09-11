from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "DEFAULT"
bcrypt = Bcrypt(app)

app_database = 'schema_logins' 