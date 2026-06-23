# -*- coding: utf-8 -*-
"""
Référentiel administratif de la Tunisie : gouvernorats et délégations.

Source : Ministère de l'Intérieur (opendata.interieur.gov.tn) / INS,
recoupé avec le shapefile gouvernorats fourni (decoupage_gouv.shp).

Chaque gouvernorat est identifié par sa clé interne (alignée sur le champ
'Noms_Gouv' du shapefile decoupage_gouv) et contient :
    - "label_fr"   : nom officiel français
    - "label_ar"   : nom officiel arabe
    - "code"       : code gouvernorat (CODE_GOUV du shapefile)
    - "has_data"   : True si des données SIG détaillées (raster + shapefile
                     de délégations) sont disponibles pour ce gouvernorat
    - "delegations": liste ordonnée des délégations officielles
"""

GOVERNORATES = {
    "ariana": {
        "label_fr": "Ariana", "label_ar": "أريانة", "code": 12, "has_data": False,
        "delegations": ["Ariana Ville", "Cité Ettadhamen", "Kalâat El Andalous",
                         "La Soukra", "Mnihla", "Raoued", "Sidi Thabet"],
    },
    "beja": {
        "label_fr": "Béja", "label_ar": "باجة", "code": 21, "has_data": False,
        "delegations": ["Amdoun", "Béja Nord", "Béja Sud", "Goubellat",
                         "Medjez El Bab", "Nefza", "Téboursouk", "Testour", "Thibar"],
    },
    "ben_arous": {
        "label_fr": "Ben Arous", "label_ar": "بن عروس", "code": 13, "has_data": False,
        "delegations": ["Ben Arous", "Bou Mhel El Bassatine", "El Mourouj", "Ezzahra",
                         "Fouchana", "Hammam Chott", "Hammam Lif", "Medina Jedida",
                         "Mégrine", "Mohamedia", "Mornag", "Radès"],
    },
    "bizerte": {
        "label_fr": "Bizerte", "label_ar": "بنزرت", "code": 17, "has_data": True,
        "delegations": ["Bizerte Nord", "Bizerte Sud", "El Alia", "Ghar El Melh",
                         "Ghezala", "Joumine", "Mateur", "Menzel Bourguiba",
                         "Menzel Jemil", "Ras Jebel", "Sejnane", "Tinja",
                         "Utique", "Zarzouna"],
    },
    "gabes": {
        "label_fr": "Gabès", "label_ar": "قابس", "code": 51, "has_data": False,
        "delegations": ["Dkhilet Toujane", "El Hamma", "Gabès Médina", "Gabès Ouest",
                         "Gabès Sud", "Ghannouch", "Habib Thameur Bouatouch", "Mareth",
                         "Matmata", "Menzel El Habib", "Métouia", "Nouvelle Matmata", "Oudhref"],
    },
    "gafsa": {
        "label_fr": "Gafsa", "label_ar": "قفصة", "code": 61, "has_data": False,
        "delegations": ["Belkhir", "El Guettar", "El Ksar", "Gafsa Nord", "Gafsa Sud",
                         "Mdhila", "Métlaoui", "Moularès", "Redeyef", "Sened",
                         "Sidi Aïch", "Sidi Boubaker", "Zannouch"],
    },
    "jendouba": {
        "label_fr": "Jendouba", "label_ar": "جندوبة", "code": 22, "has_data": False,
        "delegations": ["Aïn Draham", "Balta - Bou Aouane", "Bou Salem", "Fernana",
                         "Ghardimaou", "Jendouba", "Jendouba Nord", "Oued Meliz", "Tabarka"],
    },
    "kairouan": {
        "label_fr": "Kairouan", "label_ar": "القيروان", "code": 41, "has_data": False,
        "delegations": ["Aïn Djeloula", "Bou Hajla", "Chebika", "Echrarda", "El Alâa",
                         "Haffouz", "Hajeb el Ayoun", "Kairouan Nord", "Kairouan Sud",
                         "Menzel Mehiri", "Nasrallah", "Oueslatia", "Sbikha"],
    },
    "kasserine": {
        "label_fr": "Kasserine", "label_ar": "القصرين", "code": 42, "has_data": False,
        "delegations": ["El Ayoun", "Ezzouhour", "Fériana", "Foussana", "Haïdra",
                         "Hassi El Ferid", "Jedelienne", "Kasserine Nord", "Kasserine Sud",
                         "Majel Bel Abbès", "Sbeïtla", "Sbiba", "Thala"],
    },
    "kebilli": {
        "label_fr": "Kébili", "label_ar": "قبلي", "code": 63, "has_data": False,
        "delegations": ["Douz Nord", "Douz Sud", "Faouar", "Kébili Nord",
                         "Kébili Sud", "Rjim Maatoug", "Souk Lahad"],
    },
    "lekef": {
        "label_fr": "Le Kef", "label_ar": "الكاف", "code": 23, "has_data": False,
        "delegations": ["Dahmani", "El Ksour", "Jérissa", "Kalâat Khasba", "Kalaat Senan",
                         "Kef Est", "Kef Ouest", "Nebeur", "Sakiet Sidi Youssef",
                         "Sers", "Tajerouine", "Touiref"],
    },
    "mahdia": {
        "label_fr": "Mahdia", "label_ar": "المهدية", "code": 33, "has_data": False,
        "delegations": ["Bou Merdes", "Chebba", "Chorbane", "El Bradâa", "El Jem",
                         "Essouassi", "Hebira", "Ksour Essef", "Mahdia", "Melloulèche",
                         "Ouled Chamekh", "Rejiche", "Sidi Alouane"],
    },
    "manouba": {
        "label_fr": "Manouba", "label_ar": "منوبة", "code": 14, "has_data": False,
        "delegations": ["Borj El Amri", "Djedeida", "Douar Hicher", "El Batan",
                         "Manouba", "Mornaguia", "Oued Ellil", "Tebourba"],
    },
    "medenine": {
        "label_fr": "Médenine", "label_ar": "مدنين", "code": 52, "has_data": False,
        "delegations": ["Ben Gardane", "Beni Khedache", "Djerba Ajim", "Djerba Houmt Souk",
                         "Djerba Midoun", "Médenine Nord", "Médenine Sud",
                         "Sidi Makhlouf", "Zarzis"],
    },
    "monastir": {
        "label_fr": "Monastir", "label_ar": "المنستير", "code": 32, "has_data": False,
        "delegations": ["Bekalta", "Bembla", "Beni Hassen", "Jemmal", "Ksar Hellal",
                         "Ksibet El Médiouni", "Moknine", "Monastir", "Ouerdanine",
                         "Sahline", "Sayada - Lamta - Bouhjar", "Téboulba", "Zéramdine"],
    },
    "nabeul": {
        "label_fr": "Nabeul", "label_ar": "نابل", "code": 15, "has_data": False,
        "delegations": ["Béni Khalled", "Béni Khiar", "Bou Argoub", "Dar Châabane El Fehri",
                         "El Haouaria", "El Mida", "Grombalia", "Hammamet", "Hammam Ghezèze",
                         "Kélibia", "Korba", "Menzel Bouzelfa", "Menzel Temime",
                         "Nabeul", "Soliman", "Takelsa"],
    },
    "sfax": {
        "label_fr": "Sfax", "label_ar": "صفاقس", "code": 34, "has_data": False,
        "delegations": ["Agareb", "Bir Ali Ben Khalifa", "El Amra", "El Hencha", "Graïba",
                         "Jebiniana", "Kerkennah", "Mahrès", "Menzel Chaker",
                         "Sakiet Eddaïer", "Sakiet Ezzit", "Sfax Ouest", "Sfax Sud",
                         "Sfax Ville", "Skhira", "Thyna"],
    },
    "sidibouzid": {
        "label_fr": "Sidi Bouzid", "label_ar": "سيدي بوزيد", "code": 43, "has_data": False,
        "delegations": ["Bir El Hafey", "Cebbala Ouled Asker", "El Hichria", "Essaïda",
                         "Jilma", "Meknassy", "Menzel Bouzaiane", "Mezzouna",
                         "Ouled Haffouz", "Regueb", "Sidi Ali Ben Aoun",
                         "Sidi Bouzid Est", "Sidi Bouzid Ouest", "Souk Jedid"],
    },
    "Siliana": {
        "label_fr": "Siliana", "label_ar": "سليانة", "code": 24, "has_data": False,
        "delegations": ["Bargou", "Bou Arada", "El Aroussa", "El Krib", "Gaâfour",
                         "Kesra", "Makthar", "Rouhia", "Sidi Bou Rouis",
                         "Siliana Nord", "Siliana Sud"],
    },
    "sousse": {
        "label_fr": "Sousse", "label_ar": "سوسة", "code": 31, "has_data": False,
        "delegations": ["Akouda", "Bouficha", "Enfida", "Hammam Sousse", "Hergla",
                         "Kalâa Kebira", "Kalâa Seghira", "Kondar", "M'saken",
                         "Sidi Bou Ali", "Sidi El Hani", "Sousse Jawhara",
                         "Sousse Médina", "Sousse Riadh", "Sousse Sidi Abdelhamid",
                         "Zaouiet - Ksibet Thrayet"],
    },
    "tataouine": {
        "label_fr": "Tataouine", "label_ar": "تطاوين", "code": 53, "has_data": False,
        "delegations": ["Beni Mehira", "Bir Lahmar", "Dehiba", "Ghomrassen",
                         "Remada", "Smâr", "Tataouine Nord", "Tataouine Sud"],
    },
    "tozeur": {
        "label_fr": "Tozeur", "label_ar": "توزر", "code": 62, "has_data": False,
        "delegations": ["Degache", "El Hamma du Jérid", "Hazoua", "Nefta",
                         "Tamerza", "Tozeur"],
    },
    "tunis": {
        "label_fr": "Tunis", "label_ar": "تونس", "code": 11, "has_data": False,
        "delegations": ["Bab El Bhar", "Bab Souika", "Carthage", "Cité El Khadra",
                         "Djebel Jelloud", "El Hraïria", "El Kabaria", "El Menzah",
                         "El Omrane", "El Omrane Supérieur", "El Ouardia", "Ettahrir",
                         "Ezzouhour", "La Goulette", "La Marsa", "Le Bardo", "Le Kram",
                         "Medina", "Séjoumi", "Sidi El Béchir", "Sidi Hassine"],
    },
    "zaghouan": {
        "label_fr": "Zaghouan", "label_ar": "زغوان", "code": 16, "has_data": False,
        "delegations": ["Bir Mcherga", "El Fahs", "Nadhour", "Saouaf", "Zaghouan", "Zriba"],
    },
}


