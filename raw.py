#!/usr/bin/env python

import binascii
import sys

from rpc import send_req

def send(url, method, raw):
  data = binascii.unhexlify(raw)
  return send_req(url, method, data)

res = send(sys.argv[1], 'getValuesSingle', sys.argv[2])
print res
print "keycount %d (len: %d)"%(res.keyCount, len(res.values))
for k,v  in res.values.items():
  print "\t%s: %s"%(k, binascii.hexlify(v))
