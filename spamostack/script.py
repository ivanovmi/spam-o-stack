from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

auth = v3.Password(auth_url="http://192.168.122.218:5000/v3", username="admin",
                   password="secret", project_name="admin",
                   user_domain_id="default", project_domain_id="default")

sess = session.Session(auth=auth)
keystone = client.Client(session=sess)

print(keystone.projects.list())
