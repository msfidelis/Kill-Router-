#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue

from os import path
from termcolor import colored

class Passlist(object):

    def __init__(self, passlist=None):
        self._passlist = passlist
        self._currpath = path.dirname(path.realpath(__file__))

        self._passlist10 = "/../extras/wordlists/10.txt"
        self._passlist100 = "/../extras/wordlists/100.txt"
        self._passlistAM = "/../extras/wordlists/Ashley_Madison.txt"
        self._passlistStp = "/../extras/wordlists/stupid.txt"

    def get_list(self):

        if self._passlist is None:
            self.select_default_lists()

        fd = open(self._passlist, 'rw')
        passwordList = fd.readlines()
        passwords = Queue.Queue()

        for password in passwordList:
            password = password.rstrip()
            passwords.put(password)

        return passwords

    def select_default_lists(self):

        print ""
        print colored("[*] DEFINE A DEFAULT WORDLIST:", 'blue', attrs=['bold'])
        print colored("[+] 1 - Top 10~ Passwords Wordlist", 'blue', attrs=['bold'])
        print colored("[+] 2 - Top 100~ Passwords Wordlist", 'blue', attrs=['bold'])
        print colored("[+] 3 - Ashley Madison Wordlist", 'blue', attrs=['bold'])
        print colored("[+] 4 - Stupid Passwords Wordlist", 'blue', attrs=['bold'])

        response = int(raw_input("[!] SELECT A WORDLIST: "))

        if response == 1:
            passlist = self._passlist10
        elif response == 2:
            passlist = self._passlist100
        elif response == 3:
            passlist = self._passlistAM
        elif response == 4:
            passlist = self._passlistStp

        self._passlist = path.dirname(path.realpath(__file__)) + passlist