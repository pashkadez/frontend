from flask import render_template, flash, redirect, url_for
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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
