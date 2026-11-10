# 🦺 DIO Agent — Cibersegurança

> Seu mentor de **Cibersegurança Aplicada** para aprender a proteger sistemas, identificar vulnerabilidades e estudar ataques de forma ética e controlada.

O **DIO Agent** é um agente de IA especialista em segurança que acompanha você na sua jornada de aprendizado. Ele conhece conceitos de segurança de sistemas, mantimentos e protocolos de exploração em laboratório, além de ajudar a analisar código em busca de falhas de segurança.

Você não precisa instalar nada complicado. Em **3 passos simples**, o seu mentor de IA estará pronto para usar.

---

## ✨ Antes de começar: dois conceitos rápidos

Para usar o DIO Agent, basta entender duas palavras. As duas estão no [Glossário completo](docs/glossary.md), mas aqui vai a versão rápida:

- 🧠 **Agente de IA:** um programa que não apenas responde perguntas, mas executa tarefas para alcançar um objetivo. Diferença entre alguém que te explica o caminho e alguém que caminha junto com você. O DIO Agent é desse tipo: um tutor especializado em segurança.
- 🖥️ **Harness:** é o programa onde a conversa com o agente acontece. Vale a comparação: o agente é o professor, e o harness é a sala de aula. O mesmo professor pode dar aula em salas diferentes. Por isso o DIO Agent funciona em qualquer harness: você escolhe a "sala" no Passo 1, e o seu mentor continua o mesmo.

Pronto. Com isso já dá para começar.

---

## 🎯 O que o DIO Agent faz por você

| Você precisa de... | O DIO Agent... |
|--------------------|----------------|
| Saber por onde começar | Monta um plano de estudos de segurança no seu ritmo |
| Analisar código em busca de falhas | Revisa código com checklists de OWASP e MITRE ATT&CK |
| Entender um conceito de segurança | Explica de forma simples, com analogias e exemplos |
| Mapear ameaças de um sistema | Realiza análise de ameaças (threat modeling) |
| Estudar como uma falha é explorada | Roda laboratórios controlados e seguros |

Ele conhece os conceitos de segurança base: OWASP Top 10, MITRE ATT&CK, modelagem de ameaças, criptografia e boas práticas de segurança.

---

## 🚀 Comece em 3 passos

### 1️⃣ Escolha um harness

O harness é o programa que dá vida ao agente. Recomendamos o **Google Antigravity**, **Claude Code**, **Codex**, **OpenCode** ou **Hermes**. Cada um tem documentação oficial com o passo a passo para sua plataforma.

### 2️⃣ Baixe ou clone este repositório

**Opção A: com Git**

```bash
git clone https://github.com/digitalinnovationone/dio-agent.git
```

**Opção B: baixando o .zip**

Na página do repositório, clique no botão verde **Code** e depois em **Download ZIP**. Extraia a pasta em um lugar fácil de encontrar.

### 3️⃣ Configure o ambiente de estudo

Abra a pasta `dio-agent` no harness que você instalou. O harness lê automaticamente o arquivo `AGENTS.md` e o agente já sabe quem é: o seu mentor de **cibersegurança**.

> 🔄 **Fique de olho nas atualizações.** O repositório evolui com o tempo. Se usa Git, rode `git pull`; quem baixou o .zip, pode baixar novamente.

---

## 🧩 As skills do agente

Uma **skill** é uma habilidade do agente, descrita em um guia passo a passo. O DIO Agent vem com skills focadas em segurança:

| Skill | Para que serve |
|-------|----------------|
| [Revisão de código](skills/security-review/SKILL.md) | Analisa código em busca de falhas (SQLi, XSS, autenticação, etc.) com mapeamento MITRE ATT&CK |
| [Análise de ameaças](skills/threat-modeling/SKILL.md) | Mapeia ameaças de um sistema ou componente |
| [Laboratório de ataque](skills/attack-lab/SKILL.md) | Roda experimentos de segurança em ambientes controlados |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de segurança de forma didática |
| [Pesquisa na web](skills/web-search/SKILL.md) | Busca informações atuais sobre vulnerabilidades e patches |

Você não precisa "chamar" uma skill. O agente percebe o que você precisa e usa a skill certa sozinho.

---

## 📖 Estrutura do repositório

```text
dio-agent/
├── AGENTS.md                          # Definição do agente (fonte única de verdade)
├── CLAUDE.md                          # Atalho para o Claude Code
│
├── agent/
│   ├── persona.md                     # Personalidade e tom do agente
│   └── knowledge/
│       ├── security-threat-modeling.md   # Fundamentos de modelagem de ameaças
│       ├── owasp-top10.md                # OWASP Top 10 — riscos mais críticos
│       └── mitre-attck.md                # Referência de técnicas do MITRE ATT&CK
│
├── skills/
│   ├── README.md                      # O que são skills
│   ├── security-review/               # Skill: revisão de código com segurança
│   ├── threat-modeling/               # Skill: análise de ameaças
│   ├── attack-lab/                    # Skill: laboratórios controlados
│   ├── explain-concept/               # Skill: explicar conceitos
│   └── web-search/                    # Skill: pesquisa na web
│
└── docs/
    └── glossary.md                    # Glossário de termos
```

---

## 📖 Glossário rápido

Termos como *agente*, *harness*, *skill*, *modelagem de ameaças* e *MITRE ATT&CK* estão explicados com analogias simples no **[Glossário completo](docs/glossary.md)**. Se algum termo soar estranho, comece por lá.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você desde o início das jornadas de segurança. A ideia é simples: aprender a proteger sistemas fica mais fácil quando você tem um mentor a qualquer hora, com foco em ética, laboratório controlado e aprendizado prático.

Bons estudos, e vamos com segurança. 🔒
