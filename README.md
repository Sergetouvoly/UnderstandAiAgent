# Formation : comprendre et développer des agents IA spécialisés

Quatre notebooks pour débutants, autour d'un même fil rouge : **MégaShop**, une boutique en ligne d'articles du quotidien (smartphones, écouteurs, baskets, vêtements, sacs), et **Léa**, son assistante IA. Léa gagne une compétence à chaque notebook.

| Notebook | Léa sait... | Notions |
|---|---|---|
| `notebook_1_llm_et_memoire.ipynb` | **converser et se souvenir** | tokens, probabilités, température, rôles, historique, fenêtre glissante, résumé, profil client (Pydantic) |
| `notebook_2_tool_calling_et_react.ipynb` | **agir** sur le catalogue | outils, tool calling, boucle ReAct, validation des arguments (Pydantic) |
| `notebook_3_rag_et_recherche_web.ipynb` | **chercher** dans la documentation et sur le web | embeddings, découpage, index, RAG, réponse structurée, recherche web, routeur ou agent |
| `notebook_4_mcp_multi_agents_securite.ipynb` | **travailler en équipe, en sécurité** | serveur et client MCP, coordinateur et spécialistes, injection de prompt, validation humaine, coûts, évaluation |

Chaque notebook est **autonome** : les données, les outils et les fonctions d'affichage sont dans le notebook, il n'y a aucun fichier à importer. Chaque notion est montrée d'abord **en Python pur**, puis avec **LangChain ou LangGraph** dans une cellule séparée.

## Livre en ligne

Les notebooks sont aussi disponibles sous forme de livre Jupyter Book (navigation, schémas, sorties incluses). Construction et publication : voir [`PUBLIER.md`](PUBLIER.md). Adresse prévue après publication : `https://sergetouvoly.github.io/UnderstandAiAgent/`.

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

## À savoir avant la séance

* **Coût** : une exécution complète des 4 notebooks coûte quelques centimes de dollar avec ces modèles.
* **Les réponses varient** d'une exécution à l'autre : un LLM n'est pas déterministe. La recherche web du notebook 3 est réelle, donc ses résultats changent aussi.
* **Notebook 4, injection de prompt** : la Léa « naïve » utilise volontairement `gpt-4.1-mini`, qui se fait piéger par l'avis truqué. `gpt-5-mini` y résiste plus souvent.
* **Notebook 4, validation humaine** : un champ de saisie apparaît. Réponds `o` (oui) ou `n` (non), puis `Entrée`.
* **Notebook 4, serveur MCP** : la cellule `%%writefile` crée le fichier `serveur_megashop.py` dans le dossier. Il est relancé automatiquement à chaque appel d'outil.

## Dépannage

| Symptôme | Solution |
|---|---|
| `Ajoute OPENAI_API_KEY=...` | Créer le fichier `.env` avec la clé, puis redémarrer le noyau |
| `ModuleNotFoundError: mcp.server.mcpserver` | Le SDK MCP installé est en version 1 : `pip install -U "mcp>=2,<3"` |
| `Called get_config outside of a runnable context` | La pause humaine LangGraph en async demande Python 3.11 ou plus : garder `invoke` (et non `ainvoke`) avec Python 3.10 |
| Une cellule du notebook 4 semble bloquée | Elle attend ta réponse `o` ou `n` dans le champ de saisie |

## Schémas et icônes

Le dossier `assets/` contient les visuels des notebooks :

* `assets/diagrams/` : 30 schémas, chacun en `.excalidraw` (source modifiable sur [excalidraw.com](https://excalidraw.com)), `.svg` et `.png`. Les notebooks affichent les `.png`. Une couleur correspond à un rôle dans tous les schémas : violet pour le LLM, bleu pour ton code ou le serveur, vert pour les outils et les données, orange pour le client ou l'humain, rouge pour les contrôles et les risques.
* `assets/icons/` : 24 icônes PNG utilisées dans les schémas.

Les icônes viennent de [Flaticon](https://www.flaticon.com) (auteur Magnific). Leur licence gratuite exige une attribution : *Icons created by Magnific - Flaticon*. Détails dans `assets/LICENSES.md`.

## Anciennes versions

Le dossier `ancien/` contient la version précédente de la formation (fil rouge « DocBot », support technique). Elle utilisait `utils.py`, `serveur_statut.py`, `docs/` et `data/`, qui sont rangés avec elle.
