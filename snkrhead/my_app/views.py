from django.shortcuts import render

class Shoe:
    def __init__(self, name, amount, description, image_url=""):
        self.name = name
        self.amount = amount
        self.description = description
        self.image_url = image_url

shoes = [
    Shoe('Lost and Found Jordans', 1200, 'Rare Replica 1984 Pair', '/static/images/lostandfound.png'),
    Shoe('Jarritos Dunks', 1000, 'Jaritos dunks inspired by the drink - rare find', '/static/images/jarritos.png'),
    Shoe('UNC Jordans', 500, 'Inspired by Jordans UNC years - light blue edition', '/static/images/unc.png'),
    Shoe('Jordan Golf Green', 280, 'Jordans green golf line - best color', '/static/images/golf.png')

]

def snkr_index(request):
    return render(request, 'shoes/index.html', {'shoes': shoes})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


