#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from os import path

class Log(object):

    @staticmethod
    def found(target, port, username, password, method):

        logfile = path.dirname(path.realpath(__file__)) + "/../results2.csv"

        log = "echo '%s;%s;%s;%s;%s' >> %s" % (target, port, username, password, method, logfile)
        subprocess.call(log, shell=True)
        return True