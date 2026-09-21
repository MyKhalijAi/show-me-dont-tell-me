---
name: "show-me-dont-tell-me"
description: "Produire un tuto ou une assistance pas-à-pas avec captures annotées (repères numérotés, flèches, zoom) plutôt que des explications verbeuses. Pour documenter une app, guider un réglage, dépanner une interface, ou assister en direct sur l'écran de l'utilisateur."
---

# show-me-dont-tell-me

Chaque étape = **une image annotée + une ligne d'action**. Le texte ne décrit jamais ce que l'image montre déjà.

Réponds dans la langue de l'utilisateur.

## Règle absolue

Ne décris jamais une interface de mémoire. Capture réelle ou code source d'abord, rédaction ensuite. Une interface change de version en version ; une consigne inventée coûte plus de temps qu'elle n'en fait gagner.

Si rien n'est obtenable : le dire et demander une capture. Ne jamais deviner la position d'un bouton.

---

## Étape 0 — Trier la demande

Quatre modes. Le mode décide de tout ce qui suit. Si la demande est ambiguë, poser **une** question pour trancher.

| Mode | Déclencheur | Captures | Sortie |
|---|---|---|---|
| **DIRECT** | « aide-moi à », « je suis bloqué », session en cours | 1 par message, recapture avant chaque consigne | message court + image |
| **DOC** | « documente », « tuto de mon app » | 1 par étape + états limites | document structuré, images intégrées |
| **DEPANNAGE** | une erreur précise, « ça marche pas » | capture de l'erreur + de la correction | cause → correction → vérification |
| **SCRIPT** | « vidéo », « screencast », « formation » | 1 par plan | script minuté, plans numérotés |

### Public

Identifier pour qui — ça change le vocabulaire et la quantité de « pourquoi » :

- **Client final** — zéro jargon technique, jamais de chemin de fichier serveur, ton rassurant sur les erreurs.
- **Équipe interne** — jargon maison autorisé, raccourcis clavier, cas limites.
- **Soi-même plus tard** — noter les décisions et les pourquoi, pas seulement les gestes.

---

## Étape 1 — Source de vérité

### Quand c'est l'application de l'utilisateur

Lire le code **avant** de capturer. C'est le plus gros gain de justesse du skill.

1. **Libellés exacts** — fichiers i18n, templates, constantes. Copier les chaînes telles quelles, pas de traduction approximative.
2. **Parcours complet** — routes, contrôleurs, validations : donne les écrans que l'utilisateur ne pensera pas à montrer.
3. **États à documenter**, pas seulement le chemin heureux : liste vide, champ invalide, chargement, permission refusée, quota atteint, échec réseau. Un tuto qui ignore l'erreur de validation est celui qui génère le ticket de support.
4. **Prérequis** — rôle, données ou réglage nécessaires avant l'étape 1. Les énoncer d'abord.

### Obtenir un fichier image

Il faut un **fichier sur disque** pour annoter. Une image qui arrive seulement dans le contexte ne peut pas être modifiée.

Par ordre de préférence :

1. **Capture fournie par l'utilisateur** — déjà un fichier.
2. **Navigateur** — `mcp__claude-in-chrome__computer` action `screenshot`, `save_to_disk: true`. Le résultat donne le chemin. Exige l'autorisation de l'extension sur le site ; `localhost` et `127.0.0.1` doivent être autorisés explicitement.
3. **Machine de l'utilisateur** — `device_bash` pour capturer, `device_stage_files` pour rapatrier. Nécessite un dossier connecté.
4. **Computer use** — `computer_screenshot` sert à **voir et se repérer**, mais rend une image en contexte, pas un fichier : non annotable. L'utiliser pour lire l'état réel, puis reconstruire (point 5).
5. **Reconstruction fidèle** — redessiner le panneau observé en PIL/SVG. Toujours écrire « schéma reconstruit » sur l'image. Ne jamais faire passer une reconstruction pour une capture.

### Pièges de capture

