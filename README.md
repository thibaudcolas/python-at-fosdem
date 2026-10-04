# Template workspace

A reusable starting point for documentation workspace projects: MkDocs site with the Material theme, link checking, linting and formatting, CI, and GitHub Pages deployment.

This is a template extracted from the [Django marketing workspace](https://github.com/marketing-django/marketing-workspace). Placeholder content lives in `docs/` — replace it with real content when using the template.

## What's included

| Concern                 | Tool                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------- |
| Documentation site      | MkDocs + Material for MkDocs, built strictly in CI                                 |
| Task runner             | [just](https://github.com/casey/just) (`justfile`)                                 |
| Python deps             | [uv](https://github.com/astral-sh/uv) (`pyproject.toml`)                           |
| Python lint/format      | [ruff](https://github.com/astral-sh/ruff)                                          |
| Type checking           | [mypy](https://mypy-lang.org/) + [ty](https://docs.astral.sh/ty/)                  |
| Formatting (non-Python) | [prettier](https://prettier.io)                                                    |
| Git hooks               | [prek](https://prek.j178.dev/) (`prek.toml`)                                       |
| Link checking           | [lychee](https://lychee.cli.rs) (`lychee.toml`)                                    |
| CI + deploy             | GitHub Actions: lint, strict docs build, Pages deploy (`.github/workflows/ci.yml`) |

## Site features

Configured in `mkdocs.yml` (each option commented inline):

- Light/dark themes with a custom local color palette (`docs/theme/theme.css`).
- Last-modified dates from git history per page.
- [Tag index](docs/tags.md): page tags and shared folder metadata group related documentation.
- `llms.txt` / `llms-full.txt` generation for LLM consumption.
- [Agent skill publishing](docs/agent-skills.md), with raw skill files and discovery catalogs under `.well-known/`.
- Abbreviation tooltips: `docs/contributing/abbreviations.md` is auto-appended to every page.
- Strict link and nav validation: pages must be in `nav` or opted out; broken anchors fail the build.

## Getting started

Requirements: `uv`, `just`, `prek`, `lychee`, Node.js (`node-version` pins the version).

```sh
just init      # Install dependencies, set up hooks
just docs      # Serve the docs locally on http://localhost:8001
just build-docs  # Strict build (what CI runs)
just lint      # ruff + mypy + ty + prettier checks
just test      # Skill publishing tests
just format    # Auto-format
just check-links  # Link check (requires lychee)
```

## Customization checklist

When starting a new project from this template:

1. Rename the project in `pyproject.toml`, `package.json`, and `README.md`.
2. Set `repo_url`, `site_url`, `repo_name` in `mkdocs.yml` (search for `thibaudcolas/python-at-fosdem` placeholders).
3. Replace `docs/` placeholder content with real content, and update `nav` plus the `llmstxt` `sections` in `mkdocs.yml` to match.
4. Update `site_name`, `site_description`, logos, and favicon in `docs/theme/`.
5. Enable GitHub Pages from GitHub Actions in the repository settings (the workflow deploys on push to `main`).
6. Adapt the starter skill in `.agents/skills/research-workspace/` to your workspace. Every skill in `.agents/skills/` is published with the docs.

## License

MIT — see [LICENSE](LICENSE).
