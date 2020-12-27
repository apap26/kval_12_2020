import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from GAI import models


@login_required
def index(request):
    return render(request, "index.html", {})

def create_dtp(request):
    if (request.method == "GET"):
        type_list = models.type_incident.objects.all()
        return render(request, "addCard.html", {"types":type_list})
    elif request.method == "POST":
        marks = models.cars_brand.objects.all()
        if(request.POST.get('step') == "0"):
            card_number = request.POST.get("card_number")
            dateTime = request.POST.get("date")
            place = request.POST.get("place")
            type_dtp = request.POST.get("type")
            responce = render(request, "aboutDriver.html", {"card_number":card_number, "date":dateTime, "place":place,
                                                            "type":type_dtp, "marks":marks})
            return responce
        elif(request.POST.get('step') == "1"):
            card_number = request.POST.get("card_number")
            date_time = request.POST.get("date")
            place = request.POST.get("place")
            type_dtp = request.POST.get("type")
            auto_mark = request.POST.get("auto_mark")
            state_number = request.POST.get("stateNumber")
            license_number = request.POST.get("licenseNumber")
            context = {"card_number":card_number, "date":date_time, "place":place, "type":type_dtp, "stateNumber":state_number,
                       "mark":auto_mark, "licenseNumber":license_number}
            if(models.drivers.objects.all().filter(license_number = license_number).exists()):
                return render(request, "casualties.html", context)
            else:
                context['marks'] = marks
                context['error'] = "Водительское удостоверение не найдено"
                return render(request, "aboutDriver.html", context)
        elif(request.POST.get('step') == "2"):
            card_number = request.POST.get("card_number")
            date_time = request.POST.get("date")
            place = request.POST.get("place")
            type_dtp = request.POST.get("type")
            auto_mark = request.POST.get("auto_mark")
            state_number = request.POST.get("stateNumber")
            license_number = request.POST.get("licenseNumber")
            number_wounded = request.POST.get("numberWounded")
            death_toll = request.POST.get("deathToll")
            date_time_d = datetime.datetime.strptime(date_time,"%Y-%m-%dT%H:%M")
            card = models.cards(date=date_time_d, place=place, incident=models.type_incident.objects.get(int(type_dtp)),
                                car=models.cars.objects.all()
                                    .filter(plate_number=state_number), driver=models.drivers.objects.all()
                                    .filter(license_number = license_number), died_count=death_toll,
                                injured_count=number_wounded, conditional_id=2)
            card.save()
            card.Причины.add()
            card.save()


def allIncident(request):
    allIncident = models.cards.objects.all()
    return render(request, "allIncidents.html", {"data":allIncident})

# Create your views here.
