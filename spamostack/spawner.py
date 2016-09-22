from cache import Cache
from client_factory import ClientFactory


class Spawner(object):
    def __init__(self, cache, conf):
        self.cache = cache
        self.conf = conf
        self.client_factory = ClientFactory(cache)

    def spawn_clients(self):
        for key, value in self.conf:
            if key == "keystone":
                cache["keystone"]["client"]. \
                    append(self.client_factory.keystone())
            if key == "neutron":
                cache["neutron"]["client"]. \
                    append(self.client_factory.neutron())

    def spawn_simulators(self):
        for 
