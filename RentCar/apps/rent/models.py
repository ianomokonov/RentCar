from django.db import models
from django.utils import timezone

class Cars(models.Model):

    class Meta:
        db_table = 'Cars'
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    car_id = models.AutoField('id', primary_key=True)
    brand = models.CharField('Марка', max_length=100)
    model = models.CharField('Модель', max_length=100)
    release_year = models.IntegerField('Год выпуска')
    color = models.CharField('Цвет', max_length=100)
    engine = models.FloatField('Объем двигателя')
    hp = models.IntegerField('Лошадиные силы')
    gearbox = models.CharField('Коробка', max_length=100)
    price = models.FloatField('Цена')

    def __str__(self):
        return f'{self.brand} {self.model}'


class Rent(models.Model):

    class Meta:
        db_table = 'Rent'
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'

    rent_id = models.AutoField('id', primary_key=True)
    cars = models.ForeignKey('Cars', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    rent_date = models.DateTimeField('Дата бронирования', blank=True)
    rent_from = models.DateField('Начало аренды')
    rent_till = models.DateField('Конец аренды')
    total_price = models.FloatField('Стоимость аренды', blank=True)

    def save(self, *args, **kwargs):
        self.rent_date = timezone.now()
        self.total_price = (self.rent_till - self.rent_from).days * self.cars.price
        super(Rent, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user}_{self.cars}'
