from flask.ext.sqlalchemy import SQLAlchemy # importSQLAlchemy class from flask
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy() # create a variable containing a new instances of the SQLALchemy class

class User(db.Model): #create a python class to model a users attribtues (same as column as user table in postgres)
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))

  def __init__(self, firstname, lastname, email, password): #create constructor to set each of these class attributes
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password): #encrypts passwords
    self.pwdhash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)