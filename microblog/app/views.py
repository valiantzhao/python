from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [
        {
            'author': {'nickname': 'Vz'},
            'body': 'test'
        },
        {
            'author': {'nickname': 'bbbb'},
            'body': 'ffff'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


if __name__ == '__main__':
    app.run()
