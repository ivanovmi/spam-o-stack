from keystoneclient.v3 import client

class KeystoneSim(object):
    def __init__(self, session):
        '''
        Creates `KeystoneSim` object

        @param session: Session object of `keystoneauth1`
        @type session: `keystoneauth1.session.Session`
        '''

        self.keystone = client.Client(session=session)
        self.keystone.projects.crea

    def project_create(self):
        pass

    def project_update(self):
        pass

    def user_create(self):
        pass

    def user_update(self):
        pass

    def action(self):
        pass
