# show-me-dont-tell-me

**Claude décrit le bouton. Ça le fait pointer le bouton.**

![Avant / après](assets/hero.png)

Chaque étape revient sous forme de capture annotée avec un repère numéroté, plus une ligne qui dit quoi faire. Pas de préambule, pas de récapitulatif, pas de « j'espère que ça aide ».

[English](README.md) · [Installation](INSTALL.md) · [Changelog](CHANGELOG.md)

---

## Le problème

Demandez à un assistant de vous guider dans une interface : vous récupérez trois paragraphes qui décrivent un bouton. Il reste à le trouver. Et si l'assistant travaille de mémoire plutôt que sur votre écran réel, le bouton ne porte peut-être plus ce nom.

## Ce que ça change

| Sans | Avec |
|---|---|
| « Rendez-vous dans le panneau de réglages et repérez l'option de téléchargement » | Une image avec un ① rouge sur le bouton exact |
| Des libellés inventés d'après une version plus ancienne | Des libellés lus sur votre écran ou dans vos fichiers i18n |
| Uniquement le chemin heureux | Liste vide, erreur de validation, permission refusée |
| Des captures publiées avec des données clients réelles | Le caviardage est une étape obligatoire |
| « Ça va prendre un moment » | « Environ 25 min à 100 Mbps » |

## Quatre modes

Le skill trie la demande avant d'agir. Le mode décide de la densité de captures, de la structure et du format de sortie.

| Mode | Déclenché par | Sortie |
|---|---|---|
| **DIRECT** | « aide-moi à », « je suis bloqué », session en cours | message court + une image par étape |
| **DOC** | « documente », « tuto de mon app » | document structuré, images intégrées |
| **DEPANNAGE** | une erreur précise, « ça marche pas » | cause → correction → vérification |
| **SCRIPT** | « vidéo », « screencast », « formation » | plans numérotés, durée par plan |

## Règles de fond

1. **Ne jamais décrire une interface de mémoire.** Capture réelle ou code source d'abord.
2. **Caviarder avant d'annoter.** Emails, clés d'API, noms de clients, barre d'onglets.
3. **Un numéro de repère = un numéro d'étape.** Jamais de décalage.
4. **Chaque étape finit par un signal de vérification** — ce qu'il faut voir pour savoir que c'est réussi.
5. **Cinq repères maximum par image.** Au-delà, découper.

## Démarrage

```
/show-me-dont-tell-me documente le parcours d'inscription de mon app
```

```
/show-me-dont-tell-me je suis bloqué sur cet écran
```

```
/show-me-dont-tell-me pourquoi ça renvoie une 403
```

## Ce qu'il lit quand c'est votre application

Pointé sur un dépôt, le skill lit le code avant toute capture :

- **Fichiers i18n, templates, constantes** → libellés exacts, dans la bonne langue
- **Routes, contrôleurs, validateurs** → les écrans qu'on ne pense pas à montrer
- **Chemins d'erreur** → liste vide, champ invalide, chargement, permission refusée, quota atteint, échec réseau

Un tuto qui saute l'erreur de validation est celui qui génère le ticket de support.

## Utilitaire d'annotation

`scripts/annotate.py` est un petit wrapper Pillow qui implémente les conventions :

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

## Bibliothèque réutilisable

Un dossier par produit, pour que le cinquième tuto coûte une fraction du premier :

```
<produit>/
  captures/      images brutes
  annotees/      images finales
  glossaire.md   libellés exacts, par langue
  style.md       couleurs, polices, largeur de fenêtre, jeu de démo
  parcours/      un fichier par tuto
```

## Accessibilité

- Le sens n'est jamais porté par la couleur seule — c'est le numéro qui le porte
- Texte alternatif obligatoire par image, décrivant le contenu et non « capture d'écran »
- Le texte doit rester lisible à la moitié de la taille
- Les interfaces RTL sont traitées explicitement

## À propos

Conçu et maintenu par **Dr Maher** chez **MyKhalijAi** — outillage et formation Claude, en arabe, français, anglais et espagnol.

Contact : [mykhalijai@gmail.com](mailto:mykhalijai@gmail.com) · [github.com/MyKhalijAi](https://github.com/MyKhalijAi)

Premier élément d'une suite de skills qui travaillent à partir d'interfaces réelles. Issues et pull requests bienvenues.

## Licence

MIT — voir [LICENSE](LICENSE).
