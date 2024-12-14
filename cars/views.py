from django.http import HttpResponse
from django.shortcuts import redirect, render
from cars.forms import CarCreate
from cars.models import Car

def home(request):
    cars = Car.objects.all  
    return render(request, 'home.html', {'cars': cars})

def car_detail(request, id):
    car = Car.objects.get(id=id)    

    return render(request, 'details.html', {'car': car})

def upload(request):
    form = CarCreate()

    if request.method == 'POST':
        form = CarCreate(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            for field in form.cleaned_data:
                print(f"{field}: {form.cleaned_data[field]}")
            return HttpResponse('Form is not valid')
    else:
        return render(request, 'car_form.html', {'form': form})
    
def delete(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return redirect('home')

def edit(request, id):
    car = Car.objects.get(id=id)
    form = CarCreate(instance=car)

    if request.method == 'POST':
        form = CarCreate(request.POST, instance=car)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('Form is not valid')
    else:
        return render(request, 'edit.html', {'form': form, 'car': car})