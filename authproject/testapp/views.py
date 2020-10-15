from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_exams_view(request):
    return render(request,'testapp/javaexams.html')

@login_required
def python_exams_view(request):
    return render(request,'testapp/pythonexams.html')

@login_required  
def aptitude_exams_view(request):
    return render(request,'testapp/aptitudeexams.html')
    

def logout_view(request):
    return render(request,'testapp/logout.html')

def sign_up_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()  # password will be saved in encrypted form
        # form.save() the password won't be saved in encrypted form, so we should not use this
        # if form.is_valid():
        #     form.save()   # otherway of encryption of password
        return HttpResponseRedirect('/accounts/login')

    return render(request,'testapp/signup.html',{'form':form})
