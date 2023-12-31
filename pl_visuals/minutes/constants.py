LEAGUES = {
    "epl": {
        "lge_code": "c9",
        "lge_name": "Premier League",
        "fotmob_id": "47",
        "start_year": 1992,
    },
    "laliga": {
        "lge_code": "c12",
        "lge_name": "La Liga",
        "fotmob_id": "87",
        "start_year": 1988,
    },
    "ligue1": {
        "lge_code": "c13",
        "lge_name": "Ligue 1",
        "fotmob_id": "53",
        "start_year": 1995,
    },
    "bundesliga": {
        "lge_code": "c20",
        "lge_name": "Bundesliga",
        "fotmob_id": "54",
        "start_year": 1988,
    },
    "seriea": {
        "lge_code": "c11",
        "lge_name": "Serie A",
        "fotmob_id": "55",
        "start_year": 1988,
    },
    "ucl": {"lge_code": "c8", "lge_name": "Champions League", "fotmob_id": "42"},
    # "uel": {"lge_code": "c19", "lge_name": "Europe League", "fotmob_id": "73"},
}

CATEGORIES = [
    "gls",
    "ast",
    "g+a",
    "gls90",
    "ast90",
    "g+a90",
    "minutes",
    "cards",
    "nationalities",
    "progression",
]

COLUMNS = [
    "Player",
    "Nation",
    "Pos",
    "Age",
    "MP",
    "Starts",
    "Min",
    "90s",
    "Gls",
    "Ast",
    "G+A",
    "G-PK",
    "PK",
    "PKatt",
    "CrdY",
    "CrdR",
    "xG",
    "npxG",
    "xAG",
    "npxG+xAG",
    "PrgC",
    "PrgP",
    "PrgR",
    "Gls90",
    "Ast90",
    "G+A90",
    "G-PK90",
    "G+A-PK90",
    "xG90",
    "xAG90",
    "xG+xAG90",
    "npxG90",
    "npxG+xAG90",
]

NINETY_COLUMNS = [
    "Gls90",
    "Ast90",
    "G+A90",
    "G-PK90",
    "G+A-PK90",
    "xG90",
    "xAG90",
    "xG+xAG90",
    "npxG90",
    "npxG+xAG90",
    "PrgC90",
    "PrgP90",
]

AGGREGATOR = {
    "Pos": "first",
    "MP": "sum",
    "Starts": "sum",
    "Min": "sum",
    "90s": "sum",
    "Gls": "sum",
    "Ast": "sum",
    "G+A": "sum",
    "G-PK": "sum",
    "PK": "sum",
    "PKatt": "sum",
    "CrdY": "sum",
    "CrdR": "sum",
    "xG": "sum",
    "npxG": "sum",
    "xAG": "sum",
    "npxG+xAG": "sum",
    "PrgC": "sum",
    "PrgP": "sum",
    "PrgR": "sum",
    "club_name": "first",
    "club_id": "first",
    "lge": "first",
}

TYPES_DICT = {
    "MP": "int",
    "Starts": "int",
    "Min": "int",
    "90s": "float",
    "Gls": "int",
    "Ast": "int",
    "G+A": "int",
    "G-PK": "int",
    "PK": "int",
    "PKatt": "int",
    "CrdY": "int",
    "CrdR": "int",
    "xG": "float",
    "npxG": "float",
    "xAG": "float",
    "npxG+xAG": "float",
    "PrgC": "int",
    "PrgP": "int",
    "PrgR": "int",
}


NATION_COLOURS = {
    "Argentina": "#43A1D5",
    "Nigeria": "#008751",
    "Denmark": "#C60C30",
    "Germany": "#000000",
    "Belgium": "#E30613",
    "France": "#21304D",
    "Portugal": "#E42518",
    "Norway": "#C8102E",
    "Brazil": "#FFDC02",
    "England": "#000040",
    "Spain": "#8B0D11",
    "Poland": "#DC143C",
    "Italy": "#0064AA",
    "Chile": "#0039A6",
    "Senegal": "#11A335",
    "Morocco": "#17A376",
    "Algeria": "#007229",
    "Canada": "#C5281C",
    "Suriname": "#377E3F",
    "Japan": "#000555",
    "Austria": "#ED2939",
    "Netherlands": "#F36C21",
    "Israel": "#0038B8",
    "Serbia": "#B72E3E",
    "Croatia": "#ED1C24",
    "Uruguay": "#55B5E5",
    "Republic of Ireland": "#169B62",
    "Wales": "#AE2630",
    "Scotland": "#004B84",
    "Colombia": "#FCD116",
    "Kosovo": "#244AA5",
    "Czech Republic": "#ED1B2C",
    "Switzerland": "#D52B1E",
    "Albania": "#E41E20",
    "Côte d'Ivoire": "#FF8200",
    "Mali": "#FCD116",
    "Cameroon": "#479A50",
    "Ghana": "#D40023",
    "Bosnia": "#002F6C",
    "Ukraine": "#FFD700",
    "Cameroon": "#479A50",
    "Turkey": "#E30A17",
    "Switzerland": "#FF0000",
    "Egypt": "#C8102E",
    "United States": "#002868",
    "Angola": "#C8102E",
    "Georgia": "#BA0C2F",
}


COUNTRIES = {
    "ar ARG": "Argentina",
    "ng NGA": "Nigeria",
    "dk DEN": "Denmark",
    "de GER": "Germany",
    "be BEL": "Belgium",
    "fr FRA": "France",
    "pt POR": "Portugal",
    "no NOR": "Norway",
    "br BRA": "Brazil",
    "eng ENG": "England",
    "es ESP": "Spain",
    "pl POL": "Poland",
    "it ITA": "Italy",
    "cl CHI": "Chile",
    "sn SEN": "Senegal",
    "ma MAR": "Morocco",
    "dz ALG": "Algeria",
    "ca CAN": "Canada",
    "sr SUR": "Suriname",
    "jp JPN": "Japan",
    "at AUT": "Austria",
    "nl NED": "Netherlands",
    "il ISR": "Israel",
    "rs SRB": "Serbia",
    "hr CRO": "Croatia",
    "uy URU": "Uruguay",
    "xk KVX": "Kosovo",
    "ua UKR": "Ukraine",
    "gh GHA": "Ghana",
    "ba BIH": "Bosnia",
    "cm CMR": "Cameroon",
    "ch SUI": "Switzerland",
    "eg EGY": "Egypt",
    "tr TUR": "Turkey",
    "ao ANG": "Angola",
    "ge GEO": "Georgia",
}
