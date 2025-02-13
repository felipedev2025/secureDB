import bcrypt

# Função para criptografar senhas
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode(), salt)
    return hashed_pw

# Função para verificar senhas
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)
