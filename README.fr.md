<div align="center">

# show-me-dont-tell-me

### Les assistants *décrivent* votre écran. Celui-ci **le pointe du doigt**.

Un skill Claude qui répond par des captures annotées — repères numérotés, flèches, zoom — au lieu de trois paragraphes qui supposent où se trouve un bouton.

[![Licence MIT](https://img.shields.io/badge/licence-MIT-000000)](LICENSE)
[![Skill Claude](https://img.shields.io/badge/Claude-skill-d97757)](INSTALL.md)
[![Version 2.0.0](https://img.shields.io/badge/version-2.0.0-2563eb)](CHANGELOG.md)

[English](README.md) · **Français** · [العربية](README.ar.md) · [Español](README.es.md) · [简体中文](README.zh.md)

</div>

![Avant / après : un pavé de texte qui décrit un bouton, face à une capture annotée où un repère rouge numéroté le désigne directement](assets/hero.png)

---

## La minute que vous perdez, à chaque fois

Vous demandez où se trouve un réglage. On vous répond ceci :

> *« Rendez-vous dans le panneau de réglages, repérez la section Avancé, et cherchez l'option de téléchargement vers le bas. »*

Trois phrases. Zéro pixel. Il reste à le trouver — et si la réponse vient du souvenir d'une version plus ancienne, l'option ne porte peut-être même plus ce nom.

**show-me-dont-tell-me** répond à la même question par une image de **votre** écran, avec un ① rouge posé sur le bouton exact.

Une étape = une image annotée + une ligne d'action. Le texte ne répète jamais ce que l'image montre déjà.

---

## Installation en 30 secondes

```bash
claude plugin marketplace add MyKhalijAi/show-me-dont-tell-me
claude plugin install show-me-dont-tell-me
```

Puis, simplement :

```
/show-me-dont-tell-me documente le parcours d'inscription de mon app
/show-me-dont-tell-me je suis bloqué sur cet écran
/show-me-dont-tell-me pourquoi ça renvoie une 403
```

Autres plateformes, installation manuelle, mise en place sans CLI → **[INSTALL.md](INSTALL.md)**

---

## Ce que ça change

| Sans | Avec |
|---|---|
| « Rendez-vous dans le panneau de réglages et repérez l'option de téléchargement » | Une image avec un ① rouge sur le bouton exact |
| Des libellés inventés d'après une version plus ancienne | Des libellés lus sur votre écran ou dans vos fichiers i18n |
| Uniquement le chemin heureux | Liste vide, erreur de validation, permission refusée |
| Des captures publiées avec de vraies données clients | Le caviardage est une étape obligatoire, pas une relecture |
| « Ça va prendre un moment » | « Environ 25 min à 100 Mbps » |
| Un pavé de texte à décoder | Une image, un geste, une chose à vérifier |

---

## Ce que les gens en font vraiment

**📘 Livrer le guide utilisateur que vous repoussez depuis des mois.** Pointez-le sur votre dépôt : il lit vos routes, vos templates et vos fichiers i18n, puis produit un tuto qui couvre les écrans que vous auriez oubliés — états d'erreur compris.

**🧑‍💻 Former quelqu'un sans caler une visio.** « Documente notre procédure de déploiement » devient un document numéroté et illustré, avec un signal de vérification après chaque étape.

**🎫 Transformer un ticket de support en réponse définitive.** Le mode dépannage donne cause → correction → vérification, avec l'erreur capturée et la correction capturée. Collez-le dans votre centre d'aide, et ne répondez plus jamais deux fois.

**🧭 Se débloquer dans une interface jamais vue.** Le mode direct recapture votre écran avant chaque instruction : il ne vous guide jamais dans un panneau que vous avez déjà quitté.

**🎬 Storyboarder un screencast avant d'appuyer sur REC.** Plans numérotés, durée par plan, texte dit séparé du texte à l'écran.

---

## Quatre modes, triés pour vous

Le skill détermine ce dont vous avez besoin avant d'agir. Le mode décide de la densité de captures, de la structure et du format de sortie.

| Mode | Déclenché par | Sortie |
|---|---|---|
| **DIRECT** | « aide-moi à », « je suis bloqué » | message court + une image par étape |
| **DOC** | « documente », « tuto de mon app » | document structuré, images intégrées |
| **DÉPANNAGE** | une erreur précise, « ça marche pas » | cause → correction → vérification |
| **SCRIPT** | « vidéo », « screencast », « formation » | plans numérotés, durée par plan |

Il adapte aussi le vocabulaire au public visé — client final, équipe interne, ou vous-même dans six mois.

---

## Cinq règles qu'il ne casse jamais

C'est ce qui permet de coller sa sortie directement dans votre documentation :

1. **Ne jamais décrire une interface de mémoire.** Capture réelle ou code source d'abord. Si rien n'est récupérable, il le dit et demande — il ne devine jamais où est un bouton.
2. **Caviarder avant d'annoter.** Emails, clés d'API, noms de clients, barre d'onglets. Flouté plutôt que masqué, pour que le lecteur voie qu'un champ est là.
3. **Un numéro de repère = un numéro d'étape.** Jamais de décalage.
4. **Chaque étape finit par un signal de vérification** — ce qu'il faut voir pour savoir que c'est réussi.
5. **Cinq repères maximum par image.** Au-delà, il découpe.

Puis il relit l'image qu'il vient de produire et vérifie les cinq points, parce qu'un repère mal placé est pire que pas de repère du tout.

---

## Pointez-le sur votre propre code — c'est là qu'il gagne

Avec accès à vos sources, il lit avant de capturer :

- **Fichiers i18n, templates, constantes** → libellés exacts, au mot près, dans la bonne langue
- **Routes, contrôleurs, validateurs** → les écrans qu'on ne pense jamais à montrer
- **Chemins d'erreur** → liste vide, champ invalide, chargement, permission refusée, quota atteint, échec réseau
- **Prérequis** → le rôle, la donnée ou le réglage nécessaires avant l'étape 1, annoncés d'emblée

> Un tuto qui saute l'erreur de validation est celui qui génère le ticket de support.

---

## Conçu pour de vrais produits, pas pour des captures de démo

- **Le RTL traité sérieusement.** En arabe et en hébreu, les repères passent à **gauche** de la cible, les flèches pointent vers la droite, l'ordre de lecture va de droite à gauche — et il le vérifie sur l'image produite, pas de mémoire.
- **Accessible par construction.** Le sens n'est jamais porté par la couleur seule : c'est le numéro qui le porte. Texte alternatif obligatoire sur chaque image. Le texte doit rester lisible à la moitié de la taille.
- **Répond dans votre langue.** Écrivez en espagnol, vous obtenez de l'espagnol — tandis que les libellés d'interface restent cités exactement tels qu'ils s'affichent.
- **Reste juste dans le temps.** Chaque tuto est daté face à une version de l'app, et le texte n'est jamais modifié sans recapturer l'écran concerné.

---

## L'utilitaire d'annotation

`scripts/annotate.py` — un petit wrapper Pillow qui implémente les conventions. Pas de framework, pas d'étape de build :

```python
from annotate import Annot

(Annot("capture.png")
    .blur(120, 300, 420, 28)        # caviarder d'abord
    .frame(980, 550, 460, 50)
    .point_at(980, 575, 1)          # repère + flèche, conscient du RTL
    .crop_around(1100, 500, 1000, 600)
    .save("etape-01-telecharger.png"))
```

`set_rtl(True)` inverse la position des repères et le sens des flèches pour l'arabe et l'hébreu.

---

## Le cinquième tuto coûte une fraction du premier

Un dossier par produit, pour que le travail se capitalise au lieu de repartir de zéro :

```
<produit>/
  captures/      images brutes
  annotees/      images finales
  glossaire.md   libellés exacts, par langue
  style.md       couleurs, polices, largeur de fenêtre, jeu de démo
  parcours/      un fichier par tuto
```

Avant de repartir de zéro, il vérifie si le parcours existe déjà et n'a besoin que d'une mise à jour.

---

## Pour qui

Toute personne qui doit rendre une interface compréhensible à quelqu'un d'autre :

- **Les développeurs** qui documentent leur app sans y perdre une journée
- **Les équipes support** qui répondent chaque semaine à la même question d'écran
- **Les rédacteurs techniques** qui ont besoin de captures qui restent justes version après version
- **Les formateurs et enseignants** qui construisent des cours illustrés, dans n'importe quelle langue
- **Toute personne bloquée** dans un logiciel, là, maintenant

---

## Contribuer

Le skill tient dans un seul fichier Markdown lisible — [`SKILL.md`](skills/show-me-dont-tell-me/SKILL.md). Pas de build, pas de dépendances, pas de magie. Améliorez une convention là, elle apparaît dans les tutos de tout le monde.

⭐ **Mettez une étoile** si ça vous a épargné une capture — c'est comme ça que les autres le trouvent.

🐛 **Issues et pull requests bienvenues**, dans n'importe laquelle des cinq langues de ce README. Voir [CONTRIBUTING.md](CONTRIBUTING.md).

---

## À propos

Conçu et maintenu par **Dr Maher** chez **MyKhalijAi** — outillage et formation Claude, en arabe, français, anglais et espagnol.

Contact : [mykhalijai@gmail.com](mailto:mykhalijai@gmail.com) · [github.com/MyKhalijAi](https://github.com/MyKhalijAi)

Premier élément d'une suite de skills qui travaillent à partir d'interfaces réelles plutôt que de mémoire.

## Licence

MIT — voir [LICENSE](LICENSE). Usage commercial, fork et redistribution autorisés.
