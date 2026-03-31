# Contributing to gorilli-skills

## Adding a New Skill

1. **Copy the template:**

   ```bash
   cp -r skills/_template skills/<your-skill-name>
   ```

2. **Edit `SKILL.md`:**
   - Fill in the YAML frontmatter (name must match the folder name)
   - Write your skill instructions in the body
   - Required frontmatter fields: `name`, `version`, `description`, `author`, `license`

3. **Add eval cases** in `evals/evals.json`:

   ```json
   {
     "evals": [
       {
         "prompt": "Example user prompt",
         "expected_behavior": "What the skill should do"
       }
     ]
   }
   ```

4. **Validate:**

   ```bash
   python scripts/validate_skill.py skills/<your-skill-name>
   ```

5. **Test** by running Claude with your SKILL.md context against each eval prompt.

6. **Package:**

   ```bash
   python scripts/package_skill.py skills/<your-skill-name>
   ```

## Versioning

- Bump version with: `python scripts/bump_version.py skills/<skill-name> patch|minor|major`
- This updates both `SKILL.md` frontmatter and `catalog.json`
- Tag and push: `git tag <skill-name>@<version> && git push origin <skill-name>@<version>`

## Skill Quality Checklist

Before submitting a PR:

- [ ] `validate_skill.py` passes with no errors
- [ ] At least 3 eval cases covering different input types
- [ ] SKILL.md body is under 500 lines
- [ ] Description clearly states when the skill should trigger
- [ ] No hardcoded paths or user-specific values in the skill
