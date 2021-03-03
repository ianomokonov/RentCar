from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars, Rent
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'rent/index.html')


def cars(request):
    cars_list = Cars.objects.order_by('brand')
    return render(request, 'rent/list_cars.html', {'cars_list': cars_list})


def user_rents(request, user_id):
    curr_user = get_object_or_404(User, pk=user_id)
    linked_rents = curr_user.rent_set.all()
    return render(request, 'rent/list_rents.html', {'rent_list': linked_rents, 'user': curr_user})


def cars_detailed(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    return render(request, 'rent/detailed_car.html', {'car': car})


def add_car(request):
    if request.method == "POST":
        new_car = Cars(brand=request.POST['brand'], model=request.POST['model'],
                       release_year=request.POST['release_year'], color=request.POST['color'],
                       engine=request.POST['engine'],
                       hp=request.POST['hp'], gearbox=request.POST['gearbox'], price=request.POST['price'])
        new_car.save()
        return HttpResponseRedirect(reverse('rent:cars'))
    return render(request, 'rent/add_car.html')


def delete_car(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    car.delete()
    return HttpResponseRedirect(reverse('rent:cars'))


def change_car(request, car_id):
    car = get_object_or_404(Cars, pk=car_id)
    if request.method == "POST":
        car.brand = request.POST['brand']
        car.model = request.POST['model']
        car.release_year = request.POST['release_year']
        car.color = request.POST['color']
        car.engine = request.POST['engine']
        car.hp = request.POST['hp']
        car.gearbox = request.POST['gearbox']
        car.price = request.POST['price']
        car.save()
        return HttpResponseRedirect(reverse('rent:cars_detailed', args=(car.car_id,)))
    return render(request, 'rent/change_car.html', {'car': car, 'engine': str(car.engine), 'price': str(car.price)})


def add_rent(request, user_id):
    all_cars = Cars.objects.all()
    cars_names = {a.car_id: f'{a.brand} {a.model}' for a in all_cars}
    if request.method == "POST":
        new_meteor = Rent(cars_id=request.POST['cars'], user_id=user_id,
                          rent_from=request.POST['rent_from'], rent_till=request.POST['rent_till'])
        new_meteor.save()
        return HttpResponseRedirect(reverse('rent:user_rents', args=(user_id,)))
    return render(request, 'rent/add_rent.html', {'cars_names': cars_names, 'car_id': int(request.GET.get('carId'))})


def delete_rent(request, rent_id , user_id):
    rent = get_object_or_404(Rent, pk=rent_id)
    rent.delete()
    return HttpResponseRedirect(reverse('rent:user_rents', args=(user_id,)))
