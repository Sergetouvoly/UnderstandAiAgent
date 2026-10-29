# Construire et publier le livre

Le livre est un [Jupyter Book](https://jupyterbook.org) 1.x construit à la racine du dépôt à partir des 4 notebooks. Les sorties affichées sont celles **déjà enregistrées** dans les notebooks : la construction n'appelle jamais l'API OpenAI et n'a besoin d'aucune clé.

| Fichier | Rôle |
|---|---|
| `_config.yml` | titre, auteur, dépôt, thème, options de rendu |
| `_toc.yml` | ordre et navigation des chapitres |
| `index.md`, `demarrer.md`, `credits.md` | accueil, installation, crédits |
| `_ext/copier_assets.py` | copie `assets/` (schémas) dans le site |
| `_static/livre.css` | ajustements mobile |
| `requirements-book.txt` | dépendances de construction |
| `.github/workflows/livre.yml` | publication automatique sur GitHub Pages |

## Construire en local

Dans un environnement distinct de celui des notebooks :

```bash
python -m venv .venv-book
.venv-book\Scripts\activate             # macOS / Linux : source .venv-book/bin/activate
pip install -r requirements-book.txt
jupyter-book build . --warningiserror
```

Le site est dans `_build/html`. Pour le consulter :

```bash
python -m http.server 8000 --directory _build/html
```

puis ouvrir <http://localhost:8000>. Après une modification des notebooks, relancer la construction ; en cas de doute, `jupyter-book clean .` repart de zéro.

## Publier sur GitHub Pages

**Automatique (recommandé)**, une seule fois :

1. Dans le dépôt GitHub : *Settings > Pages > Build and deployment > Source* : **GitHub Actions**.
2. Fusionner la branche de travail dans `main` : le workflow `livre.yml` construit et publie.

Le livre est alors à l'adresse `https://sergetouvoly.github.io/UnderstandAiAgent/`. L'avancement se suit dans l'onglet *Actions* ; le workflow peut aussi être lancé à la main (*Run workflow*).

**Manuelle**, sans GitHub Actions :

```bash
pip install ghp-import
ghp-import -n -p -f _build/html
```

puis *Settings > Pages* : source = branche `gh-pages`.

## Mettre à jour le contenu

* **Notebook** : modifier le `.ipynb`, ré-exécuter ses cellules dans Jupyter pour rafraîchir les sorties, enregistrer, puis reconstruire.
* **Schéma** : modifier le `.excalidraw`, ré-exporter le `.png`, le remplacer dans `assets/diagrams/`.
* **Ordre ou titres** : `_toc.yml` pour la navigation, `_config.yml` pour le titre et l'auteur.
