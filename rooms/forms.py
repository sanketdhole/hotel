from django import forms
from .models import RoomRate, OverriddenRoomRate, Discount, DiscountRoomRate

class RoomRateForm(forms.ModelForm):
    class Meta:
        model = RoomRate
        fields = ['room_id', 'room_name', 'default_rate']

class OverriddenRoomRateForm(forms.ModelForm):
    class Meta:
        model = OverriddenRoomRate
        fields = ['room_rate', 'overridden_rate', 'stay_date']

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['discount_id', 'discount_name', 'discount_type', 'discount_value']

class DiscountRoomRateForm(forms.ModelForm):
    class Meta:
        model = DiscountRoomRate
        fields = ['room_rate', 'discount']
