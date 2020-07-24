from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    OrderSources = (
        ('Cassandra','Cassandra'),
        ('Jana', 'Jana'),
        ('Kara', 'Kara'),
        ('RK', 'RK'),
        ('Megan', 'Megan'),
        ('Brandy', 'Brandy')
    )
    HouseAccount = (
        ('Baycare', 'Baycare'),
        ('Republic', 'Republic'),
        ('Cater Nation', 'Cater Nation'),
        ('No', 'No')
    )
    orderSource = models.CharField(choices= OrderSources,max_length=100, default='RK')
    houseAccount = models.CharField(choices=HouseAccount,max_length=100, default='Baycare')
    name = models.CharField(max_length=100,default='NO NAME')
    address = models.CharField(max_length=200,default='NO ADDRESS')
    mobile = models.BigIntegerField()
    deliverydriver = models.CharField(max_length=100, default='NOT ASSIGNED')
    deliverytime = models.TimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    specialInstruction = models.CharField(max_length=300, default='NONE')
    cateringAmount = models.BigIntegerField(default='0')
    deliveryFee = models.BigIntegerField(default='0')
    tips = models.BigIntegerField(default='0')
    salesTax = models.IntegerField(default='0')
    customerFeedBack = models.CharField(max_length=300, default='NONE')
    onTime = models.CharField(choices=(('Yes','Yes'), ('No', 'No')), default='Yes',max_length=100)
    deliveryStatus = models.CharField(choices=(('Delivered','Delivered'),('Not Delivered','Not Delivered')), default='Not Delivered',max_length=100)
    customerPaymentStatus = models.CharField(choices=(('PAID','PAID'),('NOT PAID','NOT PAID')), default='NOT PAID',max_length=100)
    employeePaymentStatus = models.CharField(choices=(('PAID', 'PAID'), ('NOT PAID', 'NOT PAID')), default='NOT PAID',max_length=100)
    cateringDate = models.DateTimeField(default=timezone.now)
    commissionAmount = models.IntegerField(default='0')
    commissionStatus = models.CharField(max_length=20, default='NOT PAID')
    estimatedDelivery = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
