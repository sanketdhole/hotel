from django.shortcuts import render, redirect
from datetime import date

from .models import RoomRate, OverriddenRoomRate, DiscountRoomRate, Discount
from .forms import RoomRateForm, OverriddenRoomRateForm, DiscountForm, DiscountRoomRateForm

def default_view(request):
    stay_date_str = request.GET.get('stay_date')
    if stay_date_str:
        stay_date = date.fromisoformat(stay_date_str)
    else:
        stay_date = date.today()
    rooms_with_rates = []
    room_rates = RoomRate.objects.all()
    for room_rate in room_rates:
        overridden_rate = OverriddenRoomRate.objects.filter(room_rate=room_rate, stay_date=stay_date).first()
        if overridden_rate:
            rate_for_date = overridden_rate.overridden_rate
        else:
            rate_for_date = room_rate.default_rate
        highest_discount = DiscountRoomRate.objects.filter(room_rate=room_rate).order_by('-discount__discount_value').first()
        if highest_discount:
            if highest_discount.discount.discount_type == 'fixed':
                final_rate = rate_for_date - highest_discount.discount.discount_value
            elif highest_discount.discount.discount_type == 'percentage':
                final_rate = rate_for_date * (1 - highest_discount.discount.discount_value / 100)
        else:
            final_rate = rate_for_date
        rooms_with_rates.append({
            'room_id': room_rate.room_id,
            'room_name': room_rate.room_name,
            'rate_for_date': rate_for_date,
            'final_rate': final_rate,
        })

    return render(request, 'default_view.html', {'rooms': rooms_with_rates, 'stay_date': stay_date})


# room rates views
def room_rate_list(request):
    room_rates = RoomRate.objects.all()
    return render(request, 'room_rate_list.html', {'room_rates': room_rates})

def room_rate_create(request):
    if request.method == 'POST':
        form = RoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_rate_list')
    else:
        form = RoomRateForm()
    return render(request, 'room_rate_form.html', {'form': form})

def room_rate_update(request, room_id):
    room_rate = RoomRate.objects.get(pk=room_id)
    if request.method == 'POST':
        form = RoomRateForm(request.POST, instance=room_rate)
        if form.is_valid():
            form.save()
            return redirect('room_rate_list')
    else:
        form = RoomRateForm(instance=room_rate)
    return render(request, 'room_rate_form.html', {'form': form})

def room_rate_delete(request, room_id):
    room_rate = RoomRate.objects.get(pk=room_id)
    room_rate.delete()
    return redirect('room_rate_list')

# over ridden rates views
def overridden_rate_list(request):
    overridden_rates = OverriddenRoomRate.objects.all()
    return render(request, 'overridden_rates.html', {'overridden_rates': overridden_rates})

def overridden_rate_create(request):
    if request.method == 'POST':
        form = OverriddenRoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('overridden_rate_list')
    else:
        form = OverriddenRoomRateForm()
    return render(request, 'overridden_rates_form.html', {'form': form})

def overridden_rate_update(request, overridden_rate_id):
    overridden_rate = OverriddenRoomRate.objects.get(pk=overridden_rate_id)
    if request.method == 'POST':
        form = OverriddenRoomRateForm(request.POST, instance=overridden_rate)
        if form.is_valid():
            form.save()
            return redirect('overridden_rate_list')
    else:
        form = OverriddenRoomRateForm(instance=overridden_rate)
    print(form)
    return render(request, 'overridden_rates_form.html', {'form': form})

def overridden_rate_delete(request, overridden_rate_id):
    overridden_rate = OverriddenRoomRate.objects.get(pk=overridden_rate_id)
    overridden_rate.delete()
    return redirect('overridden_rate_list')

# discount views
def discount_list(request):
    discounts = Discount.objects.all()
    return render(request, 'discount_list.html', {'discounts': discounts})

def discount_create(request):
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discount_list')
    else:
        form = DiscountForm()
    return render(request, 'discount_form.html', {'form': form})

def discount_update(request, pk):
    discount = Discount.objects.get(pk=pk)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            return redirect('discount_list')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'discount_form.html', {'form': form})

def discount_delete(request, pk):
    discount = Discount.objects.get(pk=pk)
    discount.delete()
    return redirect('discount_list')

def discount_room_rate_list(request):
    discount_room_rates = DiscountRoomRate.objects.all()
    if request.method == 'POST':
        form = DiscountRoomRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discount_room_rate')
    else:
        form = DiscountRoomRateForm()
    return render(request, 'discount_room_rates.html', {'discount_room_rates': discount_room_rates, 'form': form})

def discount_room_rate_update(request, discount_room_rate_id):
    discount_room_rate = get_object_or_404(DiscountRoomRate, pk=discount_room_rate_id)
    if request.method == 'POST':
        form = DiscountRoomRateForm(request.POST, instance=discount_room_rate)
        if form.is_valid():
            form.save()
            return redirect('discount_room_rate_list')
    else:
        form = DiscountRoomRateForm(instance=discount_room_rate)
    return render(request, 'discount_room_rate_form.html', {'form': form})

# View to delete a discount-room rate association
def discount_room_rate_delete(request, discount_room_rate_id):
    discount_room_rate = get_object_or_404(DiscountRoomRate, pk=discount_room_rate_id)
    discount_room_rate.delete()
    return redirect('discount_room_rate')
