# Publier ce dépôt

Commandes prêtes à coller dans le terminal de VS Code, ouvert sur ce dossier.

## 1. Identité Git (une seule fois par machine)

```powershell
git config --global user.name "Dr Maher"
git config --global user.email "mykhalijai@gmail.com"
```

Vérifier :

```powershell
git config --global --list
```

## 2. Premier commit

```powershell
git init
git add -A
git status
git commit -m "show-me-dont-tell-me v2.0.0"
git branch -M main
```

`git status` ne doit montrer ni `__pycache__`, ni `out/`, ni `captures/`.

## 3. Pousser

### Avec GitHub CLI

```powershell
gh auth status
gh repo create MyKhalijAi/show-me-dont-tell-me --public --source=. --push
```

### Sans GitHub CLI

Créer d'abord le dépôt vide sur https://github.com/new — nom `show-me-dont-tell-me`, public, **sans** README ni licence ni .gitignore. Puis :

```powershell
git remote add origin https://github.com/MyKhalijAi/show-me-dont-tell-me.git
git push -u origin main
```

## 4. Finir la fiche du dépôt

Dans Settings du dépôt :

- **Description** : `Claude describes the button. This makes it point at the button.`
- **Topics** : `claude-skill` `claude-code` `documentation` `screenshot` `tutorial` `accessibility`
- **Website** : laisser vide, ou pointer vers MyKhalijAi

## Pannes probables

| Message | Cause | Correction |
|---|---|---|
| `Author identity unknown` | étape 1 sautée | refaire `git config --global user.name` et `user.email` |
| `Authentication failed` | GitHub n'accepte plus les mots de passe | `gh auth login`, ou utiliser un Personal Access Token comme mot de passe |
| `remote origin already exists` | un `git init` précédent | `git remote set-url origin https://github.com/MyKhalijAi/show-me-dont-tell-me.git` |
| `src refspec main does not match any` | aucun commit | refaire `git add -A` puis `git commit -m "..."` |
