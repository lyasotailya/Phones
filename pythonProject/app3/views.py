import csv
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from django.http import HttpResponse
from django.shortcuts import render

from app3.models import Phone


# Create your views here.


def index(request):
    return HttpResponse("<br/>".join([
        # "<a href='/'>Главная страница </a",
        f"<a href='{reverse('aid')}'>добавить в бд </a",
        f"<br/><a href='{reverse('lp')}'>Каталог </a",
        # f"<br/><a href='{reverse('buter')}'>Бутерброд </a",
    ]))


def append_in_data(request):
    with open("phones.csv", mode="r", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for el in reader:
            phone = Phone(
                id=el['id'],
                name=el['name'],
                image=el['image'],
                price=el['price'],
                release_date=el['release_date'],
                lte_exists=el['lte_exists'],

            )
            phone.save()
    return HttpResponse('Done!')


sort_phones = ['название', 'с дешевых', 'с дорогих']


def list_phones(request):
    sort = request.GET.get('sort', 'id')
    if sort == 'min_price': sort = 'price'
    if sort == 'max_price': sort = '-price'
    phones = Phone.objects.order_by(sort).all()
    context = {
        'phones': phones,
    }
    return render(request, 'phones.html', context=context)


def show_post(request, slug):
    post = get_object_or_404(Phone, slug=slug)
    context = {
        'post': post,
        'name': post.name,
        'price': post.price,
        'image': post.image,
        'release': post.release_date,
        'lte': ('Нет', 'Да')[post.lte_exists],
    }
    return render(request, 'post.html', context=context)
