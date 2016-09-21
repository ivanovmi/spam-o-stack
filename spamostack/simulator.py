import time
from random import randint


class Simulator(object):
    def __init__(self, method_name, clients, params):
        self.method_name = method_name
        self.clients = clients

    def simulate(self):
        '''Simulates an action concurrently'''

        for client in self.clients:
            func = getattr(client, self.method_name)
            
