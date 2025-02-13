# secureDB
Projeto: SecureDB - Sistema de Monitoramento e Auditoria de Acessos
# SecureDB - Sistema de Monitoramento e Auditoria de Acessos

SecureDB é um sistema de monitoramento e auditoria de acessos ao banco de dados, desenvolvido para detectar tentativas de invasão e alertar administradores sobre atividades suspeitas.

## 📌 Funcionalidades
- 🔒 **Registro Seguro de Usuários**: Hash de senhas usando `bcrypt` para armazenamento seguro.
- 📊 **Monitoramento de Acessos**: Cada tentativa de login é registrada com IP, data/hora e status (sucesso ou falha).
- 🚨 **Detecção de Tentativas de Invasão**: Bloqueio de IPs com múltiplas falhas de login e envio de alertas.
- 📬 **Notificações Automáticas**: Envio de e-mails para administradores ao detectar acessos suspeitos.
- 🌐 **Dashboard Web (Opcional)**: Interface simples para visualizar logs de acessos e tentativas de invasão.

## ⚙️ Tecnologias Utilizadas
- **Python**
- **Flask** (para a interface web)
- **SQLAlchemy** (para gerenciamento do banco de dados)
- **Bcrypt** (para segurança de senhas)
- **Smtplib** (para envio de e-mails)
- **Pandas** (para análise de logs)
- **PyCryptodome** (para criptografia de dados sensíveis)

## 🚀 Como Rodar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/felipedev2025/secureDB.git
