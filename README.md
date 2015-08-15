# hfiletools
Tools for debugging/interacting with Foursquare's `HFile` KV service, via thrift-over-http RPC.

Can be used to talk to [dt/thile](/dt/thile).

## keys.py
Takes the hex-encoded payload of an RPC request and dumps info about which method it is calling and the keys requested.

## same.py
Takes a method name and two hex-encoded RPC responses. Exits 0 if they are the same after deserialization, or prints a summary of each and exits 1 if not.

## raw.py
Takes a URL and a hex-encoded `getValuesSingle` RPC request, and prints a summary of the response.

## query.py
Takes a URL, an collection name and a series of hex-encoded keys. Constructs `getValuesSingle` request for those keys from that collection, sends it to the URL and prints a summary of the response.

