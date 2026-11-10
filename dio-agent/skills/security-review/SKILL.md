---
name: security-review
description: Use quando o estudante quer analisar código em busca de falhas de segurança, identificar vulnerabilidades, ou quando um código envolve autenticação, entrada de dados, banco de dados ou comunicação externa.
---

# Skill: Revisão de Segurança de Código

Revisão de segurança: analisa código em busca de falhas — SQL Injection, XSS, autenticação quebrada, exposição de dados sensíveis — com mapeamento para MITRE ATT&CK e verificação com testes.

## Quando usar

- O estudante quer revisar código em busca de falhas de segurança
- O código envolve autenticação, entrada de dados do usuário, banco de dados, arquivos ou comunicação externa
- Um bug de segurança precisa ser identificado ou um incidente precisa ser analisado

## Fluxo (na ordem exata)

### 1. Ler o código alvo

Não adivinhe. Use `read_file` para ler o código e localize:
- Funções que recebem entradas do usuário
- Consultas a banco de dados
- Armazenamento ou manipulação de senhas/credenciais
- Upload de arquivos
- Respostas HTTP ou renderização de conteúdo

### 2. Classificar a vulnerabilidade

Para cada ponto de entrada não confiável, classifique:

| Vuln. | O que é | Sinais de alerta no código |
|-------|---------|---------------------------|
| SQL Injection | Entrada interpolada em query SQL | `f"SELECT...{variavel}"`, `execute(f"...")` |
| XSS | HTML/JS injetado no navegador | `render(template, ...)` com entrada não escapada |
| Command Injection | Entrada executada como comando | `os.system()`, `subprocess()` com entrada |
| Path Traversal | Acesso a arquivos fora do diretório | `open()` com caminho contendo `..` |
| Insecure Direct Object Reference | Acesso a recurso por ID sem verificação de propriedade | `usuario_id = request.params['id']`, sem essa consulta |
| Sensitive Data Exposure | Dados sensíveis em texto puro ou expostos | Senha em `SELECT *`, `.env` commitado |
| Broken Authentication | Login/falha de controle de acesso | Comparação de senha sem hash, sem expiração de sessão |

### 3. Explicar a exploração

Dê pelo menos um payload concreto e mostre o que ele produz:

```sql
-- Exemplo: SQL Injection no login
usuario = "admin' --"
senha = "qualquer_coisa"
```

O que o código produz:

```sql
SELECT * FROM usuarios WHERE usuario = 'admin' --' AND senha = 'qualquer_coisa'
```

O `--` comenta o restante da query, ignorando a verificação de senha.

### 4. Mapeamento MITRE ATT&CK

Associe a técnica mais próxima:

- SQL Injection → **T1190** (Initial Access — Exploit Public-Facing Application)
- Command Injection → **T1059** (Execution)
- XSS → **T1190** (Initial Access, via exploração da web)
- Autenticação quebrada → **T1078** (Valid Accounts)
- Path Traversal → **T1005** (Collection de dados)

Se o mapeamento for ambíguo, diga "T1190 (mais provável)".

### 5. Corrigir

Aplicar a correção real — nunca só um filtro de "limpeza" na entrada:

| Falha | Correção |
|-------|----------|
| SQL Injection | Use consultas parametrizadas (`?` placeholders) |
| XSS | Escapa saída ou use templates auto-escapados |
| Command Injection | Evite execução de comandos com entrada de usuário; use APIs seguras |
| Path Traversal | Valide caminhos, use `os.path.realpath()` e controle o prefixo |
| Sensitive Data Exposure | Hash de senhas (bcrypt/argon2), nunca em texto puro |
| Broken Authentication | Tokens, rate limiting, sessões legítimas |

### 6. Verificar

Execute testes com casos de borda:

- Payload malicioso deve ser bloqueado (ex: `' OR '1'='1` não dá acesso)
- Entrada legítima deve funcionar normalmente
- Dados sensíveis não devem estar em texto puro no código ou no banco

## Regras de ouro

- **Corrigir, não só explicar.** A saída final é sempre código funcionando, não um relatório teórico.
- **Parâmetros `?` > sanitização.** Consultas parametrizadas são a correção primeira; filtros de entrada são de segunda linha.
- **Não expor o fix em produção.** Quando o fix for entregue, indique que a revisão foi aplicada e o que verificar em staging antes de deploy.
- **Testar o fix.** Um patch que não passa de testes não foi testado — rode casos de borda.

## Referências

- `../agent/knowledge/owasp-top10.md` — OWASP Top 10
- `../agent/knowledge/mitre-attck.md` — Técnicas MITRE ATT&CK
