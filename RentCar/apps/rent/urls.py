from django.urls import path, include
from . import views
from RentCar.apps.accounts.views import redirect_view

app_name = 'rent'

urlpatterns = [
    path('', redirect_view, name='index'),
    path('cars', views.cars, name='cars'),
    path('user_rents<int:user_id>', views.user_rents, name='user_rents'),
    path('cars/<int:car_id>', views.cars_detailed, name='cars_detailed'),
    path('rents/<int:rent_id>', views.rent_detailed, name='rent_detailed'),

]