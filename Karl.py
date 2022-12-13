#!/usr/bin/env python3
import os
import sys
import json
try: from types import SimpleNamespace as Namespace
except ImportError: from argparse import Namespace
import httplib2
args = sys.argv
url = json.loads(open('./url.json').read(), object_hook=lambda d: Namespace(**d))
def send(_in, w): print(httplib2.Http().request(uri=w, method='POST', headers={'Content-Type': 'application/json; charset=UTF-8'},body=json.dumps(_in)))
def beemovie(w): with open('beemovie.txt') as f: for x in f.read().splitlines(): send(x,w)
def hilfe():
  t = f"""
Usage: cmd [OPTION] [idk]
this isnt done yet idk

    -h, --help             give this help list
    -g, --get              .
    -t, --text             send message to given user

"""
  print(t)
def usage(a):
  print(f"Error:   {a}  is not a valid entry")
  hilfe()
def _get():
  a = {"g":url.groups,"groups":url.groups,"group":url.groups,"p":url.people,"people":url.people}.get(args[2],usage(args[2]))
  for x in a:
    print(x)
def sw_1(a):
  sw = {
    "-h": hilfe(),
    "--help": hilfe(),
    "-g": _get(),
    "--get": _get()
  }
  return sw.get(a, usage(a))

def main():
  if args[1:]:
    sw_1(args[1])
  else: usage()

if __name__ == "__main__": main()
