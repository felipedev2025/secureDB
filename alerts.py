import smtplib
from email.mime.text import MIMEText

def send_alert(email, ip):
    msg = MIMEText(f"Atenção! Tentativas de login suspeitas detectadas do IP {ip}.")
    msg["Subject"] = "⚠ ALERTA: Tentativas de Invasão"
    msg["From"] = "seuemail@gmail.com"
    msg["To"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("seuemail@gmail.com", "sua_senha")
        server.sendmail(msg["From"], msg["To"], msg.as_string())

# Simulação de alerta
send_alert("admin@securedb.com", "192.168.1.10")
