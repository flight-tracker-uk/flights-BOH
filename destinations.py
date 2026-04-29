"""Bournemouth Airport (BOH) destinations — April 2026."""

DESTINATIONS = {
    "BOH": {
        "name": "Bournemouth",
        "routes": {
            "ACE": "Lanzarote",
            "AGA": "Agadir",
            "AGP": "Malaga",
            "ALC": "Alicante",
            "AYT": "Antalya",
            "BGI": "Barbados",
            "CCF": "Carcassonne",
            "CFU": "Corfu",
            "CHQ": "Crete (Chania)",
            "DLM": "Dalaman",
            "EDI": "Edinburgh",
            "EFL": "Kefalonia",
            "EGC": "Bergerac",
            "ENF": "Enontekio",
            "FAO": "Faro",
            "FNC": "Funchal",
            "FUE": "Fuerteventura",
            "GRO": "Girona",
            "GVA": "Geneva",
            "HER": "Crete (Heraklion)",
            "IBZ": "Ibiza",
            "IVL": "Ivalo",
            "KEF": "Reykjavik",
            "KGS": "Kos",
            "KRK": "Krakow",
            "KTT": "Kittila",
            "LCA": "Larnaca",
            "LPA": "Gran Canaria",
            "MAH": "Menorca",
            "MLA": "Malta",
            "PFO": "Paphos",
            "PMI": "Palma",
            "PRG": "Prague",
            "REU": "Reus",
            "RHO": "Rhodes",
            "RMU": "Murcia",
            "TFS": "Tenerife South",
            "TPS": "Trapani",
            "VIE": "Vienna",
            "WRO": "Wroclaw",
            "XRY": "Jerez",
            "ZAD": "Zadar",
            "ZTH": "Zakynthos",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
