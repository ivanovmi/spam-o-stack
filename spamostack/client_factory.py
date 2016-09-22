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

    def get_unused(self, resource):
        

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


'''from cinderclient.v3.client import Client
Client.volumes.create(self, size, consistencygroup_id, group_id, snapshot_id, source_volid, name, description, volume_type, user_id, project_id, availability_zone, metadata, imageRef, scheduler_hints, source_replica, multiattach)
Client.volumes.update(self, volume)
Client.volumes.get(self, volume_id)
Client.volumes.list(self, detailed, search_opts, marker, limit, sort_key, sort_dir, sort)
Client.volumes.delete(self, volume, cascade)
Client.groups.create(self, group_type, volume_types, name, description, user_id, project_id, availability_zone)
Client.groups.update(self, group)
Client.groups.get(self, group_id)
Client.groups.list(self, detailed, search_opts)
Client.groups.delete(self, group, delete_volumes)
'''

'''from neutronclient.v2_0.client import Client'''

'''from novaclient.v2.client import Client'''

'''from glanceclient.v2.client import Client
Client.images.create(self)
Client.images.update(self, image_id, remove_props)
Client.images.get(self, image_id)
Client.images.list(self)
Client.images.delete(self, image_id)
'''

'''from keystoneclient.v3.client import Client
Client.projects.create(self, name, domain, description, enabled, parent)
Client.projects.update(self, project, name, domain, description, enabled)
Client.projects.get(self, project, subtree_as_list, parents_as_list, subtree_as_ids, parents_as_ids)
Client.projects.list(self, domain, user)
Client.projects.delete(self, project)
Client.endpoints.create(self, service, url, interface, region, enabled)
Client.endpoints.update(self, endpoint, service, url, interface, region, enabled)
Client.endpoints.get(self, endpoint)
Client.endpoints.list(self, service, interface, region, enabled, region_id)
Client.endpoints.delete(self, endpoint)
Client.users.create(self, name, domain, project, password, email, description, enabled, default_project)
Client.users.update(self, user, name, domain, project, password, email, description, enabled, default_project)
Client.users.get(self, user)
Client.users.list(self, project, domain, group, default_project)
Client.users.delete(self, user)
Client.groups.create(self, name, domain, description)
Client.groups.update(self, group, name, description)
Client.groups.get(self, group)
Client.groups.list(self, user, domain)
Client.groups.delete(self, group)


class OSClient(object):
    def __init__(self, cache):
        self.cache = cache

    def get_unused(self, rcinderclient.v3esources):
        pass


class Keystone(OSClient, Client):
    def __init__(self, cache):
        super(Keystone, self).__init__()
        self.cache = cache

        self._projects_create = self.projects.create
        self.projects.create = self.complement(self._projects_create)

    def complement(self, func):
        return func(name=self.get_unused(self.cache["projects"]["name"]),
                    domain=self.get_unused(self.cache["domain"]),
                    enabled=True)
'''






