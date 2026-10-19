# todo — repositório de exercícios

Um gestor de tarefas em linha de comandos, pequeno de propósito: é o projecto em que trabalhas durante as cinco sessões do curso *Agentes de código com LLMs na prática*. Lê-se em dez minutos, e cada técnica nova cai sobre código que já conheces.

O projecto traz alguns problemas de propósito: vais encontrá-los nas sessões, não tens de os procurar agora.

## Instalação

Precisas do [uv](https://docs.astral.sh/uv/) e do git.

```bash
git clone <url-deste-repositório>
cd claude-code-curso-exercicios
uv sync
uv run pytest
```

## Utilização

```bash
uv run todo add "Entregar relatório" --priority high --due 2026-11-01
uv run todo list
uv run todo list --all --sort priority
uv run todo done 1
uv run todo rm 1
uv run todo import antigo.txt
```

As tarefas ficam em `tasks.json`, no directório actual. Para usar outro ficheiro: `TODO_FILE=/caminho/tarefas.json` (PowerShell: `$env:TODO_FILE = "C:\caminho\tarefas.json"`).

## Sessões

Cada sessão tem um enunciado em `exercises/` e uma tag com o ponto de partida. No início de cada sessão, cria um branch teu a partir da tag:

```bash
git switch -c s01 s1-start
```

| Sessão | Tag | Enunciado |
|---|---|---|
| 1 — Modelo mental e primeira sessão | `s1-start` | [`exercises/s01-primeira-sessao.md`](exercises/s01-primeira-sessao.md) |
| 2 — Comunicar e planear | `s2-start` | `exercises/s02-*.md` |
| 3 — Memória e contexto | `s3-start` | `exercises/s03-*.md` |
| 4 — Verificar: testes, debugging, git | `s4-start` | `exercises/s04-*.md` |
| 5 — Escala e segurança | `s5-start` | `exercises/s05-*.md` |

Todas as tags partem do mesmo código: se te atrasares, ou se uma sessão correr mal, recomeças limpo na tag seguinte. Os enunciados chegam um por sessão.

Cada enunciado termina num comando de verificação. Os testes de verificação ficam em `exercises/checks/` e não correm com o `uv run pytest` normal: correm-se um a um, como o enunciado indica.

## Estrutura

```text
src/todo/
  cli.py            comandos e argumentos
  models.py         a tarefa (Task)
  storage.py        leitura e escrita de tasks.json
  query.py          filtros e ordenação do list
  legacy_import.py  importação do formato todo.txt antigo
tests/unit/         testes
exercises/          enunciados e testes de verificação
```

## Licença

[MIT](LICENSE).
