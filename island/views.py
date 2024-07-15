from django.shortcuts import render
from .models import *
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.db import IntegrityError

from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def home(request):
    print("Media Root:", settings.MEDIA_ROOT)
    plat = list(Plat.objects.all())
    for plats in plat:
        print(plats.image1.url)
    
    context={
        'plat':plat
    }

    return render(request,"island/home.html",context)

def about(request):
    return render(request,"island/about.html")



def menu(request):
    plat = list(Plat.objects.all())
    context={
        'plat':plat
    }
    return render(request,"island/food-menu.html",context)

def details(request,id):
    plat = get_object_or_404(Plat, pk=id)
    context={
        'plat':plat,
    }
    return render(request,"island/details.html",context)
    
def reservation(request):
    return render(request,"island/reservation.html")

def creat_res(request):
    missing_fields = []
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        serve = request.POST.getlist("serve")
        time = request.POST.get("time")
        email = request.POST.get('email')
        date = request.POST.get('date')
        
        print(f"name: {name}")
        print(f"phone: {phone}")
        print(f" serve : { serve }")
        print(f"time: {time}")
        print(f"email: {email}")
        print(f"date: {date}")
    
        # Attempt to create a new user
        if not name:
            missing_fields.append("name")
        if not phone:
            missing_fields.append("phone")
        if not serve:
            missing_fields.append("serve")
        if not time:
            missing_fields.append("time")
        if not email:
            missing_fields.append("email")
        if not date:
            missing_fields.append("date")
        if missing_fields:
            message2=f"Missing or invalid fields: {', '.join(missing_fields)}"
            return render(request, "island/reservation.html", {
                "message2": message2
            })
        try:
            reserve = Reservation.objects.create(
                name=name,
                phone=phone,
                email = email ,
                time=time,
                serve=','.join(serve),
                date=date,
            )
            reserve.save()
            message = f"Hey {reserve.name}, thank you for making a reservation at Tasty Bite. We look forward to hosting you on {reserve.date} at {reserve.time}. Bon appétit!"
            return render(request, "island/reservation.html", {
    "message": message
})
  # Call save() on the instance, not the model class
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            return render(request, "island/home.html", {
                "messages": "Reservation Valid."
            })
              
    else:
        return render(request, "island/reservation.html")
