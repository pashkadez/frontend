from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_id = db.Column(db.Integer)
    avatar_url = db.Column(db.String(220))
    user_id = db.Column(db.String(60))
    issue_action = db.Column(db.String(60))
    issue_title = db.Column(db.String(120))
    issue_state = db.Column(db.String(60))
    issue_html_url = db.Column(db.String(220))
    modified_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_html_url = db.Column(db.String(220))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))