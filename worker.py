import time

import requests
from celery import Celery

from config import BROKER

app = Celery(__name__, broker=BROKER)


class NotifierTask(app.Task):
    """ Task that sends notification on completion """

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        """ Handler called after the task returns; return value ignored """
        url = 'http://localhost:3000/notify'
        print(f'Task after_return method clientid kwargs: {kwargs["clientid"]}')
        data = {'clientid': kwargs['clientid'], 'result': retval}
        requests.post(url, data=data)


@app.task(base=NotifierTask)
def mytask(clientid=None):
    """ Simulates some slow computation """
    time.sleep(5)
    return 42
