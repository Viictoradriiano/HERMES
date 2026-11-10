import sqlite3
import hashlib
import hmac
import secrets

# Tamanho do salt em bytes (16 bytes = 128 bits de aleatoriedade)
_TAMANHO_SALT = 16


def _gerar_hash(senha, salt=None):
    """Gera salt + hash SHA-256 de uma senha.

    Retorna (salt_hex, hash_hex) no formato 'salt$hash'.
    """
    if salt is None:
        salt = secrets.token_hex(_TAMANHO_SALT)
    hash_bytes = hashlib.sha256((salt + senha).encode('utf-8')).digest()
    return f"{salt}${hash_bytes.hex()}"


def _verificar_senha(senha, hash_armazenada):
    """Verifica se a senha fornecida corresponde ao hash armazenado.

    Suporta dois formatos:
      - Novo: 'salt_hex$hash_hex' (gerado com _gerar_hash)
      - Legado: texto puro (compatibilidade com banco antigo)
    """
    if '$' in hash_armazenada:
        salt, hash_comparacao = hash_armazenada.split('$', 1)
        hash_calculado = hashlib.sha256((salt + senha).encode('utf-8')).digest().hex()
        return hmac.compare_digest(hash_calculado, hash_comparacao)
    # Senha legada em texto puro — compatibilidade, mas não segura
    return hmac.compare_digest(senha, hash_armazenada)


def _atualizar_senha_hash(usuario, nova_hash):
    """Atualiza o hash de senha no banco (útil para migração de legado)."""
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    cursor.execute("UPDATE usuarios SET senha = ? WHERE usuario = ?", (nova_hash, usuario))
    conexao.commit()
    conexao.close()


def criar_usuario(usuario, senha):
    """Cria um usuário com senha already hasheada.

    Retorna True se o usuário foi criado, False se já existia.
    """
    hash_senha = _gerar_hash(senha)
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", (usuario, hash_senha))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()


def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    cursor = conexao.cursor()

    # Consulta parametrizada: busca apenas pelo usuário
    cursor.execute("SELECT senha FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado is None:
        return "Acesso Negado!"

    senha_hash = resultado[0]

    if _verificar_senha(senha, senha_hash):
        return "Acesso Permitido!"
    return "Acesso Negado!"
