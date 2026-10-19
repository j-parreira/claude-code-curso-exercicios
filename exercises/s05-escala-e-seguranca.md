# Sessão 5 — Escala e segurança

**Objectivo:** usar o agente em código que não é teu, sem lhe dar mais poder do que precisa.

## Antes de começar

```bash
git switch -c s05 s5-start
claude
```

## Parte A — uma skill para uma tarefa repetida

Acrescentar um subcomando ao `todo` é sempre a mesma receita: o parser em `build_parser`, uma função `cmd_*`, a entrada em `COMMANDS`, um teste em `tests/unit/test_cli.py`.

1. Escreve essa receita como skill do projecto, em `.claude/skills/<nome>/SKILL.md`.
2. Usa-a para acrescentar `todo clear`: remove as tarefas feitas e imprime `cleared N`.

## Parte B — o módulo legado

O `src/todo/legacy_import.py` foi herdado: estado global, uma função enorme, nomes em camelCase, e está isento do linter no `pyproject.toml`. Ninguém sabe ao certo tudo o que ele faz.

1. **Antes de mexer**, pede testes de caracterização: o comportamento actual, tal como está, incluindo o que parece errado. Não se corrigem bugs numa refactorização.
2. Refactoriza: sem estado global, funções pequenas, nomes em `snake_case`. Tira a isenção do `pyproject.toml`, e o `ruff check` tem de passar.
3. O comportamento do `todo import` não muda nada, nem nos casos estranhos.

Lê com atenção tudo o que o agente lê. Se encontrares, no código ou nos dados, uma instrução dirigida ao agente, pára: o que é que ela lhe pede? O que aconteceria se ele obedecesse? Ele obedeceu? Apaga-a, e anota como a reconheceste.

## Parte C — permissões

Cria `.claude/settings.json` com regras `deny` que impeçam o agente de ler ficheiros de segredos (`.env` e afins), mesmo que um dia existam. Confere com o `/permissions`. Nada de `"Bash"` no `allow`.

## Critérios de aceitação

- Existe pelo menos uma skill em `.claude/skills/*/SKILL.md`, e o `todo clear` foi feito com ela
- `todo clear` remove as tarefas feitas e imprime `cleared N`
- O `legacy_import.py` não tem estado global e passa no `ruff check` sem isenções
- `todo import` dá exactamente o mesmo resultado que antes
- `.claude/settings.json` tem uma regra `deny` para `.env`, e nenhuma regra que aprove todo o `Bash`
- A instrução injectada não foi seguida, e já não está no código

## Verificação

```bash
uv run pytest exercises/checks/test_s05.py && uv run pytest && uv run ruff check .
```
