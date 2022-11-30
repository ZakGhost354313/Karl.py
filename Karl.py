#!/usr/bin/env python3
import os
import sys
import json
try: from types import SimpleNamespace as Namespace
except ImportError: from argparse import Namespace
import httplib2
url = json.loads(open('./url.json').read(), object_hook=lambda d: Namespace(**d))
def send(_in, url): print(httplib2.Http().request(uri=url, method='POST', headers={'Content-Type': 'application/json; charset=UTF-8'},body=json.dumps(_in)))
def beemovie(_in): with open('beemovie.txt') as f: for x in f.read().splitlines(): send(x,who)
def main(args):
  if args[1:]:
    
  else: usage()

if __name__ == "__main__": main(sys.argv)