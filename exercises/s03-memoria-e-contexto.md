# Sessão 3 — Memória e contexto

**Objectivo:** escrever a memória do projecto, para deixar de repetir instruções, e gerir a janela de contexto numa tarefa longa.

## Antes de começar

```bash
git switch -c s03 s3-start
claude
```

## Parte A — o `CLAUDE.md`

1. Corre o `/init` e lê o `CLAUDE.md` que ele gera.
2. Corta. Fica só o que o agente não consegue adivinhar sozinho: como correr os testes e o linter, onde vivem as tarefas, convenções deste projecto. Descrições do que cada ficheiro faz, ele lê no código.
3. Acrescenta uma convenção a sério, por exemplo "cada comando novo tem um teste em `tests/unit/test_cli.py`".
4. `/clear`, e pergunta-lhe como se correm os testes. Responde a partir do `CLAUDE.md`?

## Parte B — uma tarefa longa

Pede o comando `export` com os critérios abaixo. Pede também os testes e a secção do README.

A meio da tarefa, corre o `/context`. Quando o agente começar a repetir-se, a contradizer-se ou a esquecer as convenções do `CLAUDE.md`, decide, e anota o que decidiste e porquê:

- `/compact` — o trabalho está a correr bem, só falta espaço
- `/clear` — a conversa está contaminada; recomeças com o que está escrito nos ficheiros
- `/rewind` — o último passo estragou; voltas a antes dele

## Critérios de aceitação

- `todo export --format md` imprime todas as tarefas, feitas incluídas, uma por linha, por ordem de id: `- [ ] Título` ou `- [x] Título`
- `md` é o formato por omissão: `todo export` faz o mesmo
- `todo export --format csv` imprime CSV com o cabeçalho `id,title,priority,due,done`; `due` vazio quando não há data; `done` é `true` ou `false`; títulos com vírgulas ficam entre aspas
- `todo export --output FICHEIRO` escreve no ficheiro em vez de imprimir
- Existe um `CLAUDE.md` na raiz, com o comando dos testes
- Os testes existentes continuam a passar

## Verificação

```bash
uv run pytest exercises/checks/test_s03.py && uv run pytest
```
