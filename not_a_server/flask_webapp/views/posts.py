from flask import Blueprint, render_template

bp = Blueprint("posts", __name__, template_folder='templates')

@bp.route('/posts')
def show():
    return render_template('posts.html')

