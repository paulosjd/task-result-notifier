from urllib.parse import urlparse

from flask import Flask, render_template, request

from config import NOTIFIER_PORT, NOTIFIER_URL
from worker import mytask

app = Flask(__name__, template_folder='.')


@app.route('/')
def index():
    context = {
        'notifier_url': NOTIFIER_URL or 'http://{}:{}'.format(
            urlparse(request.url).hostname, NOTIFIER_PORT),
    }
    return render_template('index.html', **context)


@app.route('/runtask', methods=['POST'])
def runtask():
    """ Client receives id from notifier service upon connection. On a browser
    click event, this is sent in the POST request body to this view function,
    which then includes the client id as an argument for the Celery task. This
    view function itself just returns a simple string in the 202 response """
    clientid = request.form.get('clientid')
    mytask.delay(clientid=clientid)
    return 'running task...', 202


if __name__ == '__main__':
    app.run(debug=True)
