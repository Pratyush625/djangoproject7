To run locally, do the usual:

#. Create a Python 3.6 virtualenv Django 1.11 version installed

#. Create project projectname 
   
    django-admin startproject authproject

#. Go to the project dir 
   
    cd authproject

#. Create application inside main project directory 

    py manage.py startapp testapp

#. Configure the templatefile and staticfile inside settings.py 

#.Create template folder and static folder(if required), inside static folder create css folder and image folder, insert the required images, Here sqlite used as default database


#. Inside template folder we have use multiple template files

#. base.html
            

              <!DOCTYPE html>
              <html lang="en">
              <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
               <title>Document</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
            </head>
           <body>
           <nav class="navbar navbar-default navbar-inverse">
           <div class="container">
             <div  class="navbar-header">
                <a class="navbar-brand" href="/">Home</a>
             </div>
             <ul class="nav navbar-nav">
                 <li><a href="/java">Java Exams</a></li>
                 <li><a href="/python">Python Exams</a></li>
                 <li><a href="/aptitude">Aptitude Exams</a></li>

             </ul>
             <ul class="nav navbar-nav navbar-right">
                <li><a href="/signup">SignUp</a></li>
                <li><a href="/accounts/login">LogIn</a></li>
                <li><a href="/accounts/logout">Logout</a></li>

            </ul>
           </div>
           </nav>
           {%block body_block%}

           {%endblock%}
           </body>
           </html>

#. home.html
        

        <!DOCTYPE html>
        {% extends 'testapp/base.html'%}
        {%block body_block%}
        <div class="jumbotron">
            
            <div class="container">
                <h1>Welcome to Competive Exams</h1>
            <h2>`Rules:</h2>
            <ul>
                <li>Rule-1: You should write only one exam per day</li>
            </ul>

            </div>
   

           </div>
           {%endblock%}

#. Create link for javaexams.html

      <!DOCTYPE html>
      {% extends 'testapp/base.html'%}
      {%block body_block%}
        <div class="jumbotron">
            
            <div class="container">
                <h1>Welcome to Java Exams</h1>
           
            </div>
          </div>
         {%endblock%}
#. Create link for pythonexams.html

      <!DOCTYPE html>
      {% extends 'testapp/base.html'%}
      {%block body_block%}
        <div class="jumbotron">
            
            <div class="container">
                <h1>Welcome to Python Exams</h1>
           
            </div>
          </div>
         {%endblock%}

#. Create link for aptitudeexams.html

      <!DOCTYPE html>
      {% extends 'testapp/base.html'%}
      {%block body_block%}
        <div class="jumbotron">
            
            <div class="container">
                <h1>Welcome to Aptitude Exams</h1>
           
            </div>
          </div>
         {%endblock%}
#. Auth module require a table called user for that we have create a table in DB

         py manage.py migrate  

#. Create superuser to connect with database 

    py manage.py createsuperuser

#. Add another user in admin page with username and password
     
     Password will be come as encrypted or hashable form
     algorithm: pbkdf2_sha256
     iterations: 36000

#. We have to authenticate all exams by specific user by using decorator login_required inside view.py

#. Define view function inside views.py 

       from django.shortcuts import render
       from django.contrib.auth.decorators import login_required
       from testapp.forms import SignUpForm
       from django.http import HttpResponseRedirect


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
               user.save() -->password will be saved in encrypted form
               form.save()  -->password won't be saved in encrypted form, so we should not use this
               return HttpResponseRedirect('/accounts/login')
           return render(request,'testapp/signup.html',{'form',form})

#. We have to create a folder called registration inside templates, create login.html inside registration folder

#. Inside Login.html(auth application is responsible to display the login page)
    
    <!DOCTYPE html>
    {% extends 'testapp/base.html'%}
      {%block body_block%}
      <div class="container" align='center'>
        <h1>Login to write Exams..</h1>
        <form method="post">
            {{form.as_p}}
            {%csrf_token%}
            <button type="submit">LogIn</button>
        </form>
        </div>
      {%endblock%}

#. We have to specify after login on which page it should be rendered.
   At settings.py we have to define
     
     LOGIN_REDIRECT_URL='/'

#. Implement logout(inside base.py)
       
       "/accounts/logout"
       
    After logout we have to render to otherpage like logout.html

#. Create logout view inside views.py

#. logout.html
    

      <!DOCTYPE html>
      {% extends 'testapp/base.html'%}
      {%block body_block%}
        <div class="jumbotron">
            
            <div class="container">
                <h1>Logged Out</h1>
                <p>Thanks for spending some quality time with the Web site today.</p>
                <h2>Please Login again</h2>
                 <a href="/accounts/login" class="btn btn-primary btn-success">Login</a>

            </div>
         </div>
        {%endblock%}

#. Also have to mentioned inside setting.py
       

       LOGOUT_REDIRECT_URL='/logout'
        
#. Implement signup form(Display form based on User Model)

#. Create forms.py inside builtin testapp, inside that create UserForm
        

        from django import from
        from django.contrib.auth.models import User

        class SignUpForm(forms.ModelForm):
             class Meta:
             model=User
                fields=['username','password','email','first_name','last_name']

#. Create signup.html inside templates testapp
      
      <!DOCTYPE html>
      {% extends 'testapp/base.html'%}
      {%block body_block%}
         <div class="container">
             <h1>SignUp to write Exams</h1>
             <form method="POST">
                {{form.as_p}}
                {%csrf_token%}
                <input type="submit" class="btn btn-primary" value="SignUp">
             </form>
            </div>
          {%endblock%}

#. Create a signup_view inside views.py

#. Add signup url inside base.py

#. We can create multiple user by signup this page
        
    Username:                              150 characters or fewer. Letters, digits and @/./+/-/_ only.
    
    Password: 

    Email address: 

    First name: 

    Last name: 
#. How to use your own hashable algorithm for password. For that we need to install these:-
       

       pip install bcrypt
       pip install django[argon2]

#. Inside settings.py we need to defined, acc. to the order it will implemented

      PASSWORD_HASHERS=[
          'django.contrib.auth.hashers.Argon2PasswordHasher',
          'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
          'django.contrib.auth.hashers.BCryptPasswordHasher',
          'django.contrib.auth.hashers.PBKDF2PasswordHasher',
          'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',

      ]

#. Define view function inside urls.py

         from django.conf.urls import url,include
         from django.contrib import admin
        from testapp import views
        urlpatterns = [
         url(r'^admin/', admin.site.urls),
         url(r'^$', views.home_page_view),
         url(r'^java/', views.java_exams_view),
         url(r'^python/', views.python_exams_view),
         url(r'^aptitude/', views.aptitude_exams_view),
         url(r'^logout/', views.logout_view),
        url(r'^signup/', views.sign_up_view),
        url(r'^accounts/', include('django.contrib.auth.urls')),
        ]

#. To run server 

    py manage.py runserver
