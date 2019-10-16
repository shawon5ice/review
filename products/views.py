from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Product
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from . import  forms
from products.forms import User
from django.core import validators
# Create your views here.

def home(request):
  products = Product.objects.all()
  return render(request,'products/home.html',context={'products':products})

@login_required
def create(request):
  if request.method == 'POST':
    if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
      product = Product()
      product.title = request.POST['title']
      product.body = request.POST['body']
      if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
        product.url = request.POST['url']
      else:
        product.url = 'http://'+request.POST['url']
      
      product.icon = request.FILES['icon']
      product.image = request.FILES['image']
      product.pub_date = timezone.datetime.now()
      product.hunter = request.user
      product.save()
      return redirect('/product/'+str(product.id))
    else:
      return render(request,'products/create.html',{'error':'all fields are required'})

  return render(request,'products/create.html')


def detail(request,product_id):
  product = get_object_or_404(Product,pk=product_id)
  return render(request,'products/detail.html',{'product':product})

@login_required(login_url='/account/signup')
def upvote(request,product_id):
  if request.method == 'POST':
    product = get_object_or_404(Product,pk= product_id)
    product.votes_total+=1
    product.save()
    return redirect('/product/'+str(product.id))


def form_page(request):
  form = forms.my_form()
  if request.method == 'POST':
    form = forms.my_form(request.POST)
    if form.is_valid():
      print("Form validation success")
      print("Name: "+form.cleaned_data['name'])
      print("Email: "+form.cleaned_data['email'])
      print("Text: "+form.cleaned_data['text'])
  return render(request,'formpage.html',{'form':form})




def signup(request):
  form = User()
  if request.method =='POST':
    form = User(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return HttpResponse("hello")
    else:
      print("form input is not valid")
      return HttpResponse("hello")
  else:
    return render(request,'signup.html',{'form':form})