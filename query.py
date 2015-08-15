#!/usr/bin/env python

import binascii
import sys

sys.path.append('gen-py')
from hfileservice.ttypes import *

from rpc import send_req, req_data

def send(url, method, hfile, keys):
  keys = [binascii.unhexlify(i) for i in keys]
  req = SingleHFileKeyRequest(hfileName=hfile, sortedKeys=keys)
  data = req_data(method, req)
  return send_req(url, method, data)

print send(sys.argv[1], 'getValuesSingle', sys.argv[2], sys.argv[3:])
