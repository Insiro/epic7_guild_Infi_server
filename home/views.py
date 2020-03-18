from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.exceptions import PermissionDenied

import home.models as Emodels

# Create your views here.


def index(request):
    noticLit = Emodels.notic.objects.filter(important=True)
    hintLit = Emodels.tips.objects.filter(important=True)
    return render(
        request, "e7index.html", {"notics": noticLit, "hints": hintLit, "rev": False}
    )


def revert(request):
    noticLit = Emodels.notic.objects.filter(important=True)
    hintLit = Emodels.tips.objects.filter(important=True)
    return render(
        request, "e7index.html", {"notics": noticLit, "hints": hintLit, "rev": True}
    )


def tiplit(request):
    lit = Emodels.tips.objects.all().order_by("-id")
    hitlist = {"datas": lit, "table": "tips"}
    return render(request, "e7list.html", hitlist)


def guildPR(request):
    return render(request, "e7PR.html")


def search(request):
    req = request.GET
    for r in req:
        r.replace("<", "&lt")
    datas = {"kq": None, "notic": list(), "tips": list()}
    if "kq" in req:
        kq = req.get("kq")
        kq = kq.split(" ")
        search_filter = Q(name=None)
        for k in kq:
            search_filter = (
                Q(name__icontains=k) | Q(writer__icontains=k) | search_filter
            )
        datas["kq"] = " ".join(kq)
        datas["notic"] = Emodels.notic.objects.all().filter(search_filter)
        datas["tips"] = Emodels.tips.objects.all().filter(search_filter)
    return render(request, "e7search.html", datas)


def notic(request):
    lit = Emodels.notic.objects.all().order_by("-id")
    datas = {"datas": lit, "table": "notic"}
    return render(request, "e7list.html", datas)


def post(request):
    if not request.session.get("isSigned"):
        return redirect(revert)
    return render(request, "e7post.html")


class Astatus:
    attack = 0
    plusAttac = 0
    attackRank = 1
    other = 0
    otherRank = 1
    Pow = 1
    critical = 0
    criticalDamage = 150
    plus = 1
    Dep = 0
    win = None

    def getDamage(self):
        damage = (
            self.attack * (1 + self.plusAttac) * self.attackRank
            + self.other * self.otherRank / 100 * 1.871
        )
        damage = damage / (self.Dep / 300 + 1)
        cri = self.critical / 100 * (self.criticalDamage / 100 - 1)
        damage = damage + damage * cri
        damage = damage * self.plus
        if self.win == "on":
            damage = damage * 1.1
        return damage


def damageCalc(request):
    herolist = Emodels.Heros.objects.all().order_by("name")
    return render(request, "e7damageCalc.html", {"heros": herolist})


def detail(request):
    req = request.GET
    for r in req:
        r.replace("<", "&lt;").replace(">", "&rt;")
    data = {"id": None, "table": None}
    if "table" in req and "id" in req:
        data["table"] = req.get("table")
        data["id"] = req.get("id")
    return render(request, "e7detail.html", data)
