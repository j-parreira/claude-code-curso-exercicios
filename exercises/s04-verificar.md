# Sessão 4 — Verificar: testes, debugging, git

**Objectivo:** corrigir bugs com teste primeiro, em commits pequenos, e rever o diff antes do merge.

## Antes de começar

```bash
git switch -c s04 s4-start
claude
```

## Os bugs reportados

Chegaram três relatos de utilizadores. Descrevem o sintoma, não a causa.

1. *"Apaguei uma tarefa, acrescentei outra, e fiquei com duas tarefas com o mesmo número. Agora o `todo done` marca a errada."*
2. *"Tenho uma tarefa que é para hoje e já me aparece no `todo list --overdue`. Ainda não passou de prazo!"*
3. *"O `todo list --sort priority` mostra as tarefas de prioridade baixa primeiro. A ajuda diz que as mais importantes vêm primeiro."*

## Tarefa

Para cada bug, num branch próprio (`fix/ids-repetidos`, por exemplo, a partir do `s04`):

1. **Reproduz.** Cola no pedido o relato e os comandos que o reproduzem. Pede ao agente que encontre a causa, sem corrigir ainda.
2. **Teste primeiro.** Pede um teste que falhe por causa do bug. Corre-o e vê-o falhar, pelo motivo certo.
3. **Corrige.** Só agora a correcção. O teste passa, os outros também.
4. **Commit pequeno**, com mensagem `fix: ...`.
5. **Revê o diff com olho adversarial.** Numa sessão nova (`/clear`), pede ao agente que revê o diff do branch à procura do que pode correr mal. Lê tu o diff também: cada linha é tua.
6. Merge no `s04`.

O `query.py` não tem testes nenhuns. Antes de mexeres no bug 2 ou no bug 3, pede testes para o comportamento actual de `query.py` em `tests/unit/test_query.py`, e confirma que cobrem os dois bugs depois de corrigidos.

## Critérios de aceitação

- Um id nunca pertence a duas tarefas ao mesmo tempo
- Uma tarefa com data de hoje não está em atraso; com data de ontem, está
- `--sort priority` mostra `high`, depois `medium`, depois `low`
- Existe `tests/unit/test_query.py`, e cada bug tem um teste que falhava antes da correcção
- Um commit por correcção; o `git log` conta a história sem precisares de abrir os diffs

## Verificação

```bash
uv run pytest exercises/checks/test_s04.py && uv run pytest
```
