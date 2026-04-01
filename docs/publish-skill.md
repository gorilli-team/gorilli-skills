# How to Package and Publish a Skill

This document covers the full flow to validate, package, and publish a skill to ClawhHub.

---

## Prerequisites

- Skill folder exists under `skills/<skill-name>/`
- `SKILL.md` is complete with valid frontmatter
- `evals/evals.json` exists with at least one eval entry
- Skill is registered in `catalog.json`

---

## Step 1 — Validate

Checks SKILL.md frontmatter, folder name, and evals structure.

```bash
python scripts/validate_skill.py skills/<skill-name>
```

Must pass with no errors before proceeding.

---

## Step 2 — Package

Creates `dist/<skill-name>.skill` (a ZIP archive) and prints the SHA-256 checksum.

```bash
python scripts/package_skill.py skills/<skill-name>
```

The `evals/` folder is excluded from the package automatically.

---

## Step 3 — Update catalog.json

After packaging, update `catalog.json` with the SHA-256 printed by the package script:

```json
{
  "name": "<skill-name>",
  "version": "<version>",
  "sha256": "<checksum from package script>",
  "published_at": "<ISO date>"
}
```

---

## Step 4 — Commit and Push

```bash
git add skills/<skill-name>/ dist/<skill-name>.skill catalog.json
git commit -m "feat: add <skill-name> skill"
git push
```

---

## Step 5 — Publish to ClawhHub

```bash
clawhub publish /path/to/gorilli-skills/skills/<skill-name> \
  --version <version>
```

Replace `<version>` with the version in `SKILL.md` frontmatter (e.g. `1.1.0`).

---

## Checklist

- [ ] `validate_skill.py` passes
- [ ] `package_skill.py` runs and outputs SHA-256
- [ ] `catalog.json` updated with sha256 and published_at
- [ ] Changes committed and pushed
- [ ] `clawhub publish` run with correct version
