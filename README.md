# gorilli-skills

Monorepo for all ClawhHub-published Claude skills authored under the Gorilli brand.

## Quick Start

```bash
# Validate a skill
python scripts/validate_skill.py skills/<skill-name>

# Package a skill into a .skill file
python scripts/package_skill.py skills/<skill-name>

# Bump version (patch | minor | major)
python scripts/bump_version.py skills/<skill-name> minor
```

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

## Skill Folder Layout

```
skills/<skill-name>/
├── SKILL.md          # Required. YAML frontmatter + instructions.
├── evals/            # Test cases (excluded from packaging)
│   └── evals.json
├── scripts/          # Optional. Helpers bundled into the skill.
├── references/       # Optional. Markdown docs loaded on demand.
└── assets/           # Optional. Templates, fonts, icons.
```

## Creating a New Skill

```bash
cp -r skills/_template skills/<new-skill-name>
```

Edit `SKILL.md`, add eval cases, then validate and package. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Versioning

Each skill is versioned independently with semver. Git tags use `<skill-name>@<version>`.

| Change type | Bump |
|---|---|
| Fix wording, typo | PATCH |
| New section, examples, reference files | MINOR |
| Breaking change to output format or triggering | MAJOR |

## License

Apache 2.0 — see [LICENSE](LICENSE).
