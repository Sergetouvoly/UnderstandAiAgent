# Démarrer

Cette page décrit ce qu'il faut pour **exécuter** les notebooks chez toi. Pour simplement lire le livre, rien n'est à installer.

## Récupérer les notebooks

Les notebooks et leurs schémas sont dans le dépôt du projet : [github.com/Sergetouvoly/UnderstandAiAgent](https://github.com/Sergetouvoly/UnderstandAiAgent).

## Prérequis

* **Python de base** : variables, fonctions, listes, dictionnaires, boucle `for`. Les notions plus avancées (`async`, classes Pydantic) sont expliquées là où elles apparaissent.
* **Un compte OpenAI avec de quoi payer l'API** : une clé gratuite sans crédit ne suffit pas. Une exécution complète des quatre premiers notebooks coûte quelques centimes. Le notebook 5 est un guide à suivre dans n8n : il ne contient aucun code à exécuter.
* **Facultatif** : [Ollama](https://ollama.com) pour comparer avec un petit modèle local au chapitre 2.
* **Aucun prérequis** en IA ni en mathématiques.

## Installation

1. **Python 3.10 ou plus récent**, puis dans un environnement virtuel :

   ```bash
   python -m venv .venv
   .venv\Scripts\activate             # macOS / Linux : source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Une clé OpenAI** dans un fichier `.env` à la racine du dossier :

   ```
   OPENAI_API_KEY=sk-...
   ```

3. **Lancer Jupyter** depuis ce dossier (`jupyter lab`), ou ouvrir les notebooks dans VS Code.

## Modèles utilisés

| Modèle | Où | Pourquoi |
|---|---|---|
| `gpt-4.1-mini` | Notebook 1, coordinateur du notebook 4, recherche web du notebook 3 | Rapide, accepte la température et les probabilités des tokens |
| `gpt-5-mini` | Agents des notebooks 2, 3 et 4 | Raisonne avant d'agir : plus fiable pour choisir les outils |
| `text-embedding-3-small` | Notebook 3 | Embeddings pour le RAG |

Le notebook 2 peut aussi tourner avec **Ollama** en local (`FOURNISSEUR = "ollama"`, modèle `qwen2.5:7b`), pour comparer avec un petit modèle.

## À savoir avant de lancer

* **Coût** : une exécution complète des 4 notebooks coûte quelques centimes de dollar avec ces modèles.
* **Les réponses varient** d'une exécution à l'autre. La recherche web du notebook 3 est réelle, donc ses résultats changent aussi.
* **Notebook 4, injection de prompt** : l'Awa « naïve » utilise volontairement `gpt-4.1-mini`, qui se fait piéger par l'avis truqué. `gpt-5-mini` y résiste plus souvent.
* **Notebook 4, validation humaine** : un champ de saisie apparaît. Réponds `o` (oui) ou `n` (non), puis `Entrée`.
* **Notebook 4, serveur MCP** : la cellule `%%writefile` crée le fichier `serveur_djassa.py` dans le dossier. Il est relancé automatiquement à chaque appel d'outil.

## Dépannage

| Symptôme | Solution |
|---|---|
| `Ajoute OPENAI_API_KEY=...` | Créer le fichier `.env` avec la clé, puis redémarrer le noyau |
| `ModuleNotFoundError: mcp.server.mcpserver` | Le SDK MCP installé est en version 1 : `pip install -U "mcp>=2,<3"` |
| `Called get_config outside of a runnable context` | La pause humaine LangGraph en async demande Python 3.11 ou plus : garder `invoke` (et non `ainvoke`) avec Python 3.10 |
| Une cellule du notebook 4 semble bloquée | Elle attend ta réponse `o` ou `n` dans le champ de saisie |
