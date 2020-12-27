import datetime

from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.shortcuts import render

from GAI import models


@login_required
def index(request):
    return render(request, "index.html", {})

def create_dtp(request):
    if (request.method == "GET"):
        type_list = models.type_incident.objects.all()
        weather = models.conditionals.objects.all()
        return render(request, "addCard.html", {"types":type_list, "weather":weather})
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

            prichiny = models.reasons_DTP.objects.all()

            context = {"card_number":card_number, "date":date_time, "place":place, "type":type_dtp, "stateNumber":state_number,
                       "mark":auto_mark, "licenseNumber":license_number, "prichiny":prichiny}
            if(models.drivers.objects.all().filter(license_number = license_number).exists() and
            models.cars.objects.all().filter(plate_number=state_number)):
                return render(request, "casualties.html", context)
            else:
                context['marks'] = marks
                context['error'] = "Водительское удостоверение или автомобиь не найдены"
                return render(request, "aboutDriver.html", context)
        elif(request.POST.get('step') == "2"):
            card_number = request.POST.get("card_number")
            date_time = request.POST.get("date")
            place = request.POST.get("place")
            type_dtp = int(request.POST.get("type"))
            auto_mark = request.POST.get("auto_mark")
            state_number = request.POST.get("stateNumber")
            license_number = request.POST.get("licenseNumber")
            number_wounded = request.POST.get("numberWounded")
            death_toll = request.POST.get("deathToll")


            dfbj = models.reasons_DTP.objects.all()
            selects = []
            for r in dfbj:
                selects.append([r, True if request.POST.get("HB"+str(r.id)) != None else False])
            date_time_d = datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
            incedet = models.type_incident.objects.get(id=type_dtp)
            card = models.cards(date=date_time_d, place=place, incident=incedet,
                                car=models.cars.objects.all()
                                    .filter(plate_number=state_number)[0], driver=models.drivers.objects.all()
                                    .filter(license_number = license_number)[0], died_count=death_toll,
                                injured_count=int(number_wounded), weather=models.conditionals.objects.get(id=1))
            card.save()
            for i in selects:
                if i[1] == True:
                    card.prichiny.add(i[0])
            card.save()
            return render(request, "casualties.html", {"succes":True})
            #card.save()


def allIncident(request):
    allIncident = models.cards.objects.all()
    return render(request, "allIncidents.html", {"data":allIncident})


def thIncident(request, id):
    card = models.cards.objects.all().filter(id=id)
    return render(request, "aboutRoadAccident.html", {"card":card[0]})
# Create your views here.
