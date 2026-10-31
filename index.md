# Comprendre et développer des agents IA spécialisés

Support de la présentation **« Comprendre et développer des agents IA spécialisés »**, donnée par **Doudou Serge**. Le livre rassemble les concepts abordés, le code des démonstrations et leurs résultats, de façon à pouvoir les relire ou les reproduire.

## Le propos

Un modèle de langage sait écrire, mais il ne connaît ni votre boutique, ni l'état de vos stocks, ni les règles de votre service client, et il ne se souvient de rien d'un message à l'autre. Un **agent** est ce qu'on construit autour du modèle pour combler ces manques : de la mémoire, des outils, des documents, des garde-fous. Le livre suit cette construction pas à pas, sur un cas concret, en gardant à chaque étape deux questions en tête : que fait le modèle, et que fait le code qui l'entoure ?

Il suppose une aisance de base en Python (fonctions, listes, dictionnaires, boucles) ; les notions plus avancées, comme `async` ou les classes Pydantic, sont présentées là où elles servent. Aucune connaissance préalable en IA ou en mathématiques n'est requise. Lire le livre n'exige aucune installation ; exécuter les notebooks demande une clé OpenAI (voir {doc}`demarrer`), pour un coût de quelques centimes.

## Le fil rouge : Djassa et Awa

**Djassa** est une boutique en ligne ivoirienne d'articles du quotidien (smartphones, écouteurs, baskets, vêtements, sacs). Les prix sont en FCFA, la livraison couvre Abidjan et quelques villes du pays. **Awa**, son assistante, gagne une compétence à chaque chapitre. Chaque notion est écrite d'abord **en Python pur**, pour que le mécanisme reste visible, puis reprise avec **LangChain ou LangGraph**, pour voir ce que ces bibliothèques automatisent.

```{image} assets/diagrams/nb2_parcours_agent.png
:alt: De l'assistant à l'agent : outils, tool calling, boucle ReAct et validation
:width: 100%
```

| Chapitre | Awa sait... | Notions |
|---|---|---|
| {doc}`Notebook 1 <notebook_1_llm_et_memoire>` | **converser et se souvenir** | tokens, rôles, historique, fenêtre glissante, résumé, profil client |
| {doc}`Notebook 2 <notebook_2_tool_calling_et_react>` | **agir** sur le catalogue | outils, tool calling, boucle ReAct, validation des arguments |
| {doc}`Notebook 3 <notebook_3_rag_et_recherche_web>` | **chercher** dans les documents et sur le web | embeddings, RAG, réponse structurée, recherche web |
| {doc}`Notebook 4 <notebook_4_mcp_multi_agents_securite>` | **travailler en équipe, en sécurité** | MCP, multi-agents, injection de prompt, validation humaine, coûts |

## Trois termes à distinguer

Le vocabulaire de l'IA appliquée est flou ; celui-ci est employé dans un sens précis tout au long du livre.

| Terme | Qui décide de la suite ? | Où le voir |
|---|---|---|
| **LLM seul** | Personne : il prédit du texte, sans mémoire ni accès aux données | chapitre 1 |
| **Workflow** | Le code, selon des étapes ou des règles fixées à l'avance (un routeur à mots-clés, par exemple) | chapitre 3, étape 9 |
| **Agent** | Le LLM lui-même, dans une boucle où il choisit l'outil suivant ou s'arrête | chapitre 2, étape 5 |

## Parcourir le livre

Les chapitres se lisent dans l'ordre : les chapitres 3 et 4 reprennent la boucle d'agent du chapitre 2, elle-même construite sur la mémoire du chapitre 1. Les sections « Avec LangChain » et « Avec LangGraph » sont des variantes : le code en Python pur contient déjà tout le mécanisme, et elles peuvent être sautées lors d'une première lecture. Les sorties affichées proviennent d'une vraie exécution ; les vôtres pourront différer, un LLM n'étant pas déterministe. Chaque chapitre se télécharge en `.ipynb` depuis le bouton en haut de page.

```{tableofcontents}
```
