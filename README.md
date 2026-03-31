# gorilli-skills

Claude skills built by [Gorilli](https://gorilli.io), published on [ClawhHub](https://clawhub.ai/luduvigo).

Skills are prompt-based extensions for Claude — drop them into any Claude Code project to give your AI assistant focused, repeatable workflows. Think of them as reusable playbooks: structured instructions that tell Claude exactly how to approach a specific type of task.

---

## Published Skills

### [linear-ticket-creator](https://clawhub.ai/luduvigo/linear-ticket-creator)

Generate well-structured Linear tickets from bugs, features, and improvements. Explores the codebase to auto-populate technical notes, acceptance criteria, and scope boundaries.

**Install:**
```bash
clawhub install linear-ticket-creator
```

**Use:**
> "Create a ticket: users can't reset their password if their email has uppercase letters"

Claude will analyze the input, explore your codebase for relevant files, draft a complete ticket with context, steps to reproduce, acceptance criteria, and technical notes — then ask targeted follow-up questions before finalizing.

---

## Repo Structure

```
gorilli-skills/
├── catalog.json              # Machine-readable registry of all published skills
├── scripts/
│   ├── validate_skill.py     # Validate SKILL.md frontmatter + structure
│   ├── package_skill.py      # Package a skill into dist/<name>.skill
│   └── bump_version.py       # Bump version in frontmatter + catalog.json
├── skills/
│   ├── _template/            # Starting point for new skills
│   └── linear-ticket-creator/
└── dist/                     # Git-ignored; built .skill files
```

Each skill folder:

```
skills/<skill-name>/
├── SKILL.md       # Required. YAML frontmatter + instructions.
├── evals/         # Test cases (excluded from packaging)
│   └── evals.json
├── scripts/       # Optional. Helpers bundled into the skill.
├── references/    # Optional. Markdown docs loaded on demand.
└── assets/        # Optional. Templates, fonts, icons.
```

## Development Workflow

```bash
# Start from the template
cp -r skills/_template skills/<new-skill-name>

# Validate
python3 scripts/validate_skill.py skills/<skill-name>

# Package
python3 scripts/package_skill.py skills/<skill-name>

# Bump version
python3 scripts/bump_version.py skills/<skill-name> minor

# Publish
clawhub publish skills/<skill-name> --version <version> --changelog "..."
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

## Versioning

Each skill is versioned independently with semver. Git tags follow `<skill-name>@<version>`.

| Change | Bump |
|---|---|
| Fix wording, typo | PATCH |
| New section, examples, reference files | MINOR |
| Breaking change to output format or triggering | MAJOR |

## License

Apache 2.0 — see [LICENSE](LICENSE).
