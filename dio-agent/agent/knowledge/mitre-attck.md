# MITRE ATT&CK — Referência de Técnicas

O **MITRE ATT&CK** (Adversarial Tactics, Techniques, and Common Knowledge) é um repositório público de técnicas e táticas usadas por atacantes em ambientes reais. O objetivo é ajudar defensores a compreendem como os ataques ocorrem e como proteger-se deles.

> **Uso educacional:** Este documento é referência para estudar mapeamentos de falhas. O objetivo do DIO Agent é ajudar a entender e prevenir ataques — nunca a realizar investigações não autorizadas.

## Como usar este documento

1. **Identifique a falha** no código ou sistema.
2. **Mapeie para a técnica** mais próxima.
3. **Entenda o contexto** de uso da técnica.
4. **Aplique controles** para prevenir e detectar.

## Métrica de Técnica (estratégia)

Técnicas são agrupadas em Estratégias (Tactics) que representam as fases do ataque. As principais estratégias:

| Estratégia | O que representa |
|------------|------------------|
| **Initial Access** | Como o atacante ganha acesso inicial ao sistema |
| **Execution** | Como o código malicioso é executado |
| **Persistence** | Como o atacante mantém acesso ao longo do tempo |
| **Privilege Escalation** | Como o atacante ganha privilégios mais altos |
| **Defense Evasion** | Como o atacante evita detecção |
| **Credential Access** | Como o atacante obtém credenciais |
| **Discovery** | Como o atacante explora o ambiente para entender |
| **Lateral Movement** | Como o atacante se move para outros sistemas |
| **Collection** | Como o atacante coleta dados de interesse |
| **Exfiltration** | Como o atacante extrai dados |
| **Impact** | Como o atacante causa dano |

## Técnicas relevantes para análise de código

| TÉCNICA (ID) | ESTRATÉGIA | O QUE É | MAPEAMENTO COM FALHA |
|--------------|------------|---------|----------------------|
| **T1190** | Initial Access | Explorar aplicação publicada para obter acesso | SQL Injection, XSS, RCE |
| **T1059** | Execution | Uso de shell, scripts ou linguagem para executar comandos | Command Injection |
| **T1078** | Initial Access | Usar contas válidas (credenciais roubadas ou burlando) | SQLi de autenticação, credenciais fracas |
| **T1505** | Persistence | Implantar red flags em sistemas (web shells) | Upload malicioso de arquivos |
| **T1005** | Collection | Acessar dados locais do sistema | Exposição de dados |
| **T1110** | Credential Access | Forçar ou roubar credenciais (brute force, dictionary) | Login sem rate limit |
| **T1133** | Initial Access | Acesso a serviços remotos (VPN, RDP, SSH) | Configurações fracas |
| **T1210** | Lateral Movement | Explorar vulnerabilidades para se mover entre sistemas | Serviços com credenciais expostas |
| **T1021** | Lateral Movement | Uso de protocolos remotos para execução (RDP, SSH, WinRM) | Acesso não autorizado a serviços |
| **T1098** | Persistence | Alterar contas ou configurações para manter acesso | Senhas default, admins sem controle |

## Mapa rápido de falhas comuns → MITRE

| FALHA | TÉCNICA MITRE | MELHOR PRÁTICA DE DEFESA |
|-------|---------------|---------------------------|
| SQL Injection | T1190 (Initial Access), T1005 (Collection) | Consultas parametrizadas |
| XSS (Reflected/DOM) | T1190, T1505-Downloaded Executable (na web) | Validação de entrada, escaping |
| Command Injection | T1059 (Execution) | Evitar execução de comandos com entrada de usuário |
| Path Traversal | T1005 (Collection) | Validação de paths, usar APIs seguras |
| Autenticação quebrada | T1078 (Valid Accounts) | Tokens, hash de senhas, rate limit |
| SSTI (Server-Side Template Injection) | T1190, T1505 | Evitar renderização de template com entrada de usuário |
| CSRF | T1190 | Tokens CSRF, validating bots |
| File Upload Malicious | T1505 (Persistence) | Validação de tipos, armazenamento de arquivos |
| DoS | T1499 (Endpoint Denial of Service) | Limites de taxa, rate limiting |

## Como estudar com este documento

1. **Encontre a falha** no código (ex: SQL Injection).
2. **Busque a técnica** no MITRE (ex: T1190).
3. **Leia a descrição** da técnica para entender o contexto.
4. **Mapeie para fitures** do seu código para ver onde a falha pode ocorrer.
5. **Implemente controles** e valide.
6. **Repita** com novas ameaças não válidas.

## Ferramentas de mapeamento

| Ferramenta | Uso |
|------------|-----|
| `mitreattck` CLI | Consulta local de técnicas e arquivos |
| `owasp-dependency-check` | Verifica dependências com CVE |
| `semgrep` | Análise estática de código com regras de segurança |
| `bandit` | Análise estática de Python para falhas de segurança |
| `zaproxy` | Proxy de segurança para testes de aplicações web |

## Referências úteis

- MITRE ATT&CK Enterprise Matrix: https://attack.mitre.org/matrices/enterprise/
- MITRE ATT&CK for Web Applications: https://attack.mitre.org/matrices/enterprise-web/
- MITRE ATT&CK for MSTIC (IoT): https://attack.mitre.org/matrices/
