# OWASP Top 10 — Riscos de Segurança para Aplicações Web

A **OWASP Top 10** é uma lista dos riscos de segurança mais críticos para aplicações web, publicada pela Open Web Application Security Project. A seguir, uma visão geral dos principais itens e como proteger-se deles.

> **Nota:** Esta lista é referência educacional. O objetivo é estudar a defesa, não a exploração de sistemas sem autorização.

| VULNERABILIDADE | O QUE É | CÓDIGO VULNERÁVEL EXEMPLO | COMO PROTEGER |
|-----------------|---------|---------------------------|---------------|
| **A01:2021 — Acesso a API Inseguras** | APIs que expõem dados sem autenticação ou com controle de acesso fraco. | `GET /api/users/123` retorna dados de qualquer usuário. | Validar autenticação e autorização em cada rota de API. Usar IDs amigáveis. |
| **A02:2021 — Criptografia Quebrada** | Senhas, tokens ou dados sensíveis armazenados ou transmitidos sem criptografia ou com algoritmos fracos. | Armazenar `senha = "123456"` em texto puro no banco. | Usar `bcrypt`/`argon2` para senhas. Criptografar dados sensíveis. |
| **A03:2021 — Injeção** | Execução de código SQL, comando, etc., por entrada não filtrada. | `query = f"SELECT * FROM usuarios WHERE usuario = '{usuario}'"` | Usar consultas parametrizadas/prepared statements. |
| **A04:2021 — Deserialização Insegura** | Reconstrução de objetos de dados inseguros que podem executar código malicioso. | `pickle.loads(data)` com dados de entrada não confiável. | Evitar deserialização de dados de fontes não confiáveis. Usar formatos seguros. |
| **A05:2021 — Configurações Padrão** | Servidores, bancos e aplicativos com padrões de configuração fracos ou expostos. | `admin:admin` no banco de dados; `.env` commitado. | Remover credenciais padrão. Configurar em produção. |
| **A06:2021 — Vulnerabilidades de Componentes** | Bibliotecas com vulnerabilidades conhecidas não atualizadas. | Dependência `vulnerable-lib@1.0` sem atualização. | Monitorar dependências (Dependabot, Snyk). Manter atualizadas. |
| **A07:2021 — Autenticação e Gerenciamento Falhos** | Controle de acesso com falhas na autenticação, concessão de sessão, ou gerenciamento de credenciais. | Permitir login com `admin' --`. | Parâmetros `?` para queries. Hash de senhas. Expiração de sessão. |
| **A08:2021 — Falhas de Log e Monitoramento** | Falha de registro e monitoramento que impede detecção de ataques. | Nenhum log de login, erros ou tentativas de acesso. | Registrar eventos de segurança. Alertar em tempo real. |
| **A09:2021 — Falhas de Controle de Acesso** | Permissão insuficiente ou ausência de controle de acesso entre usuários. | `admin:admin` nas funções de administrador. | Proteger cada recurso por role. Validar permissões em cada rota. |
| **A10:2021 — Falhas de Controle de Acesso a Servidores** | Servidor expondo arquivos e recursos internos. | `../` em caminhos do filesystem (path traversal). | Validar entre filtros de entrada. Usar APIs de acesso a arquivos seguras. |

## Como usar este documento

1. **Identifique a tecnologia** — web, API, mobile, infraestrutura.
2. **Mapeie vulnerabilidades** — percorra a lista e veja quais se aplicam.
3. **Priorize por risco** — use `Risco = Probabilidade × Impacto`.
4. **Implemente controles** — use as soluções recomendadas.
5. **Valide** — teste a correção com métodos seguros.

## Recursos oficiais

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
