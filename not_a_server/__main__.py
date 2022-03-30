from flask_webapp.app import app


if __name__== '__main__':
    # development
    # app.run(host='127.0.0.1', debug=True)
    # production
     app.run(host='0.0.0.0', debug=False)
