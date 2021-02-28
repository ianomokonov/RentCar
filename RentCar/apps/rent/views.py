from django.shortcuts import render, get_object_or_404
from .models import Cars, Rent
from django.contrib.auth.models import User

def index(request):
    return render(request, 'rent/index.html')


def cars(request):
    cars_list = Cars.objects.order_by('brand')
    return render(request, 'rent/list_cars.html', {'cars_list': cars_list})


def user_rents(request, user_id):
    curr_user = get_object_or_404(User, pk=user_id)
    linked_rents = curr_user.rent_set.all()
    return render(request, 'rent/list_rents.html', {'rent_list': linked_rents})


def cars_detailed(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    return render(request, 'rent/detailed_car.html', {'car': car})

def rent_detailed(request, rent_id):
    rent = get_object_or_404(Rent, pk=rent_id)
    return render(request, 'rent/detailed_rent.html', {'rent': rent})