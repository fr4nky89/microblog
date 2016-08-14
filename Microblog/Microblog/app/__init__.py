from flask import Flask
 
app = Flask(__name__)
app.secret_key = "fegjefggjrpoj"
from app import views