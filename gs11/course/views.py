from django.shortcuts import render

# Create your views here.

def learn_django(request):
    cname ='Django'
    duration = '4 months'
    seats = 10
    django_details = {'nm':cname,'du':duration,'st':seats}
    # coursename = {'cname':'Zahid'}
    return render(request,'course/course1.html',django_details)

def learn_python(request):
    return render(request,'course/course2.html')
    