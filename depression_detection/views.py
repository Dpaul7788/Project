from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings

from ML import emotions_detection
from datetime import datetime
import re


def first(request):
    return render(request,'index.html')



def index(request):
    return render(request,'index.html')


def reg(request):
     return render(request,'register.html')

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        Address=request.POST.get('Address')
        password=request.POST.get('password')
        x=patient_tbl(name=name,email=email,phone=phone,Address=Address,password=password)
        x.save()
    return render(request,'index.html',{'message':"Successfully Registred"})

def docc(request):
     return render(request,'psychiatrist.html')


def doctor(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        specialization=request.POST.get('specialization')  
        clinicname=request.POST.get('clinic_name')  
        place=request.POST.get('place')
        time=request.POST.get('timing')
        password=request.POST.get('password')
        exper=request.POST.get('year_of_experience')
        y=psychiatrist_tbl(name=name,email=email,specialization=specialization,clinic_name=clinicname,place=place,timing=time,password=password,year_of_experience=exper)
        y.save()
    return render(request,'index.html',{'message':"Successfully Added"})   

def guss(request):
     return render(request,'guestuser.html')


def guest(request):
    if request.method=='POST':
        name=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        y=guestuser_tbl(uname=name,email=email,password=password)
        y.save()
    return render(request,'index.html',{'message':"Successfully Registred"})   


def viewuser(request):
    y=patient_tbl.objects.all()
    return render(request,'viewuser.html',{'x':y})


def viewappoint(request):
     sel=consultation_tbl.objects.filter(did=request.session['did'])
     user3=patient_tbl.objects.all()
     for i in sel:
        for j in user3:
            if str(i.user_id)==str(j.id):
                    i.user_id=j.name
     return render(request,'viewappoint.html',{'x':sel})

def viewpsychiatrist(request):
    y=psychiatrist_tbl.objects.all()
    return render(request,'viewpsychiatrist.html',{'x':y})

def viewguestuser(request):
    y=guestuser_tbl.objects.all()
    return render(request,'viewguestuser.html',{'x':y})


def login(request):
     return render(request,'login.html')


def addlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=='admin@gmail.com'and password=='admin':
            request.session['admin_id']=email
            return render(request,'index.html',{'message':"Successfully Logined"})
    elif psychiatrist_tbl.objects.filter(email=email,password=password).exists():
                x=psychiatrist_tbl.objects.get(email=email,password=password)
                request.session['did']=x.id
                return render(request,'index.html',{'message':"Successfully Logined"})
    elif patient_tbl.objects.filter(email=email,password=password).exists():
                y=patient_tbl.objects.get(email=email,password=password)
                request.session['uid']=y.id
                return render(request,'index.html',{'message':"Successfully Logined"})
    

    elif guestuser_tbl.objects.filter(email=email,password=password).exists():
                y=guestuser_tbl.objects.get(email=email,password=password)
                request.session['gid']=y.id
                return render(request,'index.html')
    else:
        return render(request,'login.html')

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
          del request.session[key]
    return redirect(index)


'''def userdoctor(request):
      y=psychiatrist_tbl.objects.all()
      return render(request,'book.html',{'x':y})'''
from django.shortcuts import render
from .models import psychiatrist_tbl

def userdoctor(request):
    query = request.GET.get('q')
    if query:
        y = psychiatrist_tbl.objects.filter(place__icontains=query)
    else:
        y = psychiatrist_tbl.objects.all()
    return render(request, 'book.html', {'x': y})

def bookuser(request,id):
    sel=psychiatrist_tbl.objects.get(id=id)
    return render(request,'Booking.html',{'result':sel})



def addbook(request):
    if request.method=="POST":
          did=request.POST.get('did')
          date=request.POST.get('date')
          description=request.POST.get('description')
          timing=request.POST.get('timing')
          clinic_name=request.POST.get('clinic_name')
          myfile=request.FILES['documents']
          fs=FileSystemStorage()
          filename=fs.save(myfile.name,myfile)
          ins=consultation_tbl(did=did,date=date,description=description,timing=timing,clinic_name=clinic_name,documents=filename,user_id=request.session['uid'])
          ins.save()
    return render(request,'index.html',{"message":"Succssfully Booked"})      
          


def press(request,id):
     sel=consultation_tbl.objects.get(id=id)
     sel1=med_tbl.objects.all()
     return render(request,'presc.html',{'result':sel,'res':sel1})





def addpres(request, id):
    print(f"Received id: {id}")  
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        date = request.POST.get('date')
        description = request.POST.get('description')
        timing = request.POST.get('timing')
        clinic_name = request.POST.get('clinic_name')
        filename = request.POST.get('documents')
        med_name = request.POST.get('med_name')
        prescription = request.POST.get('prescription')
        timingss = request.POST.get('timingss')
        notes = request.POST.get('notes')
        
        ins = consultation_tbl(
            user_id=user_id,
            date=date,
            description=description,
            timing=timing,
            clinic_name=clinic_name,
            documents=filename,
            medicines=med_name,
            prescription=prescription,
            timingss=timingss,
            notes=notes,
            did=request.session['did'],
            id=id
        )
        ins.save()
    return render(request, 'index.html')



def faq(request): 
    return render(request, 'faq.html')  


def data_submit(request):
    if request.method == "POST":
        q1 = int(request.POST.get('a', 0))
        q2 = int(request.POST.get('b', 0))
        q3 = int(request.POST.get('c', 0))
        q4 = int(request.POST.get('d', 0))
        q5 = int(request.POST.get('e', 0))
        q6 = int(request.POST.get('f', 0))
        q7 = int(request.POST.get('g', 0))
        q8 = int(request.POST.get('h', 0))
        q9 = int(request.POST.get('i', 0))
        q10 = int(request.POST.get('j', 0))

        total_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10

        stress_level = ""
        if total_score <= 2:
            stress_level = "Low Depression :  You might be experiencing some everyday stress, but it's likely manageable"
        elif total_score <= 5:
            stress_level = "Moderate drepression : You might be experiencing moderate stress "
        else:
            stress_level = "High Depression : You might be experiencing significant stress that requires additional support."

        return render(request, 'faq.html', {'status': 'Successfully Added', 'stress_level': stress_level})

    return render(request, 'faq.html')



def feed(request):
    return render(request,'feed.html')


'''def addfeed(request):
    if request.method=="POST":
          description=request.POST.get('description')
          ins=feedback_tbl(userid=request.session['uid'],description=description)
          ins.save()
    return render(request,'index.html',{"message":"Successfully Added"})'''
def addfeed(request):
    if request.method == "POST":
        description = request.POST.get('description')
        if not re.match("^[a-zA-Z\s]+$", description):
            return render(request, 'feedback_template.html', {'msg': 'Please enter alphabets only.'})

        # Assuming you have a Feedback model with a description field
        feedback = feedback_tbl(description=description,userid=request.session['uid'])
        feedback.save()
          # Replace with your success URL or view name

    return render(request,'index.html',{"message":"Successfully Added"})


def viewfeed(request):
    sel=feedback_tbl.objects.all()
    user= patient_tbl.objects.all()
    for i in sel:
            for j in user:
                if str(i.userid)==str(j.id):
                    i.userid=j.name
    return render(request,'viewfeed.html',{'x':sel})
          
def viewpres(request):
     sel=consultation_tbl.objects.filter(user_id=request.session['uid'])
     return render(request,'viewpres.html',{'result':sel})

def depression(request):
    emotion, stress = emotions_detection.predict()
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    sel = result_tbl(emotion = emotion, result = stress, uid = request.session['uid'],date_time=formatted_datetime)
    sel.save()
    return redirect(u_result)

def u_result(request):
    sel = result_tbl.objects.filter(uid = request.session['uid'])
    return render(request, 'view_result.html', {'result':sel})




def viewappointadmin(request):
     sel=consultation_tbl.objects.all()
     return render(request,'viewappointadmin.html',{'x':sel})



def pay(request,id):
     sel=consultation_tbl.objects.get(id=id)
     return render(request,'appay.html',{'result':sel})



def addpay(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
   
        clinic_name = request.POST.get('clinic_name')
        #did = request.POST.get('did')
        amount = request.POST.get('amount')
        
        ins = fee_tbl(
            user_id=user_id,
         
            clinic_name=clinic_name,
            did=request.session['did'],
            amount=amount,
            
            
        )
        ins.save()
    return render(request, 'index.html',{'message':"Successfully Added"})



def viewpays(request):
    sel=fee_tbl.objects.filter(user_id=request.session['uid'])
    user= psychiatrist_tbl.objects.all()
    for i in sel:
            for j in user:
                if str(i.did)==str(j.id):
                    i.did=j.name
    return render(request,'viewpays.html',{'x':sel})

def paid(request,id):
     sel=fee_tbl.objects.get(id=id)
     return render(request,'userpay.html',{'result':sel})

def addpayuser(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
   
        clinic_name = request.POST.get('clinic_name')
        did = request.POST.get('did')
        amount = request.POST.get('amount')
        cvv = request.POST.get('cvv')
        date = request.POST.get('date')
        card_name = request.POST.get('card_name')
        card_no = request.POST.get('card_no')
        
        ins = payment_tbl(
            user_id=user_id,
         
            clinic_name=clinic_name,
            did=did,
            amount=amount,
            cvv=cvv,
            card_name=card_name,
            card_no=card_no,
            date=date,
            
            
        )
        ins.save()
    return render(request, 'index.html')

def payss(request):
    sel=payment_tbl.objects.all()
    user= psychiatrist_tbl.objects.all()
    user3= patient_tbl.objects.all()
    for i in sel:
            for j in user:
                if str(i.did)==str(j.id):
                    i.did=j.name

    for i in sel:
        for j in user3:
            if str(i.user_id)==str(j.id):
                    i.user_id=j.name
    return render(request,'payss.html',{'x':sel})



def inss(request):
     return render(request,'inss.html')




def medii(request):
     return render(request,'med.html')



def addmed(request):
    if request.method=="POST":
        med_name=request.POST.get('med_name')
        timingss=request.POST.get('timingss')
        notes=request.POST.get('notes')
        ins=med_tbl(med_name=med_name,timingss=timingss,notes=notes)
        ins.save()
    return render(request,'index.html',{'message':"successfully Added"})    




def ress(request):
    sel=result_tbl.objects.all()
    user=patient_tbl.objects.all()
    for i in sel:
            for j in user:
                if str(i.uid)==str(j.id):
                    i.uid=j.name
    return render(request,'viewresult.html',{'result':sel})