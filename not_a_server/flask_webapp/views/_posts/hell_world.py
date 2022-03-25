from flask import Blueprint, render_template

bp = Blueprint("hell_world", __name__, template_folder='templates')

@bp.route('/posts/hell_world')
def show():
    return render_template('posts/hell_world.html')
