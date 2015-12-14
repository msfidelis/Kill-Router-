#!/bin/bash
echo "INSTALANDO AS DEPENDENCIAS"
sudo apt-get install -y pip python 

echo "INSTALANDO AS DEPENDENCIAS DO PIP"
pip install termcolor
pip install argparse
pip install sys
pip install requests
