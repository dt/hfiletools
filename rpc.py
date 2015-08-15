import binascii
import hashlib
import sys
import string
import struct

import requests
from thrift.protocol import *
from thrift.transport import *

sys.path.append('gen-py')
from hfileservice.ttypes import *
from hfileservice import HFileService

def req_data(method, req):
  sendbuf = TTransport.TMemoryBuffer()
  sendprot = TBinaryProtocol.TBinaryProtocol(sendbuf)
  client = HFileService.Client(None, sendprot)
  getattr(client, 'send_'+method)(req)
  return sendbuf.getvalue()

def send_req(url, method, req):
  r = requests.post(url, data=req)
  print ""
  print "Status:\t\t" +str(r.status_code)
  print "Hash:\t\t" + hashlib.md5(r.content).hexdigest()
  print "Content:\t" + filter(lambda x: x in string.printable, r.content)
  print "Hex:\t\t" + binascii.hexlify(r.content)
  print ""
  return recv(method, r.content)

def recv(method, data):
  recvbuf = TTransport.TMemoryBuffer(data)
  recvprot = TBinaryProtocol.TBinaryProtocol(recvbuf)
  client = HFileService.Client(recvprot)
  return getattr(client, 'recv_'+method)()
