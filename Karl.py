#!/usr/bin/env python3
import os
import sys
import json
try: from types import SimpleNamespace as Namespace
except ImportError: from argparse import Namespace
import httplib2
args = sys.argv
url = json.loads(open('./url.json').read(), object_hook=lambda d: Namespace(**d))
def send(_in, url): print(httplib2.Http().request(uri=url, method='POST', headers={'Content-Type': 'application/json; charset=UTF-8'},body=json.dumps(_in)))
def beemovie(_in): with open('beemovie.txt') as f: for x in f.read().splitlines(): send(x,who)
def hilfe():
  t = f"""
Usage: cmd [OPTION] [idk]
this isnt done yet idk

    -h, --help             give this help list
    -g, --get              .
    -t, --text             send message to given user

"""
  print(t)
def usage(arg):
  print(f"Error:   {a}  is not a valid entry")
  hilfe()

def sw_1(a):
  sw = {
    "-h": hilfe(),
    "--help": hilfe(),
    "-g": get(),
    "--get": get()
  }
  return sw.get(a, usage(a))

def main():
  if args[1:]:
    sw_1(args[1])
  else: usage()

if __name__ == "__main__": main()
