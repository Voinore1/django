from django.http import HttpResponse
from django.shortcuts import render

cars = [
    {
        "id": 1,
        "brand": "Toyota",
        "model": "Camry",
        "manufacture_year": 2020,
        "description": "A reliable and fuel-efficient sedan.",
        "type": "Sedan",
        "price": 24000
    },
    {
        "id": 2,
        "brand": "Ford",
        "model": "Mustang",
        "manufacture_year": 2019,
        "description": "A classic American muscle car.",
        "type": "Coupe",
        "price": 35000
    },
    {
        "id": 3,
        "brand": "Honda",
        "model": "CR-V",
        "manufacture_year": 2021,
        "description": "A compact SUV with great versatility.",
        "type": "SUV",
        "price": 30000
    },
    {
        "id": 4,
        "brand": "Chevrolet",
        "model": "Tahoe",
        "manufacture_year": 2018,
        "description": "A full-size SUV with plenty of space.",
        "type": "SUV",
        "price": 50000
    },
    {
        "id": 5,
        "brand": "BMW",
        "model": "3 Series",
        "manufacture_year": 2022,
        "description": "A luxury sedan with sporty performance.",
        "type": "Sedan",
        "price": 41000
    },
    {
        "id": 6,
        "brand": "Audi",
        "model": "Q5",
        "manufacture_year": 2020,
        "description": "A premium compact SUV with advanced features.",
        "type": "SUV",
        "price": 43000
    },
    {
        "id": 7,
        "brand": "Mercedes-Benz",
        "model": "C-Class",
        "manufacture_year": 2019,
        "description": "A luxury sedan with a comfortable ride.",
        "type": "Sedan",
        "price": 39000
    },
    {
        "id": 8,
        "brand": "Tesla",
        "model": "Model S",
        "manufacture_year": 2021,
        "description": "An electric sedan with impressive range.",
        "type": "Sedan",
        "price": 80000
    },
    {
        "id": 9,
        "brand": "Jeep",
        "model": "Wrangler",
        "manufacture_year": 2018,
        "description": "A rugged SUV built for off-road adventures.",
        "type": "SUV",
        "price": 35000
    },
    {
        "id": 10,
        "brand": "Porsche",
        "model": "911",
        "manufacture_year": 2022,
        "description": "A high-performance sports car.",
        "type": "Coupe",
        "price": 90000
    }
]

def home(request):

    list = '<ul>'

    for i in cars:
        list += f'<li>{i['brand']} {i['model']} - ${i['price']}</li>'

    list += '</ul>'    

    return HttpResponse('<h1>Car list</h2>' + list)

def car_detail(request, id):
    car = None
    for i in cars:
        if i['id'] == id:
            car = i
            break

    detail = f'<h1>{car["brand"]} {car["model"]}</h1>'
    detail += f'<p>Year: {car["manufacture_year"]}</p>'
    detail += f'<p>Type: {car["type"]}</p>'
    detail += f'<p>Description: {car["description"]}</p>'
    detail += f'<p>Price: ${car["price"]}</p>'


    return HttpResponse(detail)

