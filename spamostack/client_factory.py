from session import Session

import neutronclient.v2_0
import cinderclient.v3
import novaclient.v2
import glanceclient.v2


class OSClient(object):
    def __init__(self, cache):
        '''
        Create instance of `OSClient` class

        @param cahce: Reference to the cache
        @type cache: spamostack.cache.Cache
        '''

        self.cache = cache
        self.module = None
        self.client = None
        self._session = None

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        self.client = self.make()

    @session.deleter
    def session(self):
        del self._session

    def make(self):
        '''Makes an instance of client'''

        return self.module.Client(session=self.session.session)


class Keystone(OSClient):
    def __init__(self, cache):
        '''
        Create instance of `Keystone` class

        @param cahce: Reference to the cache
        @type cache: spamostack.cache.Cache
        '''

        super(Keystone).__init__(cache)

        from keystoneclient.v3 import client
        self.module = client
        self._session = Session(cache, self)

    def project_create(self):
        pass

    def project_update(self):
        pass

    def user_create(self):
        pass

    def user_update(self):
        pass
