import binascii
import hashlib
import sys
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
  print r
  print hashlib.md5(r.content).hexdigest()
  print binascii.hexlify(r.content)
  recv(method, r.content)

def recv(method, data):
  recvbuf = TTransport.TMemoryBuffer(data)
  recvprot = TBinaryProtocol.TBinaryProtocol(recvbuf)
  client = HFileService.Client(recvprot)
  return getattr(client, 'recv_'+method)()
