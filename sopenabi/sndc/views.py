from django.shortcuts import render_to_response
from django.template.context import RequestContext

from sndc.models import *

# Create your views here.


def home(request):
    # team members recover
    team_members = Team.objects.filter(is_active=True)

    # about us content
    about_us = AboutUs.objects.all()[0] or None

    # nos partenaires
    partenaires = Partner.objects.all()[:8]

    # remonter les produits par categorie
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(is_active=True).order_by('-name')

    ctx = {
        'products': products,
        'categories': categories,
        'about_us': about_us,
        'members': team_members,
        'partners': partenaires
    }
    return render_to_response('pages/index.html', context_instance=RequestContext(request, ctx))