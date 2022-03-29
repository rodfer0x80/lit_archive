from flask import Flask

# import routes
from .views.root import bp as root_bp
from .views.posts import bp as posts_bp
from .views.txt_posts import bp as txt_posts_bp
from .views.whoami import bp as whoami_bp

# auto generated 
# posts
from .views._posts.hell_world import bp as hell_world_bp


# auto generated 
# txt_posts
from .views._txt_posts.txt_hell_world import bp as txt_hell_world_bp


app = Flask(__name__)


# draw blueprints from routes
app.register_blueprint(root_bp)
app.register_blueprint(whoami_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(txt_posts_bp)

# auto generated
# posts
app.register_blueprint(hell_world_bp)

# auto generated
# posts
app.register_blueprint(txt_hell_world_bp)
