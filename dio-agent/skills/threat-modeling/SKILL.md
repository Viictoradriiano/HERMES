---
name: threat-modeling
description: Use quando o estudante quer analisar um sistema, aplicação ou componente para mapear ameaças, ativos, vetores de ataque e definição de controles de segurança.
---

# Skill: Análise de Ameaças (Threat Modeling)

Análise de ameaças: mapeia ativos, vetores de ataque e define controles de defesa para um sistema ou componente.

## Quando usar

- O estudante quer avaliar a segurança de um sistema ou aplicação
- Há necessidade de identificar o que está em risco e como proteger
- É o início de uma análise de segurança ou projeto

## Fluxo

### 1. Entenda o sistema

Pergunte:
- O que o sistema faz? (descrição geral)
- Quais são os ativos protegidos? (dados, credenciais, funcionalidades)
- Quem são os usuários e quais são os ataques possíveis?
- Quais são os limites do sistema? (onde ele se comunica)

### 2. Identificar ativos

Liste o que precisa ser protegido:

| Ativo | Tipo | Valor |
|-------|------|-------|
| Dados de usuários | Sensível | Alto |
| Credenciais de acesso | Muito Sensível | Muito Alto |
| Página de login | Funcional | Médio |
| API externa | Terceira Parte | Medio |

### 3. Identificar ameaças

Para cada ativo, liste ameaças possíveis:

| Ativo | Ameaça | Como |
|-------|--------|------|
| Dados de usuários | Roubo de acesso | SQL Injection, XSS |
| Credenciais | Acesso não autorizado | Autenticação falha |
| Página de login | Bypass de autenticação | SQL Injection no login |
| API | Exposição de dados | Autenticação ausente |

### 4. Avaliar risco

Use a fórmula:

```text
Risco = Probabilidade × Impacto
```

Classifique cada ameaça:

| Risco | Probabilidade | Impacto | Prioridade |
|-------|---------------|---------|------------|
| SQL Injection | Média | Crítico | Alta |
| XSS | Alta | Baixo | Média |
| Acesso não autorizado | Baixa | Alto | Média |

### 5. Definir controles

Para cada ameaça, defina controles de defesa:

| Ameaça | Controle |
|--------|----------|
| SQL Injection | Consultas parametrizadas |
| XSS | Escapa saída, Content-Security-Policy |
| Autenticação falha | Hash de senhas, rate limiting |
| Exposição de dados | Validação de permissões, autenticação |

### 6. Entregar o resultado

Apresente um relatório de análise com:

- Ativos identificados
- Ameaças mapeadas
- Nível de risco
- Controles recomendados

## Técnicas de ameaça

| Técnica | Como ocorre | Como prevenir |
|---------|-------------|---------------|
| SQL Injection | Entrada maliciosa em query | Parâmetros `?` no SQL |
| XSS | Script injetado no navegador | Escapa saída, CSP |
| Command Injection | Comando de usuário executado | Evitar execução de comandos |
| Path Traversal | Acesso a arquivos fora do diretório | Validar caminhos, `realpath()` |
| Autenticação quebrada | Controle de acesso por ID sem verificação | Verificar propriedade de recursos |

## Referências

- `../agent/knowledge/security-threat-modeling.md`
- `../agent/knowledge/owasp-top10.md`
- `../agent/knowledge/mitre-attck.md`
