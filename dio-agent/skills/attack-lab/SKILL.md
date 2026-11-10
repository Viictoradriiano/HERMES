---
name: attack-lab
description: Use quando o estudante quer estudar como falhas são exploradas em ambiente controlado e autorizado, ou quando ele quer entender a sequência de um ataque em um lab seguro.
---

# Skill: Laboratório de Ataque (Attack Lab)

Laboratório de ataque: estuda como falhas são exploradas em ambientes isolados e autorizados, seguindo práticas seguras e éticas.

## Quando usar

- O estudante quer entender como uma falha é explorada
- O estudante quer praticar em um ambiente controlado
- O estudante quer simular ataques para aprender defesa

## Princípios éticos

1. **Só ataque em ambientes autorizados.** Nunca teste em sistemas de terceiros sem permissão explícita.
2. **Use ambientes isolados.** VMs, containers, sandboxes ou o próprio sistema do estudante.
3. **Rode em horários controlados.** Evite atividades pesadas que possam gerar impacto.
4. **Registre o que faz.** Mantenha um log do que foi testado e o resultado.
5. **Relate aprendizado, não catastrofe.** Fale sobre o que aprendeu, não sobre como causar dano.

## Ambientes seguros para estudar

| Ambiente | Uso |
|----------|-----|
| Docker | Container isolado com serviços (SQLite, MySQL, etc.) |
| Vulnerable Web Apps | DVWA, OWASP Juice Shop, PortSwigger Web Security Academy |
| VMs preparadas | Metasploitable, Kali Linux (lab) |
| Sistema local | O próprio pc do estudante, em isolamento |

## Fluxo do laboratório

### 1. Estruture a sessão

- **Objetivo:** o que se vai aprender
- **Ambiente:** o que será usado
- **Tempo:** quanto tempo disponível
- **Risco:** o que está exposto (geralmente baixo em lab)

### 2. Recriar a falha

Crie um exemplo reproduzível:

```python
# App vulnerável (exemplo)
query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND senha = '{senha}'"
cursor.execute(query)
```

### 3. Provar a exploração

Acesse o sistema (sem querer danificar):

```text
usuario = admin' --
senha = qualquer coisa
```

Resultado esperado:
- Login realizado sem senha válida
- Acesso negado (senão devolvido erro)

### 4. Aplicar o controle

Substitua pelo código seguro:

```python
query = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
cursor.execute(query, (usuario, senha))
```

### 5. Verificar a correção

- Tenta novamente o payload vinculado — deve falhar
- Tenta com dados legítimos — deve funcionar
- Registra o resultado

### 6. Documentar aprendizados

- O que foi aprendido
- Como foi detectado
- Como foi corrigido
- Exemplo de código seguro

## Cuidados

| Cuidado | O que fazer |
|---------|-------------|
| Usar sistemas de terceiros | Só em ambientes próprios ou autorizados |
| Expor logs sensíveis | Não deixe senhas ou credenciais em logs |
| Alterar produção | Nunca teste em produção sem autorização |
| Usar ferramentas de rastreamento | Evite detectores de invasão em ambientes não preparados |

## Ferramentas úteis

| Ferramenta | Uso |
|------------|-----|
| `nmap` | Escaneamento de ports e serviços |
| `burpsuite` | Interceptar e modificar requisições HTTP |
| `sqlmap` | Automatização de SQL Injection (apenas em lab) |
| `zap` | Proxy de segurança para testes |
| `semgrep` | Análise estática de código |
| `bandit` | Análise estática de Python para falhas de segurança |

## Referências

- `../agent/knowledge/security-threat-modeling.md`
- `../agent/knowledge/mitre-attck.md`
