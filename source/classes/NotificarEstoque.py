import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class NotificadorEstoque:
    def __init__(self, gerente_email):
        self.gerente_email = gerente_email

    def enviar_aviso_estoque_baixo(self, produtos):
        produtos_baixo_estoque = [produto for produto in produtos if produto.quantidade_estoque < produto.quantidade_minima]

        if produtos_baixo_estoque:
            assunto = "Aviso de Estoque Baixo - {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            mensagem = "Produtos com estoque abaixo do mínimo:\n\n"
            for produto in produtos_baixo_estoque:
                mensagem += "{} (Código: {}): {} unidades\n".format(produto.nome, produto.codigo, produto.quantidade_estoque)

            self.enviar_email(assunto, mensagem)

    def enviar_email(self, assunto, mensagem):
        remetente_email = "seu_email@gmail.com"  # Substitua pelo seu e-mail
        remetente_senha = "sua_senha"  # Substitua pela sua senha
        destinatario_email = self.gerente_email

        mensagem_email = MIMEMultipart()
        mensagem_email["From"] = remetente_email
        mensagem_email["To"] = destinatario_email
        mensagem_email["Subject"] = assunto

        mensagem_email.attach(MIMEText(mensagem, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as servidor_smtp:
            servidor_smtp.starttls()
            servidor_smtp.login(remetente_email, remetente_senha)
            servidor_smtp.send_message(mensagem_email)
