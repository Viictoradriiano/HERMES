# Modelagem de Ameaças e Análise de Segurança

Contexto sobre segurança de sistemas para o agente entender onde o estudante está inserido.

## O que é segurança de sistemas

Segurança de sistemas é o conjunto de práticas, tecnologias e processos para proteger ativos digitais contra ameaças que possam comprometer confidencialidade, integridade ou disponibilidade de dados.

Os três pilares do modelo de segurança clássico (CIA Triad):

| Princípio | O que garante |
|-----------|---------------|
| **Confidencialidade** | Apenas pessoas autorizadas acessam as informações |
| **Integridade** | Os dados não foram alterados sem autorização |
| **Disponibilidade** | Os sistemas e dados estão acessíveis quando necessário |

## Conceitos fundamentais

### Ativos

Ativos são qualquer coisa que tenha valor para a organização ou para um atacante:

- Dados (pessoais, financeiros, comerciais)
- Sistemas operacionais e software
- Redes e infraestrutura
- Credenciais e autenticação
- Reputação e marca

### Vetores de ataque

Como uma ameaça chega ao alvo:

- Injeção de dados maliciosos (SQL, XSS)
- Acesso não autorizado a sistemas
- Engenharia social e phishing
- Exploiting de vulnerabilidades em software
- Interceptação de comunicação (MITM)
- Ataques de privilégio (escalonamento)
- Recursos físicos (acesso a servidores, portas)

### Linhas de defesa

Medidas para prevenir, detectar e responder a ataques:

- Prevenção: firewalls, WAF, autenticação forte, criptografia
- Detecção: monitoramento, IDS/IPS, logs, análise de comportamento
- Resposta: planos de resposta a incidentes, back-ups, recuperação

## Fluxo de análise de uma ameaça

1. **Identificar ativos** — o que está sendo protegido?
2. **Identificar ameaças** — o que pode atacar?
3. **Identificar vulnerabilidades** — como o ataque pode ser executado?
4. **Avaliar impacto e probabilidade** — o quão grave é e o quão provável?
5. **Definir controles** — o que vai prevenir, detectar ou responder?
6. **Validar** — os controles estão funcionando?

## Engenharia Social

Técnica de atacar a pessoa, não o sistema. O softwares são a porta de entrada mais comum:

- **Phishing** — e-mail falso, mas profissional, pedindo credenciais
- **Vishing** — phishing via voz (telefone)
- **Smishing** — phishing via SMS
- **Pretexting** — criação de uma situação (pré-texto) para persuadir
- **Baiting** — oferta irresistível para atrair a vítima
- **Tailgating** — segue uma pessoa acesso físico a um local protegido

## Princípios de segurança

- **Defesa em profundidade** — muitas camadas de proteção
- **Menor privilégio** — só conceder o que é necessário
- **Segredo** — a menor quantidade de informações possível
- **Completude de acesso** — quem tem acesso, tem registro
- **Segurança em profundidade** — proteção em cada nível
- **Falha fechando** — quando há dúvida, o sistema deve ser seguro
- **Confiar, mas verificar** — validar sempre a origem das requisições

## Conceitos de análise de risco

Fórmula básica:

```text
Risco = Probabilidade × Impacto
```

Onde:

- **Probabilidade** — a chance de a ameaça se materializar
- **Impacto** — o prejuízo se o risco se concretizar

## Ferramentas de análise e testes

| Ferramenta | Uso |
|------------|-----|
| `nmap` | Escaneamento de portas e serviços |
| `burpsuite` | Proxies de segurança para proxy com requisicoes HTTP |
| `OWASP ZAP` | Proxy de segurança aberto para testes de aplicações web |
| `sqlmap` | Automação de descoberta e exploração de SQL Injection |
| `feroxbuster` | Busca de diretórios e arquivos |
| `wasm-auditor` / `semgrep` | Análise estática de código |

> **Aviso:** use essas ferramentas apenas em ambientes que você tem permissão explícita para testar.
