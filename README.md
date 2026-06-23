# Plateforme SIG — Aptitude des sols (Bizerte + 24 gouvernorats)

## Ce qui a été ajouté / modifié

**1. Navigation par gouvernorat puis par délégation (région)**
- Un premier sélecteur permet de choisir l'un des 24 gouvernorats de Tunisie.
- Un second sélecteur, juste en dessous, affiche automatiquement les délégations
  officielles du gouvernorat choisi (ex. Bizerte → Bizerte Nord, Sejnane, Mateur...).
- Les 24 gouvernorats et leurs 279 délégations officielles sont définis dans
  `governorates_data.py`, à partir des données du Ministère de l'Intérieur / INS.
- Pour l'instant, seul **Bizerte** dispose de données détaillées complètes
  (raster d'aptitude des sols + shapefile de délégations `ADM_BZ32`). Pour les
  23 autres gouvernorats, l'application affiche la carte du gouvernorat
  sélectionné (à partir de `decoupage_gouv.shp`) et la liste de ses délégations,
  avec un bandeau indiquant clairement que les données détaillées n'ont pas
  encore été chargées. Quand vous recevrez les shapefiles/rasters d'un autre
  gouvernorat, il suffira de :
    1. Déposer les fichiers dans `data/` (raster) et `data/shape/` (shapefile),
    2. Passer `"has_data": False` à `"has_data": True` pour ce gouvernorat dans
       `governorates_data.py`,
    3. Ajouter, si nécessaire, une table de correspondance nom-officiel ↔
       nom-shapefile comme `BIZERTE_DELEGATION_TO_SHAPEFILE` (utile si
       l'orthographe du shapefile diffère légèrement, ex. "Sejnane" vs "SEDJNANE").

**2. Sélection d'une délégation précise**
- Quand une délégation de Bizerte est choisie (ex. "Sejnane"), elle est mise en
  surbrillance (contour + remplissage en couleur accent) sur la carte, et la
  carte se recentre automatiquement sur cette délégation.

**3. Refonte de l'interface**
- Nouvelle feuille de style (`theme.py`) : typographie sérieuse (Source Serif 4
  pour les titres, Inter pour le texte courant, IBM Plex Mono pour les
  étiquettes techniques), palette ardoise/bleu pétrole avec un seul accent
  terre cuite, cartes d'information sobres, étiquettes de section avec
  séparateurs. L'objectif est un rendu institutionnel, proche d'un outil SIG
  ministériel, sans effets décoratifs superflus.
- En-tête avec bandeau République Tunisienne / Ministère, sous-titre en arabe.
- Bandeau d'état clair quand les données détaillées ne sont pas disponibles.
- Légende et bloc "Référentiel" (statut du chargement du shapefile, CRS)
  réorganisés en cartes lisibles plutôt qu'en texte brut de la barre latérale.

**4. Corrections techniques**
- Le chemin du dossier `shape` n'est plus codé en dur en `C:\Users\LENOVO\...`
  (ce qui cassait l'application sur toute autre machine) : il est maintenant
  relatif au dossier `data/`.
- `Launch.bat` recrée automatiquement l'environnement virtuel s'il est absent,
  au lieu de pointer vers un chemin Windows fixe.
- Ajout d'un fichier `requirements.txt`.

## Lancer l'application

```bash
pip install -r requirements.txt
streamlit run app.py
```

Ou, sous Windows, double-cliquer sur `Launch.bat`.

**Remarque sur la version de Python** : `requirements.txt` n'impose plus de
version exacte pour `rasterio` et `geopandas`, car leurs dernières versions
exigent Python 3.12+. Avec une version de Python plus ancienne (3.9 à 3.11),
pip installera automatiquement la version compatible la plus récente — aucune
action nécessaire de votre part.


## Structure des fichiers

```
app.py                  → application principale Streamlit
governorates_data.py    → référentiel des 24 gouvernorats et de leurs délégations
theme.py                → feuille de style (CSS) de la plateforme
requirements.txt        → dépendances Python
data/                   → rasters (.tif), images (.jpg), shapefiles
  ├── decoupage_gouv/   → limites des 24 gouvernorats
  └── shape/            → délégations de Bizerte (ADM_BZ32)
```

## Limites connues / points d'attention

- Les délégations de Bizerte sont mises en correspondance avec le shapefile via
  une table explicite (`BIZERTE_DELEGATION_TO_SHAPEFILE`) plutôt qu'une
  comparaison de texte floue, car certains noms diffèrent légèrement entre la
  liste officielle et le shapefile fourni (ex. "Joumine" / "DJOUMINE",
  "Sejnane" / "SEDJNANE"). Si vous ajoutez un shapefile pour un autre
  gouvernorat, vérifiez l'orthographe exacte du champ contenant le nom de la
  délégation et ajustez si besoin.
- Les comptages de délégations du shapefile `decoupage_gouv.shp` (champ
  `DELEGATION`) sont légèrement différents de la liste officielle 2024 pour
  5 gouvernorats (Gabès, Kairouan, Mahdia, Sidi Bouzid, Tataouine), probablement
  en raison de scissions de délégations postérieures à la création du
  shapefile. La liste utilisée dans l'application est la liste officielle la
  plus récente.
