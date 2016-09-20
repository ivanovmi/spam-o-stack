from keystoneclient.v3 import client

class KeystoneSim(object):
    def __init__(self, session):
        '''
        Creates `KeystoneSim` object

        @param session: Session object of `keystoneauth1`
        @type session: `keystoneauth1.session`
        '''

        self.keystone = client.Client(session=session)
        self.keystone.users.

    def user_create(self):
        pass

    def user_update(self):
        pass
