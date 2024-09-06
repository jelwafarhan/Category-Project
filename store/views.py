from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.

def home(request):
    return render(request,'store/index.html')
def collections(request):
    category = Category.objects.filter
    context = {'category': category}
    return render(request,'store/collections.html',context)

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'store/products/index.html',context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug)):
        if(Product.objects.filter(slug=prod_slug)):
            products = Product.objects.filter(slug=prod_slug).first()
            context = {'products': products}
        else:
            messages.warning(request, "No such products found")
            return redirect('collections')

    else:
        messages.warning(request, "No such category found")
        return redirect('collections')
    return render(request,'store/products/view.html',context)



