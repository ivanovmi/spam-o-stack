from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

from random import randint
import time


def rotate(period, number, repeat, method, params):
    for idx in xrange(repeat):
        n = 0
        while (n < number):
            time.sleep(randint(0, period / number))
            method(params)
            n += 1

def main():
    auth = v3.Password(auth_url="http://192.168.122.218:5000/v3",
                       username="admin", password="secret",
                       project_name="admin", user_domain_id="default",
                       project_domain_id="default")
    sess = session.Session(auth=auth)

if __name___ == "__main__()":
    main()
