from django.shortcuts import render
from .forms import form1, Registration
from .models import model1
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):
    res = False
    if request.method == 'POST':
        f = Registration(request.POST)
        if f.is_valid():
            v = f.save()
            v.set_password(v.password)
            v.save()
            res = True
            context = {'res':res}
            return render(request,'login.html',context)
    
    else:
        f=Registration()
        return render(request,'register.html',{'res':res,'form':f})
    return render(request,'home.html')


def log_in(request):
    if request.method=='POST':
        userName=request.POST.get('name')
        passWord=request.POST.get('password')
        user = authenticate(username=userName,password=passWord)
        if user:
            login(request,user)
            return render(request,'home.html')
        return HttpResponse('ERROR: Entered credentials are incorrect')
    return render(request,'login.html')
    
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('app:index'))

def home(request):
    return render(request,"home.html")


def display_form(request):
    form = form1()       
    print(form1())
    if request.method == 'POST':
        form = form1(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('app:detail'))
    return render(request,"display_form.html",{'form':form})

def display_details(request):
    mod = model1.objects.all()
    return render(request,'display_details.html',{"model":mod})

def display_details_individuals(request,id):
    mod = model1.objects.get(id=id)
    model = model1.objects.all()

    return render(request,'display_details.html',{"mode":mod,'model':model})

def delete_details(request,id):
    store = get_object_or_404(model1,id=id)
    if request.method == 'POST':
        store.delete()
        return HttpResponseRedirect(reverse('app:details'))
    return render(request,"delete_details.html",{'store':store})

def update_details(request,id):
    store = get_object_or_404(model1,id=id)
    form = form1(request.POST or None,instance = store)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('app:detail'))
    return render(request,'update_details.html',{"update_form":form,"store":store})
