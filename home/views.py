from django.shortcuts import render,HttpResponse,redirect

from home.models import Product
from home.form import ProductForm
# Create your views here.

def index(request):
    product_list=Product.objects.all()
    return render(request,'index.html',{'products':product_list})

def upload(request):

    upload=ProductForm()

    if request.method == 'POST':
        upload=ProductForm(request.POST,request.FILES) 

        if(upload.is_valid()):
            upload.save()

            return redirect('index')

        else:
            return HttpResponse("<h1> Go back and fill correct data</h1>") 

    else:              
        return render(request,'upload.html',{'form':upload})

def update(request,id):
    product_id=int(id)

    try:
        product_selected=Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('index')

    product_form=ProductForm(request.POST or None,instance=product_selected)

    if product_form.is_valid():
        product_form.save()
        return redirect('index')
    return render(request,'upload.html',{'form':product_form})    


def delete(request,id):
    #return HttpResponse("<h1> Delete is called</h1>")
    product_id=int(id)

    try:
        product_selected=Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return redirect('index')
    #using QuerySet API
    product_selected.delete()
    return redirect('index')    



