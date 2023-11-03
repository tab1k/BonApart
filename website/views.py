from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from users.models import Notification
from .forms import ApartmentFilterForm, CarFilterForm, ReservationForm
from website.models import *
import telebot
from .models import Reservation
from django.conf import settings
from django.shortcuts import get_object_or_404
from telegram import Bot
from django.shortcuts import render
from django.http import JsonResponse
from .models import Reservation


    # bot_token = '6709416090:AAFayt-eVfuaYUYKUHjkt4FGKEHUgO7Oo6E'
    # chat_id = '-1002073862577'


class IndexView(View):

    def get(self, request):
        user = request.user
        apartment = Apartment.objects.filter(price__lte=20000)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        context = {
            'user': user,
            'apartment': apartment,
            'notifications' : notifications,
        }
        return render(request, 'website/index.html', context)


class SearchResultsView(View):
    class SearchResultsView(View):
        template_name = 'website/search_results.html'

        def post(self, request):
            # Обработка POST-запроса и выполнение поиска
            class_choice = request.POST.get('class_choice')
            price_choice = request.POST.get('price_choice')
            rating_choice = request.POST.get('rating_choice')
            # Дополнительная логика поиска на основе формы

            # Перенаправление на страницу с результатами поиска
            return redirect('search_results', class_choice=class_choice, price_choice=price_choice,
                            rating_choice=rating_choice)



class ApartmentView(View):
    template_name = 'website/apartments_list.html'

    def get(self, request):

        form = ApartmentFilterForm(request.GET)
        apartments = Apartment.objects.all()
        discount = Discount.objects.filter(apartment__in=apartments)
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        if form.is_valid():
            class_choice = form.cleaned_data['class_choice']
            price_choice = form.cleaned_data['price_choice']
            rating_choice = form.cleaned_data['rating_choice']
            additional_choice = form.cleaned_data['additional_choice']

            if class_choice:
                apartments = apartments.filter(level=class_choice)

            if price_choice:
                if price_choice == '1':
                    apartments = apartments.filter(price__gte=10000)
                elif price_choice == '2':
                    apartments = apartments.filter(price__range=(10000, 15000))
                elif price_choice == '3':
                    apartments = apartments.filter(price__range=(15000, 20000))
                elif price_choice == '4':
                    apartments = apartments.filter(price__range=(20000, 25000))
                elif price_choice == '5':
                    apartments = apartments.filter(price__gte=25000)

            if rating_choice:
                apartments = apartments.filter(rating=rating_choice)

            if rating_choice:
                apartments = apartments.filter(rating=rating_choice)

            if additional_choice:
                for option in additional_choice:
                    apartments = apartments.filter(**{option: True})

        paginator = Paginator(apartments, 10)  # 10 - количество элементов на странице

        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            'apartment': page,
            'form': form,
            'discount': discount,
            'notifications': notifications,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ReservationForm(request.POST)
        context = {}  # Инициализация переменной context

        if form.is_valid():
            form.save()
            # Дополнительная логика, например, перенаправление на страницу успешного бронирования
        else:
            apartments = Apartment.objects.all()
            context = {'apartments': apartments, 'form': form}

        return render(request, self.template_name, context)


class StockView(View):

    def get(self, request):
        stock = Stock.objects.filter(valid=True).order_by('start_date')
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'stock' : stock,
            'notifications': notifications,
        }
        return render(request, 'website/stock.html', context)


class CollaborationView(View):

    def get(self, request):
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'notifications': notifications,
        }

        return render(request, 'website/collaboration.html', context)


class TransfersView(View):

    def get(self, request):
        form = CarFilterForm(request.GET)
        cars = Car.objects.all()
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        if form.is_valid():
            class_choice = form.cleaned_data['class_choice']
            if class_choice:
                cars = cars.filter(level=class_choice)

        paginator = Paginator(cars, 10)  # 10 - количество элементов на странице

        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

        context = {
            'cars': page,
            'form': form,
            'notifications': notifications,
        }
        return render(request, 'website/transfers.html', context)




class AboutView(View):

    def get(self, request):
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')

        context = {
            'notifications': notifications,
        }

        return render(request, 'website/about-us.html', context)


class ApartamentsDetailView(View):

    def get(self, request, pk):
        notifications = Notification.objects.filter(read=False).order_by('-timestamp')
        apartments_detail = Apartment.objects.get(pk=pk)
        # geo_position = GeoPosition.objects.get(apartment=apartments_detail)


        context = {
            'detail': apartments_detail,
            # 'geo_position': geo_position,
            'notifications': notifications,
        }

        return render(request, 'website/detail.html', context)






