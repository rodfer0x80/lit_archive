from flask import Blueprint, render_template

bp = Blueprint("txt_posts", __name__, template_folder='templates')

@bp.route('/txt_posts')
def show():
    return render_template('txt_posts.html')

