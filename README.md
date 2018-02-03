# Kill-Router-
Ferramenta para quebrar senhas administrativas de roteadores Wireless, routers, switches e outras plataformas de gestão de serviços de rede autenticados. 


O KillRouter é um script mega simples que criei durante um experiência onde necessitava de uma ferramenta que me auxiliasse em um brute force de senhas simples em um roteador autenticado via JavaScript. Pedindo ajuda ao Dr. Google e aos universitários, obrigado Gambler, encontrei um método de enviar o request junto com a solicitação de usuário e senha no header para o roteador. É claro que existe o projeto THC Hydra, que inclusive gosto muito, nesse aspecto a ferramenta deixa um pouco a deseja no quesito de performance, podendo até enviar requisições perdidas por aí, e isso me levou a pensar em uma forma de simplificar o processo e executar a operação de uma forma quase 3 vezes mais rápida usando Python.


## FORMA DE USO 

Faça o clone do projeto:

```bash
git clone https://github.com/msfidelis/Kill-Router-.git  
```

Agora instale as dependências
Este passo é opcional, só para garantir que você tem todas as bibliotecas do python que o script utiliza.

```
cd Kill-Router-/  
chmod +x install-kill-router.sh  
./install-kill-router.sh  ```
```

```bash
Método de uso:
[!] Usage: ./kill-router.py -t [TARGET IP] -u [USER TO TEST] -p [PATH TO PASSLIST]  
[!] Usage: ./kill-router.py -t 192.168.0.1 -u admin -p passlist.txt  
```

```bash
Especificando uma porta para o ataque:
[!] Usage: ./kill-router.py -t [TARGET IP] -p [TARGET PORT] -u [USER TO TEST] -l [PATH TO PASSLIST]
[!] Usage: ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt

```


```bash
Utilizando ataques em URLs com SSL 
[!] Usage: ./kill-router.py -t [TARGET IP] -p [TARGET PORT] -u [USER TO TEST] -l [PATH TO PASSLIST] -m [PROTOCOL]
[!] Usage: [!] ./kill-router.py -t 192.168.0.1 -p 8080 -u admin -l passlist.txt -m https", 'red'
```

```bash
Fazendo buscas no Shodan com a API 
[!] Usage: ./kill-router.py -s [DORK]
[!] Usage: [!] ./kill-router.py -S Apache2
```

## Shodan 

* Para utilizar as buscas via [Shodan](https://shodan.io), será necessário se cadastrar previamente no [site](https://account.shodan.io/login) para adquirir sua API Key de desenvolvimento. 

* Assim que estiver com sua Key em mãos, adicione a mesma no arquivo `.env` na raiz do projeto.

# Tutoriais
* Uso e Instalação do Kill Router: http://www.nanoshots.com.br/2015/12/kill-router-brute-force-em-senhas-de.html
* Uso e configuração do Shodan Search: http://www.nanoshots.com.br/2016/06/kill-router-10-brute-force-em-massa-em.html