def get_governorate_keys_sorted():
    """Retourne les clés des gouvernorats triées par nom français."""
    return sorted(GOVERNORATES.keys(), key=lambda k: GOVERNORATES[k]["label_fr"])


def get_label(gov_key):
    return GOVERNORATES[gov_key]["label_fr"]


def get_delegations(gov_key):
    return GOVERNORATES[gov_key]["delegations"]


def has_detailed_data(gov_key):
    return GOVERNORATES[gov_key]["has_data"]


# ----------------------------------------------------------------------
# Correspondance entre les noms officiels des délégations (utilisés dans
# l'interface) et l'orthographe trouvée dans le shapefile ADM_BZ32 (champ
# ADM_DEL), qui suit une transcription française légèrement différente.
# Utilisé uniquement pour le gouvernorat de Bizerte, le seul pour lequel
# le shapefile de délégations est disponible.
# ----------------------------------------------------------------------
BIZERTE_DELEGATION_TO_SHAPEFILE = {
    "Bizerte Nord": "BIZERTE NORD",
    "Bizerte Sud": "BIZERTE SUD",
    "El Alia": "EL ALIA",
    "Ghar El Melh": "GHAR EL MELEH",
    "Ghezala": "GHEZALA",
    "Joumine": "DJOUMINE",
    "Mateur": "MATEUR",
    "Menzel Bourguiba": "MENZEL BOURGUIBA",
    "Menzel Jemil": "MENZEL DJEMIL",
    "Ras Jebel": "RAS EL DJEBEL",
    "Sejnane": "SEDJNANE",
    "Tinja": "TINJA",
    "Utique": "UTIQUE",
    "Zarzouna": "ZARZOUNA",
}


def get_shapefile_name(delegation_label):
    """Renvoie l'orthographe utilisée dans le shapefile pour une délégation
    de Bizerte donnée (nom officiel -> nom du shapefile)."""
    return BIZERTE_DELEGATION_TO_SHAPEFILE.get(delegation_label, delegation_label.upper())
