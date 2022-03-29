from flask import Blueprint, render_template
import os
bp = Blueprint("txt_hell_world", __name__, template_folder='templates')

txt_posts_dir = 'flask_webapp/templates/txt_posts/'
@bp.route('/txt_posts/hell_world')
def show():
    output = ""
    with open(txt_posts_dir+'hell_world.txt', 'r') as fi:
        output += fi.read()
    _output = ""
    for line in output.splitlines():
        _output += line + "<br>"
    return _output
