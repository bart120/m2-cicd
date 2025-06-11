# TP DevOps & CI/CD – Projet fil rouge sur 4 jours

## 🌟 Objectif global

Mettre en place une chaîne CI/CD complète et professionnelle pour une application web composée d'un frontend, d'un backend et d'une base de données, déployée dans Azure. L'ensemble du projet est géré via GitHub ou GitLab (version gratuite).

---

## 🧱 Stack technique

* **Frontend** : React ou Vue.js
* **Backend** : Python (FastAPI) ou Node.js (Express)
* **DB** : PostgreSQL (Azure Database ou container Docker)
* **Infra as Code** : Terraform
* **CI/CD** : GitHub Actions ou GitLab CI
* **Containers** : Docker
* **Registry** : GHCR ou GitLab Registry ou Azure Registry (privée)
* **Monitoring** : Azure Monitor + Log Analytics
* **Tests** :

  * Frontend : Jest ou Vitest
  * Backend : Pytest ou Jest
  * E2E : Cypress ou Playwright (bonus)
* **Sécurité** : SonarCloud / CodeQL + Snyk / Trivy
* **Secrets** : Azure Key Vault

---

## 🗓️ Planning sur 4 jours

### 🟢 Jour 1 : Initialisation & Infrastructure Azure

#### Objectifs

* Création des projets et du dépôt
* Mise en place de l'infrastructure avec Terraform
* Gestion des secrets avec Key Vault

#### Tâches

* Structuration du projet : mono-repo ou multi-repo
* Ecriture des fichiers `.tf` pour créer :

  * Resource Group
  * App Service Plan ou AKS
  * Azure PostgreSQL flexible server
  * Azure Key Vault
  * Azure Container Registry
* Pipeline de provisionnement Terraform avec `plan` et `apply`
* Stockage distant de l'état (`tfstate`) dans Azure Storage

#### Livrables

* Code Terraform versionné
* Environnement Azure opérationnel
* Secrets stockés dans Key Vault

---

### 🟡 Jour 2 : Intégration continue & Tests unitaires

#### Objectifs

* Mettre en place la CI
* Ajouter des tests unitaires
* Intégrer l'analyse statique et les outils de sécurité

#### Tâches

* Pipeline CI (étapes principales) :

  * Lint frontend et backend
  * Tests unitaires avec rapports de couverture
  * Analyse de code (SonarCloud ou CodeQL)
  * Scan de vulnérabilités (Trivy ou Snyk)
  * Build images Docker frontend et backend
  * Push des images vers le container registry

#### Livrables

* Pipeline CI fonctionnel
* Images Docker disponibles
* Rapport de tests et de couverture

---

### 🔵 Jour 3 : Déploiement continu + Tests E2E

#### Objectifs

* Créer un pipeline CD
* Gérer les déploiements vers staging et production
* Ajouter des tests end-to-end

#### Tâches

* Pipeline CD (étapes) :

  * Déploiement vers `staging` automatique
  * Déploiement vers `production` manuel
  * Tests E2E avec Cypress ou Playwright
  * Récupération de secrets depuis Key Vault
  * Notifications de succès/échec (Slack/email)
  * Ajout de badges (CI, coverage)

#### Livrables

* Application déployée sur Azure (staging et prod)
* Tests E2E automatisés
* CI/CD avec badge et logs

---

### 💜 Jour 4 : Observabilité, résilience et audit

#### Objectifs

* Ajouter la supervision et la surveillance
* Tester la résilience
* Réaliser l'audit final du projet

#### Tâches

* Intégration Azure Monitor + Log Analytics
* Mise en place d'alertes et dashboards
* Tests de panne :

  * Arrêt du backend
  * Crash DB
  * Erreurs HTTP 500
* Mise en place de probes (liveness/readiness)
* Rollback automatique si déploiement KO
* Audit final (performance, sécurité, code)
* Bonus :

  * Canary Release
  * Secrets rotation
  * tfsec/checkov

#### Livrables

* Dashboards actifs
* Rapport final PDF
* CI/CD stable et complet

---

## 📁 Structure du projet

```text
projet-devops-ci-cd/
├── frontend/
│   └── tests/
├── backend/
│   └── tests/
├── infra/
│   ├── terraform/
│   └── tfplan/
├── .github/ ou .gitlab-ci.yml
├── docker/
├── deploy/
│   ├── helm/
│   └── scripts/
├── monitoring/
│   └── dashboards/
├── README.md
├── rapport/
    ├── audit-final.pdf
    ├── screenshots/
    └── schema-pipeline.png
```

---

## 📊 Grille de notation (100 pts)

| Critère                                        | Points |
| ---------------------------------------------- | ------ |
| Code testé (unitaires) + structure propre      | 20     |
| Pipeline CI avec analyse, Docker, qualité      | 20     |
| Pipeline CD avec staging + prod                | 20     |
| Supervision, rollback, probes                  | 15     |
| Documentation et rapport final                 | 10     |
| Bonus avancés DevOps (canary, tfsec, rotation) | 10     |
| Respect consignes et rendu final               | 5      |

---

## 💡 Suggestions de Bonus

* Test de charge (k6, Artillery)
* Cache des dépendances dans CI
* Versioning automatique via tags Git
* Lint de Dockerfile avec `hadolint`
* Analyse IaC avec tfsec / checkov
* Rotation automatique de secrets
* Canary releases via Helm / AKS

---

## Soutenance et rendu

La soutenance aura lieux le mardi 8 juillet 2025.
Le rendu se fera le mardi 8 juillet à 23h59 maxi.
La soutenance se déroulera sur Teams, chaque membre devra mettre sa caméra et son micro afin de participer.
Les horaires de passage sont définis pour chaque groupe (2 personnes max par groupe).
Toute absence à la soutenance entrainera un 0 (ZERO) pour le membre du groupe.

Les rendus doivent figurer sur un seul compte par groupe.
Le rendu s'effectu via un repos GIT. L'adresse du rendu est envoyé par mail.
Le mail de rendu est vincent.leclerc@ynov.com
Les fichiers rendus doivent contenir
  - Les fichiers et documents techniques du projet.
  - Un AUTHORS.TXT listant les membres du groupe (prénom, nom), à raison d'un par ligne.  Il liste ensuite les responsabilités effectives de chacun dans le groupe.
Le sujet du mail doit contenir votre section ainsi que le nom du projet.
Les fichiers rendus peuvent aussi comprendre: 
  - Des documents de recherche créés pour le projet et fournissant plus de détails pour l'enseignant.
Pour tout autre type de fichier, veuillez demander à l'enseignant si son inclusion est appropriée.
La soutenance dure 20 minutes durant lesquelles les membres présentent leur travail. Un échange de questions peut se faire entre le professeur et les membres du groupe.

Les groupes sont les suivants:
- Groupe 1: Damien & Grégoire & Marvin
- Groupe 2: Thomas
- Groupe 3: Grils Power
- Groupe 4: Louis & Quentin & Maxime
- Groupe 5: Sofiane
- Groupe 6: Yohan & Clément & Jérémie

Les horaires de passage des groupes sont les suivants:
 
- 9h30: Groupe 1
- 10h: Groupe 6
- 10h30: Groupe 2
- 11h30: Groupe 3
- 12h: Groupe 4
- 12h30: Groupe 5


Pour ceux dont le groupe n'est pas dans la liste, contactez-moi très rapidement à vincent.leclerc@ynov.com