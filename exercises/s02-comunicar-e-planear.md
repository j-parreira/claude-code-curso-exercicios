# Sessão 2 — Comunicar e planear

**Objectivo:** ver a diferença entre um pedido vago e um pedido com critérios de aceitação e plano.

A funcionalidade é a mesma nas duas rondas: **etiquetas (tags) nas tarefas**. Toca em vários ficheiros (`models.py`, `storage.py`, `query.py`, `cli.py`), por isso vale a pena planear.

## Ronda A — o pedido vago

```bash
git switch -c s02-vago s2-start
claude
```

Pede só isto, e aceita o que vier:

> Adiciona tags às tarefas.

No fim, guarda o resultado e corre a verificação:

```bash
git add src tests && git commit -m "feat: tags (vague prompt)"
uv run pytest exercises/checks/test_s02.py
```

Anota quantos testes passam.

## Ronda B — critérios e plan mode

```bash
git switch -c s02-plano s2-start
claude
```

Abre uma sessão nova. Entra em plan mode (`Shift+Tab`), e pede a funcionalidade com os critérios abaixo, colados no pedido. Itera sobre o plano antes de o aprovar: falta algum critério? Ele mexe em ficheiros que não devia?

## Critérios de aceitação

- `todo add TÍTULO --tag NOME` aceita uma ou mais etiquetas (`--tag a --tag b`)
- `todo list` mostra cada etiqueta como `#nome`, depois do título
- `todo list --tag NOME` mostra só as tarefas com essa etiqueta
- As etiquetas não distinguem maiúsculas: `--tag Work` e `--tag work` são a mesma, guardada como `work`
- Uma etiqueta repetida na mesma tarefa fica guardada uma vez
- Um `tasks.json` antigo, de antes das etiquetas, continua a abrir sem erro
- Os testes existentes continuam a passar

## Verificação

```bash
uv run pytest exercises/checks/test_s02.py && uv run pytest
```

## Comparar

```bash
git diff s02-vago s02-plano --stat
```

Qual das rondas passou na verificação? Que critério é que a ronda A falhou, e porquê? O critério do ficheiro antigo é o que costuma cair: porquê?
