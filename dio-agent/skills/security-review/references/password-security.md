# Guia: Armazenamento e Comparação de Senhas

Tópicos avançados de segurança de senhas — aprofundados apenas quando o código envolve autenticação ou armazenamento de credenciais.

## Princípio de Ouro

**Nunca** armazene senhas em texto puro. Sempre armazene um hash criptograficamente seguro.

## Evolução Segura de Senhas

### Nível 0 — Senha em texto puro (crítico)
```python
# PERIGOSO: expõe senhas se o banco é vazado
SELECT senha FROM usuarios WHERE usuario = ?
```
**Risco:** exponencial de dados, quebras de conta, segredos de acesso.

### Nível 1 — SHA-256 sem sal (inadequado)
```python
# INADEQUADO: atacante pode usar tabelas de rainbow
hashlib.sha256(senha.encode()).hexdigest()
```
**Risco:** hash sem sal é derivado de uma entrada fixa. Atacante comolve o hash, pode usar tabelas pré-computadas. Não recomendado.

### Nível 2 — SHA-256 com sal aleatório
```python
salt = secrets.token_hex(16)  # 128 bits de aleatório
hash_bytes = hashlib.sha256((salt + senha).encode('utf-8')).digest()
hash_hex = f"{salt}${hash_bytes.hex()}"
```
**Vantagem:** sal diferente a cada senha. Bloqueia rainbow tables.
**Problema:** SHA-256 é rápido por design (ótimo para verificação de dados). Não é ideal para senhas.

### Nível 3 — bcrypt / argon2 (recomendado)
```python
import bcrypt
# Gerar hash
salt = bcrypt.gensalt(rounds=12)
hash_bytes = bcrypt.hashpw(senha.encode('utf-8'), salt)
# Verificar
bcrypt.checkpw(senha.encode('utf-8'), hash_bytes)
```
**Vantagem:** contas de custo computacional, adaptável à capacidade do hardware. Padronizados.
**Uso:** smtp, redes, sistemas de login modernos.

### Nível 4 — Argon2 (mais robusto)
```python
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash(senha)
ph.verify(hash, senha)
```
**Vantagem:** lento por design, resiste a ataques de força bruta.
**Uso:** apps web modernos, bancos de dados críticos.

## Comparação de Hashes (Evite Timing Attacks)

Sempre compare hashes com `hmac.compare_digest` — operação em tempo constante (não depende dos bytes):

```python
import hmac
import hashlib

# CORRETO: tempo constante
def verificar_senha(senha, hash_arquivado):
    novo_hash = hashlib.sha256((salt + senha).encode('utf-8')).digest().hex()
    return hmac.compare_digest(novo_hash, hash_arquivado)

# INCORRETO: expõe tempo de comparação (vuln. de timing)
if hash_arquivado == hash_calculado:
    return True
```

**Falha:** se a comparação for cedo ou tarde dependendo dos bytes, atacante pode recuperar o hash byte a byte.

## Estrutura de Armazenamento

Formato recomendado para armazenamento no banco:

```text
salt_hex$hash_hex
ex: 3f2a1b4c...$9e8d7c6b...
```

- `salt_hex` — 32 caracteres (16 bytes de sal)
- `hash_hex` — 64 caracteres (SHA-256 de salt + senha)
- Separador `$` (não deve aparecer nos campos)

## Checklist de Validação

- [ ] Senhas não estão em texto puro no código nem no banco
- [ ] Sal é gerado com `secrets.token_hex()` (não `random`)
- [ ] Tamanho do sal ≥ 16 bytes (128 bits)
- [ ] Comparação usa `hmac.compare_digest`
- [ ] Validação de entrada de senha (tamanho mínimo, não recusa especial)
- [ ] Rate limiting para tentativas de login
- [ ] Bloqueio de conta após múltiplas falhas

## Referência

- OWASP Password Storage Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- NIST SP 800-63B (Digital Identity Guidelines): https://pages.nist.gov/800-63-3/sp800-63b.html
