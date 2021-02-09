from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from webapp.forms import signupForm
from django.http import HttpResponseRedirect
from datetime import datetime
from webapp.models import Feedback


# Create your views here.
def home_page(request):
    return render(request,'myapp/home.html')

def logout(request):
    return render(request,'myapp/logout.html')

def registration_view(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        user=form.save(commit=True)
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,"myapp/registration.html",{'form':form})

def feedback(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        date=datetime.today()
        feedback=Feedback(name=name,email=email,message=message,date=date)
        feedback.save()
    return render(request,'myapp/feedback.html')


def show_feedback(request):
    data=Feedback.objects.all().filter().order_by('date')
    #   data = Feedback.objects.all()
    stu = {"info": data}
    print("OK")
    return render( request ,"myapp/show_feedback.html", stu)

