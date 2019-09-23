import os
import sys


sys.path.append('/usr/src/app/consul/')

ENV_TYPE = os.environ.get('ENV_TYPE', 'development')

workers = 2
reload = False
if ENV_TYPE == 'production':
    workers = 4
elif ENV_TYPE == 'development':
    reload = True
    workers = 1

address = '0.0.0.0'
port = 80
bind = "%s:%s" % (address, port)
