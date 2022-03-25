from flask_webapp.app import app

# set debug to False in production
if __name__== '__main__':
    app.run(debug=True)
