from server import db
import datetime

class user(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    time = db.Column(db.DateTime,onupdate=datetime.datetime.now,default=datetime.datetime.now)

    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password