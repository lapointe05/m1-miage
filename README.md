# m1-miage


Welcome students 🐍

![alt text](https://media.tenor.com/1aL_2909P3AAAAAC/greatestshowman-work.gif)

---
## Content
* [docs](./docs)
* [src](./src)
  * [to_do](./src/to_do/)
    * [td_01](./src/to_do/td_01)
    * [td_02](./src/to_do/td_02)
    * [td_03](./src/to_do/td_03)
    * ... etc
  * [bonus_work](./src/bonus_work)
    * [hanoï](./src/bonus_work/hanoï)
* [requirements.txt](./requirements.txt)
* [README.md](./README.md)
* [.gitignore](./.gitignore)

    <!-- * [file22.ext](./bonus_work/hanoï/hanoi_nom_prenom.py) -->

---
## How to Git
### Branching strategy
The root:
- `main` **locked** 🔒 merge changes only through [_pull requests_](https://github.com/lapointe05/m1-miage/compare)

Then one branch per dev
- `prenom_nom` look below for the how to create

### Example
```bash
$> cd mon_dossier_de_dev/
# Cloner le repo (une fois l'acces granted)
$> git clone https://github.com/lapointe05/m1-miage
# Aller dans / Créer un dossier de travail
# Aller dans le dossier
$> cd m1-miage
# Créer une branche a votre nom et prenom
$> git checkout -b prenom_nom
# Lancer jupyter notebook
$> jupyter notebook
#Pour sauvegarder le travail fait
# Stage everything
$> git add .
# Pour commit un change
$> git commit -m 'Un message descriptif mais court de ce qui a été fait sur ce commit'
# Pour pousser les changements sur github, remplacer par le nom de votre branche
$> git push --set-upstream origin prenom_nom
```

> Then back to [Branching strategy](#branching-strategy)

--