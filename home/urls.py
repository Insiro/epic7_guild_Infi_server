from django.urls import path
from . import views, api, outApi


urlpatterns = [
    path("", views.index),
    path("Index", views.revert),
    path("index", views.index),
    path("tips", views.tiplit),
    path("search", views.search),
    path("notic", views.notic),
    path("post", views.post),
    path("damage", views.damageCalc),
    path("detail", views.detail),
    path("about", views.guildPR),
    path("e-score", views.Escore),
    path("404", views._404),
    # epic7API
    path("info", api.info),
    path("api/authorize", api.authorize),
    path("api/isAuthrized", api.isAuthrized),
    path("api/signOut", api.signOut),
    # epicOutApi
    path("api/getNotic", outApi.getNotic),
    path("api/getReisterNotic", outApi.getReisterNotic),
    path("api/getTip", outApi.getTip),
    path("api/getBotSkills", outApi.getBotSkills),
    path("api/getKakao", api.getKakao),
]
