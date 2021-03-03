from django.urls import path, include
from . import views
from RentCar.apps.accounts.views import redirect_view

app_name = 'rent'

urlpatterns = [
    path('', redirect_view, name='index'),
    path('cars', views.cars, name='cars'),
    path('user_rents/<int:user_id>', views.user_rents, name='user_rents'),
    path('cars/<int:car_id>', views.cars_detailed, name='cars_detailed'),
    path('add_car', views.add_car, name='add_car'),
    path('cars/<int:car_id>/delete_car', views.delete_car, name='delete_car'),
    path('cars/<int:car_id>/change_car', views.change_car, name='change_car'),
    path('user_rents/<int:user_id>/add_rent', views.add_rent, name='add_rent'),
    path('rents/<int:rent_id>/delete_rent<int:user_id>', views.delete_rent, name='delete_rent'),

]