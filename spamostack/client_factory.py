from session import Session

import neutronclient.v2_0
import cinderclient.v3
import novaclient.v2
import glanceclient.v2


def cached(func):
    '''Cache clients'''

    def wrapper(self, *args, **kwargs):
        

class ClientFactory(object):
    def __init__(self, cache):
        '''
        Create instance of `OSClient` class

        @param cahce: Reference to the cache
        @type cache: spamostack.cache.Cache
        '''

        self.cache = cache


    @cached
    def keystone(self, version="3"):
        '''
        Create keystone client

        @param version: Version of the client
        @type version: `str`
        '''

        from keystoneclient.client import Client
        session = Session(self.cache)

        client = Client(version,
                        session=session.session)
        session.parent = client

        return client

    @cached
    def neutron(self, version="2"):
        '''
        Create keystone client

        @param version: Version of the client
        @type version: `str`
        '''

        from neutronclient.client import Client
        session = Session(self.cache)

        client = Client(version,
                        session=session.session)
        session.parent = client

        return client







