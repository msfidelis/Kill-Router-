#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from os.path import join, dirname
from dotenv import load_dotenv
from modules.kill_router import Kill_Router
from modules.presentations import Presentations
from modules.arguments import CLI

def main():

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path, verbose=True)

    Presentations.banner()
    args = CLI.parse()

    kill_router = Kill_Router()

    if args.shodan != None:
        kill_router.shodan_search(args)
    else:

        if args.method is None:
            args.method = "http"

        kill_router.bruteforce(args.target, args.port, args.method, args.passlist, args.username)

    # try:
    #     kill_router = Kill_Router()
    #     kill_router.bruteforce(args.target, args.port, args.method, args.passlist, args.username)
    # except:
    #     print "deu merda"
    #     sys.exit()

main()