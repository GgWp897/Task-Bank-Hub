from django.shortcuts import render, redirect
from .models import Users, Statement
from django.contrib.auth import logout

def auth(requst):
    if requst.method=='POST':
        email=requst.POST['email']
        password=requst.POST['password']
        try:
            user=Users.objects.get(email=email, password=password)
        except Users.DoesNotExist:
            return redirect('auth')
        requst.session['user_id']=user.id
        return redirect('home')
    return render(requst, 'auth.html')


def registration(requst):
    if requst.method=='POST':
        email=requst.POST['email']
        password=requst.POST['password']
        if not Users.objects.filter(email=email).exists():
            user=Users(email=email, password=password)
            user.save()
            requst.session['user_id']=user.id
            return redirect('home')
        else:
            return redirect('registration')
    return render(requst, 'registration.html')

def home(requst):
    if 'user_id' in requst.session:
        user_id = requst.session.get('user_id')
        task = Statement.objects.filter(user_id=user_id)  
        if requst.method == 'POST':
            task = requst.POST['task']
            taskAll = requst.POST['taskAll']
            date = requst.POST['date']
            statement = Statement(task=task, taskAll=taskAll, date=date, user_id=user_id)
            statement.save()
        
        return render(requst, 'home.html', {'task': task})
    else:
        return redirect('auth')
    
def admin(requst):
    return redirect('admin')
    
def logoutxz(requst):
    logout(requst)
    return redirect('auth')


    
