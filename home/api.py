from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json

import home.models as Emodels


def info(request):
    req = request.GET
    for r in req:
        r.replace("<", "&lt")
    table = req.get("table")
    id = req.get("id")
    if table == "notic":
        data = Emodels.notic.objects.get(id=int(id))
        data = model_to_dict(data)
        print(data)
    elif table == "tips":
        data = model_to_dict(Emodels.tips.objects.get(id=int(id)))
        print(data)
        # dataDic["img"] = str(list(model_to_dict(i)for i in img_))
    else:
        data = get_object_or_404(Emodels.tips, pk=0)
    data["image"] = str(data["image"])
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})


def allRank(requests):
    url = "https://api.epicsevendb.com/api/hero/"
    req = requests.GET
    Cname = req.get("Cname")
    url = url + Cname
    data = {"s": 0}
    return JsonResponse({"data": data}, json_dumps_params={"ensure_ascii": False})


def jsonfy(string):
    li = "{" + string.split("{")[1]
    li = li.split("}")[0] + "}"
    data = json.loads(li)
    return data


@csrf_exempt
def authorize(request):
    if request.method == "POST":
        li = request.POST.get(" name")
        data = jsonfy(li)
        uid = data["uid"]
        upw = data["upw"]
        rows = Emodels.user.objects.all().filter(UID=uid)
        cryptedPW = ""
        if len(rows) == 1:
            row = model_to_dict(rows[0])
            cryptedPW = row["UPW"]
            name = row["name"]
            manager = row["isManager"]
        reuslt = check_password(upw, cryptedPW)
        if reuslt:
            request.session["isSigned"] = True
            request.session["isManager"] = manager
            request.session["uid"] = uid
            request.session["name"] = name
        return JsonResponse({"result": reuslt}, content_type="application/json")
    return JsonResponse({"result": "fail"}, content_type="application/json")


def signOut(request):
    request.session["isSigned"] = False
    return JsonResponse({"result": False})


def isAuthrized(request):
    if request.session.get("isSigned"):
        return JsonResponse({"result": True})
    return JsonResponse({"result": False})


def changePWD(request):
    if request.method == "POST":
        UID = request.POST["id"]
        UPW = make_password(request.POST["pw"])
        NEW = request.POST["newUPW"]
        get_object_or_404(Emodels.user, UID=UID, UPW=make_password(UPW)).update(
            UPW=make_password(NEW)
        )
        return JsonResponse({"result": "success"}, content_type="application/json")
    return JsonResponse({"result": "fail"}, content_type="application/json")


@csrf_exempt
def Signe(request):
    session = request.session
    if session["isSigned"] and session["ismanager"] and request.method == "POST":
        data = jsonfy(request.POST.get(" name"))
        rows = Emodels.user.objects.all().filter(UID=data["uid"])
        if len(rows) != 1:
            return JsonResponse({"result": "fail"}, content_type="application/json")
        rows[0].update(Signed=True, isManager=data["setManager"]).save()
    return JsonResponse({"result": "success"}, content_type="application/json")


@csrf_exempt
def register(request):
    if request.method == "POST":
        if not (UID and UPW and name):
            return JsonResponse({"result": "fail"}, content_type="application/json")
        Emodels.user(
            UID=request.POST["id"],
            UPW=make_password(request.POST["pw"]),
            name=request.POST["name"],
            Signed=False,
        ).save()
    return JsonResponse({"result": "success"}, content_type="application/json")


def getKakao(request):
    return JsonResponse(
        {"con": "87e0df88cc4b2f3e2191d86119d5ff15"}, content_type="application/json"
    )
