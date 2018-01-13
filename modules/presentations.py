#!/usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored

class Presentations(object):

    def __init__(self):
        pass

    @staticmethod
    def banner():
        print colored("""

            ██ ▄█▀ ██▓ ██▓     ██▓        ██▀███   ▒█████   █    ██ ▄▄▄█████▓▓█████  ██▀███
            ██▄█▒ ▓██▒▓██▒    ▓██▒       ▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
           ▓███▄░ ▒██▒▒██░    ▒██░       ▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
           ▓██ █▄ ░██░▒██░    ▒██░       ▒██▀▀█▄  ▒██   ██░▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄
           ▒██▒ █▄░██░░██████▒░██████▒   ░██▓ ▒██▒░ ████▓▒░▒▒█████▓   ▒██▒ ░ ░▒████▒░██▓ ▒██▒
           ▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
           ░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░     ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░     ░     ░ ░  ░  ░▒ ░ ▒░
           ░ ░░ ░  ▒ ░  ░ ░     ░ ░        ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░   ░         ░     ░░   ░
           ░  ░    ░      ░  ░    ░  ░      ░         ░ ░     ░                 ░  ░   ░

        								v2.0
            """, 'red', attrs=['bold'])

    @staticmethod
    def helpers():
        print colored("[*] By: Matheus Fidelis aka D0ctor", 'red', attrs=['bold'])
        print colored(
            "[!] Usage: ./kill-router.py -t [TARGET IP] -p [TARGET PORT] -u [USER TO TEST] -l [PATH TO PASSLIST]",
            'red', attrs=['bold'])
        print colored("[!] Usage: ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt", 'red',
                      attrs=['bold'])
        print colored("[!] Use -m to change request HTTP to HTTPS", 'red', attrs=['bold'])
        print colored("[!] ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt -m https", 'red',
                      attrs=['bold'])
        print colored("[!] ./kill-router.py --shodan apache2", 'red', attrs=['bold'])
        print ""
