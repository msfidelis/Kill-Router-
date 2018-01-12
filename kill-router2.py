#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from modules.kill_router import Kill_Router
from modules.presentations import Presentations
from modules.arguments import CLI

def main():

    Presentations.banner()
    args = CLI.parse()

    kill_router = Kill_Router()
    kill_router.bruteforce(args.target, args.port, args.method, args.passlist, args.username)

    # try:
    #     kill_router = Kill_Router()
    #     kill_router.bruteforce(args.target, args.port, args.method, args.passlist, args.username)
    # except:
    #     print "deu merda"
    #     sys.exit()

main()