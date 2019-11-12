from django.shortcuts import render
from listings.choices import bedroom_choices,price_choices,state_choices
from listings.models import Listing
from realtors.models import Realtor


# Create your views here.
def index(request):
    listinges = Listing.objects.all()[:3]
    context = {
        'listinges':listinges,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'state_choices':state_choices

    }

    return render(request, 'pages/home.html',context)


def about(request):
    team = Realtor.objects.all()
    mvp_realtor = Realtor.objects.filter(is_mvp=True)
    context = {
        'team':team,
        'mvp':mvp_realtor
    }
    return render(request, 'pages/about.html',context)
