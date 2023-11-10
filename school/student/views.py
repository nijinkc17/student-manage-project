from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.

#authentication decorator

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please login...!")
            return redirect('home')
    return inner

@method_decorator(signin_required,name="dispatch")
class StudentListView(View):
    def get(self,request):
        data=Students.objects.all()
        return render(request,'index.html',{"std":data})
    
@method_decorator(signin_required,name="dispatch")
class StudentAddView(View):
    def get(self,request):
        form=StudentForm()
        return render(request,'addstud.html',{"form":form})
    def post(self,request):
        form_data=StudentForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('h')
        return render(request,'addstud.html',{"form":form_data})
    

@method_decorator(signin_required,name="dispatch")
class StudentDelView(View):
    def get(self,request,**kwargs):
        std_id=kwargs.get('sid')
        res=Students.objects.get(id=std_id)
        res.delete()
        return redirect('h')

@method_decorator(signin_required,name="dispatch")
class StudentEditView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get('sid')
        res=Students.objects.get(id=sid)
        data=StudentForm(instance=res)
        return render(request,'stdedit.html',{"d":data})
    def post(self,request,*args,**kwargs):
        sid=kwargs.get('sid')
        res=Students.objects.get(id=sid)
        form_data=StudentForm(data=request.POST,files=request.FILES,instance=res)
        if form_data.is_valid():
            form_data.save()
            return redirect('h')
        return render(request,'stdedit.html',{"d":form_data})
    
class ProfileView(View):
    def get(self,request):
        return render(request,'profile.html')
    
