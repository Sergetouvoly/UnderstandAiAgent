# Comprendre et développer des agents IA spécialisés

Ce livre est le support de la présentation **« Comprendre et développer des agents IA spécialisés »**, donnée le **mercredi 5 octobre** par **Doudou Serge**.

Il rassemble les ressources associées à la présentation : tu y retrouves les concepts abordés, tu consultes les exemples de code avec leurs résultats, et tu peux reproduire toutes les démonstrations chez toi.

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
