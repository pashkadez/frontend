from flask import render_template
from app import app


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
