# Comprendre et développer des agents IA spécialisés

Ce livre est le support de la présentation **« Comprendre et développer des agents IA spécialisés »**, donnée par **Doudou Serge**.

Il rassemble les ressources associées à la présentation : tu y retrouves les concepts abordés, tu consultes les exemples de code avec leurs résultats, et tu peux reproduire toutes les démonstrations chez toi.

## Pour qui, et ce que tu sauras faire

**Pour qui ?** Pour toute personne qui débute avec les agents IA et connaît les bases de Python : variables, fonctions, listes, dictionnaires, boucle `for`. Aucune connaissance préalable en IA ni en mathématiques n'est nécessaire. Pour **lire** le livre, rien n'est à installer. Pour **exécuter** les notebooks, il faut une clé OpenAI (voir {doc}`demarrer`) ; les quatre notebooks coûtent quelques centimes.

**À la fin des quatre chapitres, tu sauras :**

* expliquer pourquoi un LLM n'a pas de mémoire, et lui en donner une (historique, résumé, fiche client) ;
* écrire toi-même la boucle d'un agent qui utilise des outils, et valider ce que le LLM te demande d'exécuter ;
* faire répondre un LLM à partir de **tes** documents (RAG) ou du web, et le faire dire « je ne sais pas » quand il le faut ;
* brancher des outils avec MCP, répartir le travail entre plusieurs agents, et protéger l'ensemble contre l'injection de prompt par des défenses empilées.

**Trois mots à ne pas confondre** (ils reviennent dans tout le livre) :

| Mot | Qui décide de la suite ? | Où le voir |
|---|---|---|
| **LLM seul** | Personne : il prédit du texte, sans mémoire ni accès à tes données | chapitre 1 |
| **Workflow** | Ton code, avec des étapes ou des règles fixées à l'avance (par exemple un routeur à mots-clés) | chapitre 3, étape 9 |
| **Agent** | Le LLM lui-même, dans une boucle où il choisit l'outil suivant ou s'arrête | chapitre 2, étape 5 |

Le mot « agent » n'apparaît donc qu'au chapitre 2 : le chapitre 1 pose ce qu'il faut comprendre avant (un LLM ne se souvient de rien).

**Deux façons de parcourir le livre.** En **parcours complet**, tu lis les quatre chapitres dans l'ordre ; prévois environ une heure par chapitre en lecture, davantage si tu exécutes les cellules (estimation indicative). En **première lecture rapide**, tu peux sauter les sections « Avec LangChain » et « Avec LangGraph » : le code en Python pur contient déjà tout le mécanisme, et les frameworks ne font que l'automatiser. Chaque chapitre est autonome, mais les chapitres 3 et 4 reprennent la boucle d'agent du chapitre 2.

## Le fil rouge : MégaShop et Léa

Les quatre chapitres suivent la même histoire. **MégaShop** est une boutique en ligne d'articles du quotidien. **Léa**, son assistante IA, gagne une compétence à chaque chapitre. Chaque notion est montrée d'abord **en Python pur**, puis avec **LangChain ou LangGraph**.

```{image} assets/diagrams/nb2_parcours_agent.png
:alt: De l'assistant à l'agent : outils, tool calling, boucle ReAct et validation
:width: 100%
```

| Chapitre | Léa sait... | Notions |
|---|---|---|
| {doc}`Notebook 1 <notebook_1_llm_et_memoire>` | **converser et se souvenir** | tokens, rôles, historique, fenêtre glissante, résumé, profil client |
| {doc}`Notebook 2 <notebook_2_tool_calling_et_react>` | **agir** sur le catalogue | outils, tool calling, boucle ReAct, validation des arguments |
| {doc}`Notebook 3 <notebook_3_rag_et_recherche_web>` | **chercher** dans les documents et sur le web | embeddings, RAG, réponse structurée, recherche web |
| {doc}`Notebook 4 <notebook_4_mcp_multi_agents_securite>` | **travailler en équipe, en sécurité** | MCP, multi-agents, injection de prompt, validation humaine, coûts |

## Comment utiliser ce livre

* **Pendant la présentation** : suis le chapitre en cours. Le code et ses résultats sont au centre, les explications sont courtes et placées juste avant.
* **Après la présentation** : relis à ton rythme. Les sorties affichées sont celles d'une vraie exécution ; tes propres réponses pourront différer, car un LLM n'est pas déterministe.
* **Pour reproduire** : la page {doc}`demarrer` explique l'installation, la clé OpenAI et le lancement des notebooks. Chaque chapitre peut être téléchargé en `.ipynb` avec le bouton de téléchargement en haut de la page.

```{tableofcontents}
```
