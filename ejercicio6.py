import json
equipos = [
    {
        "nombre": "Alianza Lima",
        "pais": "Perú",
    },
    {
        "nombre": "Universitario",
        "pais": "Perú",
    },
    {
        "nombre": "Boca Juniors",
        "pais": "Argentina",
    },
    {
        "nombre": "River Plate",
        "pais": "Argentina",
    },
    {
        "nombre": "San Lorenzo",
        "pais": "Argentina",
    },
    {
        "nombre": "palmeiras",
        "pais": "Brasil",
    },
    {
        "nombre": "Flamengo",
        "pais": "Brasil",
    }
]
jsonequipos = json.dumps(equipos, indent=4)
print(jsonequipos)
