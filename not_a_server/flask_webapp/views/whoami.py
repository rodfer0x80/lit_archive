from flask import Blueprint, render_template

bp = Blueprint("whoami", __name__, template_folder='templates')

@bp.route('/whoami')
def show():
    return render_template('whoami.html')
