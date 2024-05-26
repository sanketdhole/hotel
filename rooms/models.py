from django.db import models

class RoomRate(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=255)
    default_rate = models.DecimalField(max_digits=10, decimal_places=2)

class OverriddenRoomRate(models.Model):
    overridden_rate_id = models.AutoField(primary_key=True)
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    overridden_rate = models.DecimalField(max_digits=10, decimal_places=2)
    stay_date = models.DateField()

class Discount(models.Model):
    DISCOUNT_CHOICES = (
        ('fixed', 'Fixed'),
        ('percentage', 'Percentage'),
    )
    discount_id = models.AutoField(primary_key=True)
    discount_name = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=20, choices=DISCOUNT_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)

class DiscountRoomRate(models.Model):
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

