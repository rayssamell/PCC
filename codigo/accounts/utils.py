from django.core.mail import send_mail


def send_email_to_profissional(name, email, msg_subject, message, receiving_email):
    # Configurações de envio de email
    subject = f"Contato de {name}: {msg_subject}"
    body = f"Nome: {name}\nEmail: {email}\n\nMensagem: {message}"
    from_email = 'seu_email@example.com'  # Defina o email remetente
    to_email = [receiving_email]  # Email do profissional

    # Envie o email
    send_mail(subject, body, from_email, to_email)
