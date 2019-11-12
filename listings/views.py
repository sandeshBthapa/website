from django.shortcuts import render
from .models import Listing
from django.core.paginator import  Paginator
from listings.choices import bedroom_choices, state_choices, price_choices


# Create your views here.

def listings(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing1(request, listing_id):
    listing2 = Listing.objects.get(id=str(listing_id))
    context = {
        'listing2': listing2
    }

    return render(request, 'listings/single_listing.html', context)


def Search(request):
    queryset_list =Listing.objects.all()

    #for keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)


    #for City

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #for state

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__exact=state)


    #for Price


    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lt=price)


     #for Bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    context = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'listings':queryset_list

    }
    return render(request, 'listings/search.html',context)







