from database import session, AccessLog
import datetime

# Função para registrar tentativas de login
def log_access(username, ip, status):
    new_log = AccessLog(username=username, ip=ip, timestamp=datetime.datetime.now(), status=status)
    session.add(new_log)
    session.commit()

# Simulação de login falho
log_access("admin", "192.168.1.10", "Falha")
