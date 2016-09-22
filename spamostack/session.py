from keystoneauth1.identity import v3
from keystoneauth1 import session


class Session(object):
    def __init__(self, cache, parent=None):
        """
        Create instance of `Session` class

        @param cahce: Reference to the cache
        @type cache: spamostack.cache.Cache
        """

        self.user = None
        self.cache = cache
        self.parent = parent
        self._session = self.new_session()

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        pass

    @session.deleter
    def session(self):
        del self._session

    def new_session(self):
        """Initiate new session"""

        for key, value in self.cache["keystone"]["users"]:
            if not value["used"]:
                auth = v3.Password(auth_url=value["auth_url"],
                                   username=value["username"],
                                   password=value["password"],
                                   project_name=value["project_name"],
                                   user_domain_id=value["user_domain_id"],
                                   project_domain_id=value["project_domain_id"])
                self.cache["keystone"]["users"][key]["used"] = True
                self.user = self.cache["keystone"]["users"][key]

                return session.Session(auth=auth)
        return None

    def interrupt_session(self):
        """Interrupt old session"""

        if self.session:
            self.user["used"] = False
            self.session = None
