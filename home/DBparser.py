import requests
from django.forms.models import model_to_dict
import home.models as Emodels


# API Documents : https://epicsevendb-apiserver.herokuapp.com/


def parse():
    print(datetime.today().strftime("%Y%m%d"))
    heroInDB = Emodels.Heros.objects.values("SearchKey")
    url = "https://api.epicsevendb.com/api/hero"
    req = requests.get(url)
    json = req.json()
    heroInDB = list(hero["SearchKey"] for hero in heroInDB)
    for hero in json["results"]:
        _id = "'" + hero["_id"] + "'"
        if hero["_id"] not in heroInDB:
            Emodels.Heros(
                SearchKey=hero["_id"],
                name=hero["name"],
                rarity=hero["rarity"],
                classType=hero["classType"],
                element=hero["element"],
            ).save()
            print(hero["_id"])


if __name__ == "__main__":
    print("start")
