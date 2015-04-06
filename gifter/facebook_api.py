from flask import (
    Flask,
    flash,
    request,
    redirect,
    render_template,
    url_for
)
from gifter.config import (
    DEBUG,
    SECRET_KEY,
    FACEBOOK_AUTH
)


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/facebook/login')
def login():
    redirect_uri = url_for('authorized', _external=True)
    params = {'redirect_uri': redirect_uri}
    return redirect(FACEBOOK_AUTH.get_authorize_url(**params))


@app.route('/facebook/authorized')
def authorized():
    if not 'code' in request.args:
        flash('You did not authorize the request')
        return redirect(url_for('index'))

    redirect_uri = url_for('authorized', _external=True)
    data = dict(code=request.args['code'], redirect_uri=redirect_uri)

    session = FACEBOOK_AUTH.get_auth_session(data=data)
    me = session.get('me').json()

    flash('Logged in as ' + me['name'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=8000)
