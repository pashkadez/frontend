from flask import render_template
from app import app
from app.forms import LoginForm


# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()


@app.route("/")
@app.route("/index")
#@login_required
def index():
    user = {'username': 'Oleksii'}
    return render_template("index.html", title="Kv-DevOps-094", user=user)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", Title="Sign In", form=form)
