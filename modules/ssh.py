#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pexpect import pxssh
from termcolor import colored
from log import Log

class SSH(object):

    def __init__(self):
        pass

    def validate(self, target, port):

        try:
            s = pxssh.pxssh()
            s.login(target,username="root",port=port)
            return True
        except Exception, e:

            if str(e) == "Could not establish connection to host":
                print colored("[X] UNABLE TO CONNECT ", 'red', attrs=['bold'])
                return False
            else:
                return True

    def attack(self, target, port, username, password, method):

        try:
            s = pxssh.pxssh()
            s.login(target,username,password,port=port)

            return True

        except Exception, e:
            return False
        
    def brute_force(self, target, port, username, passwords, method):

        print ""
        print colored("==========================[STARTING TEST]==========================", 'yellow', attrs=['bold'])
        print colored("STARTING SSH TEST ON HOST: %s:%s", 'blue', attrs=['bold']) % (target, port)
        print ""

        i = 0

        if self.validate(target, port):

            while not passwords.empty():

                i = i + 1

                password = passwords.get()

                print colored('[%s]         USER[%s]          PASS [%s]', 'yellow') % (i, username, password)

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

                    Log.found(target, port, username, password, method)

                    return True

