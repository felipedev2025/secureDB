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
   
2. Entre no diretório do projeto:

cd secureDB

3. Instalar as dependências:

pip install -r requirements.txt

4. Executar uma aplicação:

python app.py

📝 Estrutura do Projeto



SecureDB/
│── app.py              # Arquivo principal do sistema
│── database.py         # Configuração do banco de dados
│── models.py           # Modelos do banco de dados
│── security.py         # Funções de segurança (hash, criptografia)
│── monitor.py          # Sistema de monitoramento de acessos
│── alerts.py           # Envio de alertas por e-mail
│── logs/               # Diretório onde os logs de acessos serão armazenados
│── templates/          # Arquivos HTML (se for usar Flask)
│── static/             # Arquivos CSS e JavaScript (se for usar Flask)
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação do projeto

🛡️ Segurança Implementada
Senhas criptografadas com bcrypt.
Proteção contra ataques de força bruta , bloqueando IPs com múltiplas falhas de login.
Envio de alertas automáticos para acessos suspeitos.
Registro detalhado de acessos , para auditorias de segurança.

📩 Contato
Caso tenha dúvidas ou sugestões, entre em contato: 📧 Email: felipefragoso2025@gmail.com
