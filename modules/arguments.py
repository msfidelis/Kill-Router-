#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from presentations import Presentations

class CLI(object):

    def __init__(self):
        pass

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description="Kill Router", add_help=False)
        parser.add_argument('-h', '--help', action=Presentations.helpers(), help='usage')
        parser.add_argument('-t', '--target', help='Informe o roteador alvo')
        parser.add_argument('-m', '--method', help='Informa o Método HTTP ou HTTPS')
        parser.add_argument('-p', '--port', help='Informa a porta')
        parser.add_argument('-l', '--passlist', help='Informa a passlist')
        parser.add_argument('-u', '--username', help='Informa o usuário a ser testado')
        parser.add_argument('-s', '--shodan', help='Informa a Dork do Shodan')

        args = parser.parse_args()

        # Default Values
        if args.username is None:
            args.username = "admin"

        if args.method == "http" and args.port is None:
            args.port = 80

        if args.method == "https" and args.port is None:
            args.port = 443

        if args.method == "ssh" and args.port is None:
            args.port = 22

        if args.method == "ftp" and args.port is None:
            args.port = 21

        return args