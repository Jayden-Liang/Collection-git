
from flask_login import UserMixin
import hashlib
from initial import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index= True,unique=True)
    email = db.Column(db.String(64), unique = True)
    hashed_password = db.Column(db.String(128))
    ct = db.Column(db.DateTime())


    @classmethod
    def salted_password(cls, password, salt='ad^&6x678$6$4h3245&DWQa'):
        import hashlib
        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()
        hash1 = sha256(password)
        hash2 = sha256(hash1 + salt)
        return hash2



class Blog(db.Model):
    id= db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String())
    body = db.Column(db.String())
    ct = db.Column(db.DateTime())
    topic = db.Column(db.String(128), index= True)
    writer = db.Column(db.String())
    ut = db.Column(db.DateTime())


db.create_all()
