from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from GAI import models


@login_required
def index(request):
    return render(request, "index.html", {})

def create_dtp(request):
    if (request.method == "GET"):
        return render(request, "addCard.html", {})
    elif request.method == "POST":
        if(request.POST.get('step') == "0"):
            card_number = request.POST.get("card_number")
            dateTime = request.POST.get("date")
            place = request.POST.get("place")
            type_dtp = request.POST.get("type")
            responce = render(request, "aboutDriver.html", {"card_number":card_number, "date":dateTime, "place":place, "type":type_dtp})
            return responce
        elif(request.POST.get('step') == "1"):
            auto_mark = request.POST.get("auto_mark")


def allIncident(request):
    allIncident = models.cards.objects.all()
    return render(request, "allIncidents.html", {"data":allIncident})

# Create your views here.
