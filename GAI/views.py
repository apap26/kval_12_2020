from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from GAI import models


@login_required
def index(request):
    return render(request, "home.html", {})

def create_dtp(request):
    if (request.method == "GET"):
        return render(request, "addCard.html", {})
    elif request.method == "POST":
        if(request.POST.get('step') == "0"):
            card_number = request.POST.get("card_number")
            dateTime = request.POST.get("date")
            place = request.POST.get("place")
            type_dtp = request.POST.get("type")
            responce = render(request, "aboutDriver.html", {})
            responce.set_cookie("card_number", card_number)
            responce.set_cookie("dateTime", dateTime)
            responce.set_cookie("place", place)
            responce.set_cookie("type_dtp", type_dtp)
            return responce
        elif(request.POST.get('step') == "1"):
            auto_mark = request.POST.get("auto_mark")

def allIncident(request):
    allIncident = models.cards.objects.all()
    return render(request, "allIncidents.html", {"data":allIncident})
# Create your views here.