- **Plusieurs écrans** : la capture vise un seul moniteur. Repérer le bon avec la liste des moniteurs, puis basculer dessus.
- **Fenêtres masquées** : terminaux, invites de commandes et fenêtres système sortent souvent masqués des captures. Si une console est nécessaire, demander à l'utilisateur de coller le texte.
- **Navigateur en lecture seule** : sous computer use, un navigateur est accordé en tier « read » — visible, non cliquable. Pour cliquer, passer par l'extension navigateur.
- **Largeur variable** : demander une largeur de fenêtre stable (1440 px conseillé) pour que toutes les captures d'un même tuto s'alignent.

---

## Étape 2 — Caviarder avant tout

**Obligatoire, avant annotation.** Une capture d'interface réelle contient presque toujours des données à masquer.

À flouter systématiquement :

1. Adresses email, numéros de téléphone, noms de personnes réelles
2. Clés d'API, jetons, identifiants de session, URL signées
3. Noms de clients, raisons sociales, montants, numéros de facture
4. Barre d'onglets et favoris du navigateur — ils exposent le reste de l'activité
5. Notifications, aperçus de messagerie, contenu d'autres fenêtres

Flouter plutôt que masquer par un rectangle plein : garder la forme pour que le lecteur comprenne qu'il y a un champ là.

```python
from PIL import ImageFilter
zone = img.crop((x, y, x+w, y+h)).filter(ImageFilter.GaussianBlur(12))
img.paste(zone, (x, y))
```

Préférer un **jeu de données de démonstration** au caviardage quand c'est possible : plus propre, et réutilisable d'un tuto à l'autre.

En cas de doute sur une zone : demander avant de publier.

---

## Étape 3 — Annoter

Recadrer sur la zone utile. Une capture 4K entière rend les repères illisibles.

Conventions :

- **Repère numéroté** = pastille pleine, chiffre blanc, contour blanc. Le numéro correspond au numéro de l'étape écrite. Jamais de décalage entre les deux.
- **Flèche** vers la cible, jamais dessus : la cible reste lisible.
- **Cadre** autour de la zone cible, 4 à 5 px.
- **Zoom** sur toute cible de moins de 40 px : vignette agrandie à côté.
- **Code couleur** : rouge = à faire maintenant, vert = après, orange = avertissement. Ne jamais faire porter le sens par la couleur seule — le numéro porte le sens.
- Maximum **5 repères par image**. Au-delà, découper en plusieurs images.
- **Avant / après** côte à côte quand le résultat est visuel.

### Langues RTL (arabe, hébreu)

L'interface est inversée : les repères se placent à **gauche** de la cible, les flèches pointent vers la droite, l'ordre de lecture des repères va de droite à gauche. Vérifier sur l'image produite, pas de tête.

### Squelette réutilisable

```python
from PIL import Image, ImageDraw, ImageFont
import math
FD = "/usr/share/fonts/truetype/dejavu/"
def F(n, b=False):
    return ImageFont.truetype(FD + ("DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), n)

img = Image.open("capture.png").convert("RGB")
d = ImageDraw.Draw(img)

def cadre(x, y, w, h, c="#ff3b30"):
    d.rounded_rectangle([x, y, x+w, y+h], radius=8, outline=c, width=5)

def fleche(x1, y1, x2, y2, c="#ff3b30", w=5):
    d.line([x1, y1, x2, y2], fill=c, width=w)
    a = math.atan2(y2-y1, x2-x1); L, s = 20, 0.5
    d.polygon([(x2, y2),
               (x2-L*math.cos(a-s), y2-L*math.sin(a-s)),
               (x2-L*math.cos(a+s), y2-L*math.sin(a+s))], fill=c)

def repere(cx, cy, n, c="#ff3b30", r=26):
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=c, outline="#ffffff", width=4)
    t = str(n); bb = d.textbbox((0, 0), t, font=F(30, True))
    d.text((cx-(bb[2]-bb[0])/2, cy-(bb[3]-bb[1])/2-5), t, font=F(30, True), fill="#ffffff")

img.save("etape-1.png")
```

