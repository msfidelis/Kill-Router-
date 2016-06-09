#!/bin/bash

#VALIDA SE O USUÁRIO É ROOT OU SUDO
if [[ $EUID -ne 0 ]]; then
	echo -e "ESTE SCRIPT DEVE SER EXECUTADO COM PERMISSÕES DE ROOT \n"

exit 1
fi

echo "INSTALANDO AS DEPENDENCIAS"
extras/get-pip.py  

echo "INSTALANDO AS DEPENDENCIAS DO PIP"

chmod 777 extras/get-pip.py
extras/get-pip.py termcolor
extras/get-pip.py requests
extras/get-pip.py shodan
