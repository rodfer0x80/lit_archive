from flask import Blueprint, render_template

bp = Blueprint("root", __name__, template_folder='templates')

@bp.route('/')
def show():
    return render_template('root.html')