Nommage : `<produit>-<parcours>-<NN>-<slug>.png`, numéro sur deux chiffres pour que le tri alphabétique suive l'ordre des étapes.

---

## Étape 4 — Rédiger

Une étape = un geste. Format :

```
1. [Geste] sur [libellé exact tel qu'il est écrit à l'écran]
   → [ce qui doit apparaître ensuite]
```

Règles :

- La première ligne de la réponse est le geste à faire maintenant, pas le contexte.
- Citer les libellés **exactement** comme ils s'affichent, dans la langue de l'interface, même si le tuto est rédigé dans une autre langue.
- Donner un **signal de vérification** après chaque étape : ce que l'utilisateur doit voir pour savoir que c'est réussi.
- Estimations de temps en unités concrètes (« 25 min à 100 Mbps »), jamais « un moment ».
- Chemins de fichiers et commandes en bloc de code, copiables tels quels.
- Pas de préambule, pas de récapitulatif, pas de formule de politesse finale.
- Supprimer toute phrase qui n'ajoute pas d'information à l'image.
- **Texte alternatif** par image : ce que montre l'image, pas « capture d'écran ».

### Quand ça casse

Pour chaque étape à risque, prévoir la panne probable :

```
Si [message d'erreur exact] : [cause en une phrase]. Correction : [geste].
```

Cause et correction, ton neutre. Pas de « oups », pas de dramatisation.

---

## Étape 5 — Contrôle final

Avant d'envoyer, **relire l'image produite** et vérifier :

1. Chaque repère tombe sur sa cible, pas à côté
2. Les numéros de l'image correspondent aux numéros du texte
3. Aucune donnée sensible visible (relire la liste de l'étape 2)
4. Le texte reste lisible une fois l'image réduite de moitié
5. Rien dans le texte ne décrit ce que l'image montre déjà

Un repère mal placé est pire que pas de repère.

---

## Étape 6 — Livrer

| Mode | Format |
|---|---|
| DIRECT | image via `SendUserFile` `display: "render"`, légende d'une ligne + étapes courtes dans le message |
| DOC | document structuré, images intégrées dans l'ordre, sommaire au-delà de 6 étapes |
| DEPANNAGE | message court : cause, correction, vérification |
| SCRIPT | plans numérotés, durée par plan, texte dit séparé du texte à l'écran |

Finir par **une seule** action concrète à faire dans les deux minutes.

---

## Bibliothèque réutilisable

Un dossier par produit. Le cinquième tuto doit coûter une fraction du premier.

```
<produit>/
  captures/        images brutes, nommées
  annotees/        images finales
  glossaire.md     libellés exacts par langue
  style.md         couleurs, polices, largeur de fenêtre, jeu de démo
  parcours/        un fichier par tuto
```

Avant de repartir de zéro : vérifier si le parcours existe déjà et s'il suffit de le mettre à jour.

## Maintenance

Dater chaque tuto et noter la version de l'app documentée.

Recapturer quand : la version change, un libellé bouge dans l'i18n, un utilisateur signale que l'écran ne correspond plus.

Ne jamais retoucher le texte d'un tuto sans recapturer l'écran concerné — c'est ainsi qu'un tuto devient faux tout en ayant l'air à jour.

---

## Assistance en direct (mode DIRECT)

1. **Recapturer avant chaque consigne** — l'utilisateur a peut-être déjà avancé ou changé d'onglet.
2. **Rappeler où il en est** (« étape 2 sur 4 ») : il ne garde pas l'état en tête entre deux messages.
3. **Une seule consigne à la fois.**
4. **Confirmer ce qui marche déjà** avant de passer à la suite.
5. **Bloqué trois échanges de suite sur le même point** : arrêter de proposer des variantes. Nommer l'hypothèse qui pourrait être fausse, demander une capture de l'état réel.

Si une action est destructrice (suppression, écrasement, migration, paiement) : confirmer avant, même si ça coûte un aller-retour.