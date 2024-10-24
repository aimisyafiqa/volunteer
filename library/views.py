from django.shortcuts import render, redirect, get_object_or_404
from library.models import Student, Event, Volunteer
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
#welcomepage
def index(request):
    return render (request, 'index.html')

# Home page view
def homepage(request):
    return render(request, "homepage.html")

# login view
def login(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')
        password = request.POST.get('password')
        try:
            student = Student.objects.get(studentid=student_id)
            if student.password == password:
                request.session['student_id']=student.studentid
                return redirect('homepage')  
            else:
                return render(request, 'login.html', {'message': 'Invalid password'})
        except Student.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid password'})
    return render(request, "login.html")
#signup view
def signup(request):
    if request.method == 'POST':
        name= request.POST['name']  
        id= request.POST['id']
        psw= request.POST['psw']
        email=request.POST['email']
        phone=request.POST['phone']
        data=Student(studentid=id, password=psw, studentname=name, phone=phone, email=email)
        data.save()
        dict = {
            'message': 'Data Succesfully Save',
        }
        return redirect('login') 
    else:
        dict ={
            'message': ''
        }
    return render(request, "signup.html", dict)

#my event view
def event(request):
    student_id = request.session.get('student_id')
    if student_id:
        vdata=Volunteer.objects.select_related('eventid','studentid').filter(studentid_id=student_id)
        context = {
            'vdata':vdata
                   }
    return render (request, 'event.html', context)

#my search event view
def search_event(request):
    if request.method =='GET':
        ename= request.GET.get('ename')
        if ename:
            data = Event.objects.filter(eventname=ename.upper())
        else:
            data = None

        context = {
            'data2': data
        }
        return render(request, "search_event.html", context)
    return render(request, 'search_event.html')

#my join event view
def join_event(request, eventid):
    student_id = request.session.get('student_id')  # Assuming student_id is stored in session
    event = get_object_or_404(Event, eventid=eventid)

    # Check if the student is already joined
    is_joined = Volunteer.objects.filter(studentid=student_id, eventid=eventid).exists()
    
    if not is_joined:
        # Create a new Volunteer entry if not already joined
        Volunteer.objects.create(studentid_id=student_id, eventid=event)

    return redirect('event')  # Redirect to the profile or another appropriate page

#my profile view
def myprofile(request):
    student_id = request.session.get('student_id')
    if student_id:
        data = Student.objects.get(studentid=student_id)
        context = {'data': data}
    return render(request, 'myprofile.html', context)

#update student view
def update_student(request, studentid):
    data = Student.objects.get(studentid=studentid)
    context = {
        'data1': data
    }
    return render(request, "update_student.html", context)

#save update student view
def save_update_student(request, studentid):
    sname = request.POST['name']
    password = request.POST['psw']
    mail = request.POST['email']
    nophone = request.POST['phone']

    # Fetch the existing student record and update its fields
    data = Student.objects.get(studentid=studentid)
    data.studentname = sname
    data.password = password
    data.phone = nophone
    data.email = mail
    # Save the updated record
    data.save()
    return HttpResponseRedirect(reverse("myprofile"))

#delete event
def delete_event(request, volunteerid):
    data=Volunteer.objects.get(volunteerid=volunteerid)
    data.delete()
    return HttpResponseRedirect(reverse('event'))

#user logout
def logout(request):
    return render (request, 'logout.html')
