from django.urls import path, include
from . import views

app_name = 'rent'

urlpatterns = [
    path('', views.index, name='index'),
    path('cars', views.cars, name='cars'),
    path('user_rents<int:user_id>', views.user_rents, name='user_rents'),
    path('cars/<int:car_id>', views.cars_detailed, name='cars_detailed'),
    path('rents/<int:rent_id>', views.rent_detailed, name='rent_detailed'),

]