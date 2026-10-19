# Sessão 1 — Modelo mental e primeira sessão

**Objectivo:** trabalhar com o agente num repositório que não conheces, sem medo de estragar: perguntar, alterar e desfazer.

## Antes de começar

```bash
git switch -c s01 s1-start
uv sync
uv run pytest
claude
```

## Tarefa

1. **Explorar só a perguntar.** Não peças alterações. Pergunta, por exemplo:
   - "O que faz este projecto e como está organizado?"
   - "Onde ficam guardadas as tarefas, e o que acontece se o ficheiro não existir?"
   - "Como é que `todo list` decide que tarefas mostra?"

   Confere pelo menos uma resposta no código, com `@src/todo/...`. O agente acertou?

2. **Uma alteração pequena.** Pede que `todo list` mostre a prioridade antes do título, em vez de depois. Lê o diff que ele propõe antes de aprovar. Experimenta com `!uv run todo add "teste"` e `!uv run todo list`.

3. **Desfazer.** Usa o `/rewind` para voltar ao estado anterior à alteração. Depois corre `!git status`.

4. **O que o `/rewind` não desfaz.** Se o `git status` mostra um `tasks.json` novo, foi criado por um comando de shell (`todo add`), e o `/rewind` não desfaz comandos de shell. Apaga-o tu.

5. **Travar a meio.** Pede uma alteração maior ("acrescenta um comando `edit`") e carrega em `Esc` antes de ele acabar. Desfaz o que tiver ficado feito.

## Critérios de aceitação

- Sabes explicar, por palavras tuas, o que fazem `storage.py` e `query.py`
- No fim, o repositório está como na tag: nenhuma alteração, nenhum ficheiro novo
- Os testes passam

## Verificação

```bash
uv run pytest && git status --porcelain
```

Passa quando o `pytest` termina sem falhas e o `git status --porcelain` não imprime nada.
