from django.shortcuts import render
#from django.http import HttpResponse
from django.http import Http404
from inventory.models import Item # Imports item models, for querying database



def index(request):
	items = Item.objects.exclude(amount=0)  # excludes item if we don't have it
	return render(request, 'inventory/index.html', {
		'items': items,
	})

def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'inventory/item_detail.html', {
		'item': item,
	})

# When views call render, it passes data to template, which generates HTML to show the user 
