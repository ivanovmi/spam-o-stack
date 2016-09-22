import time
from random import randint


class Simulator(object):
    def __init__(self, client, pipeline):
        self.client = client
        self.pipeline = pipeline

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
            
