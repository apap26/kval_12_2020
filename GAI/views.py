from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, "home.html", {})

def create_dtp(request):
    if (request.method == "GET"):
        return render(request, "addCard.html", {})
    elif request.method == "POST":
        card_number = request.POST.get("card_number")
        dateTime = request.POST.get("date")
        place = request.POST.get("place")
        type_dtp = request.POST.get("type")


# Create your views here.
