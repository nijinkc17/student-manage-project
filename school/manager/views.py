from django.shortcuts import render,redirect
from django.views import View
from.forms import RegForm,LogForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class Regview(View):
    def get(self,request):
        form=RegForm()
        context={}
        context["form"]=form
        return render(request,'reg.html',context)
    def post(self,request):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
        return render(request,'reg.html',{"form":form_data})
    
class LogView(View):
    def get(self,request):
        form=LogForm()
        return render(request,'log.html',{"form":form})
    def post(self,request):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get("user_name")
            pswd=form_data.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect('h')
            else:
                return redirect('home')
        return render(request,'log.html',{"form":form_data})
    
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('home')


