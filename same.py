#!/usr/bin/env python

import binascii
import sys

sys.path.append('gen-py')
from hfileservice.ttypes import *

from rpc import recv

first = recv(sys.argv[1], binascii.unhexlify(sys.argv[2]))
second = recv(sys.argv[1], binascii.unhexlify(sys.argv[3]))

def pretty(s):
  if s is None:
    return s
  return binascii.hexlify(s)

def same(a, b):
  if a == b:
    sys.exit(0)
  print "keyCount: %d vs %d"%(a.keyCount, b.keyCount)
  keys = set(a.values.keys() ++ b.values.keys())
  print "values: "
  for i in keys:
    print "%d:\t%d\t%s"%(pretty(a.values.get(i)), pretty(b.values.get(i)))
