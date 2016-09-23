import time
from random import randint
import threading
from collections import OrderedDict

from session import Session
from client_factory import ClientFactory


def threader(func):
    def wrapper(self, *args, **kwargs):
        threading.Thread(target=func, args=(*args, **kwargs)).start()


class Simulator(object):
    def __init__(self, pipeline):
        self.client = client
        self.pipeline = pipeline
        self.session = Session()

    @threader
    def simulate(self):
        '''Simulate an actions'''

        def loop(pipe):
            for key, value in pipe.iteritems():
                if isinstance(value, dict):
                    loop(value)

        for key, value in pipeline.iteritems():
            if isinstance(value, dict):
                

        #for client in self.clients:
        #    func = getattr(client, self.method_name)
