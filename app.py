from flask import Flask, render_template

#flask instance
app = Flask(__name__)

#route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

#error and version control
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
#server error
@app.errorhandler(500)
def invalid(e):
    return render_template('500.html'), 500

