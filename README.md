# Keylogger

Programa que faz o monitoramento do teclado do usuário.

# Descrição

Esse programa foi escrito na linguagem Python e usou a biblioteca <a href="https://pypi.org/project/pynput/">Pynput</a> e <a href="https://docs.python.org/3/library/smtplib.html">SMTPLib</a> como base. Ele faz o monitoramento do teclado do usuário, armazenando o tipo de tecla que foi apertada em um arquivo texto e faz o envio desse arquivo texto para o email escolhido.

# Como funciona?

O programa quando inciado faz o monitoramento do teclado do computador do usuário que iniciou, armazenando todas as teclas que forem apertadas em um arquivo texto, que será criado assim que a primeira tecla for pressionada. Caso o usuário queria fazer o uso de enviar um email contendo esse arquivo texto criado pelo programa, ele precisará indicar o email do remetente, a senha do remetente, email do destinatário, título do email, a mensagem do email e o nome do arquivo que foi criado (já tem um nome escolhido, mas sinta-se a vontade de trocar). Para mais informações sobre enviar o email, sugiro que dê uma olhada no meu repositório sobre <a href="https://github.com/Iuri-Almeida/Enviar-Email">enviar email</a>.

# Instalação

É preciso ter o Python instalado no seu computador (<a href="https://www.python.org/downloads/">Python</a>, recomendado baixar a última versão). Das bibliotecas usadas nesse projeto, algumas já vem pré instaladas quando o Python é baixado no computador, sendo necessário somente fazer o <i>import</i> no código (já está feito). No entanto, têm uma que é preciso fazer a instalação:

* Pynput - Forma de instalação: <b>pip install pynput</b>

<b>Obs.:</b> Essa instalação pode ser feita pelo terminal do seu computador (necessário que já tenha o Python instalado) ou pelo <a href="https://www.jetbrains.com/pt-br/pycharm/download/">PyCharm</a>, se preferir.

# Uso

Após a instalação, para começar a usar basta clonar esse repositório e digitar o comando <b>python keylogger.py</b> no terminal ou rodar pelo PyCharm.
