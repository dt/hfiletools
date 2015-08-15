#!/usr/bin/env python

import binascii
import sys

sys.path.append('gen-py')

from thrift.protocol import *
from hfileservice.ttypes import *
from hfileservice.HFileService import Iface, Processor

class RpcHandler(Iface):
  def getValuesSingle(self, req): #SingleHFileKeyRequest
    print "getValuesSingle %s (%d)"%(req.hfileName, len(req.sortedKeys))
    for k in req.sortedKeys:
      print "\t" + binascii.hexlify(k)

  def getValuesMulti(self, req): #SingleHFileKeyRequest
    print "getValuesMulti"

  def getValuesForPrefixes(self, req): #PrefixRequest
    print "getValuesForPrefixes"

  def getValuesMultiSplitKeys(self, req): #MultiHFileSplitKeyRequest
    print "getValuesMultiSplitKeys"

  def getIterator(self, req): #IteratorRequest
    print "getIterator"

  def getInfo(self, req):
    print "getInfo"

  def testTimeout(self, waitInMillis):
    print "getValuesSingle"

  def read_thrift(self, content):
    processor = Processor(self)
    iprot = TBinaryProtocol.TBinaryProtocol(TTransport.TMemoryBuffer(content))
    oprot = TBinaryProtocol.TBinaryProtocol(TTransport.TMemoryBuffer())

    processor.process(iprot, oprot)

handler = RpcHandler()
handler.read_thrift(binascii.unhexlify(sys.argv[1]))
