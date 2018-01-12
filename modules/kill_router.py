#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ftp import FTP
from ssh import SSH
from basic_auth import Basic_Auth
from passlists import Passlist

class Kill_Router(object):

    def __init__(self):
        pass

    def bruteforce(self,target,port,method,passlist,username):

        parser = Passlist(passlist)
        passwords = parser.get_list()

        if method == "http" or "https":
            attack = Basic_Auth()

        if method == "ssh":
            attack = SSH()

        if method == "ftp":
            attack = FTP()

            






