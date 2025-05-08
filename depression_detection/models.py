from django.db import models



class patient_tbl(models.Model):
    name=models.CharField(max_length=150)
    phone=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    Address=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    

class psychiatrist_tbl(models.Model):
    name=models.CharField(max_length=150)
    specialization=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    clinic_name=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    timing=models.CharField(max_length=120)
    place=models.CharField(max_length=120)
    year_of_experience=models.CharField(max_length=120)

class guestuser_tbl(models.Model):
    uname=models.CharField(max_length=150)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=120)

class consultation_tbl(models.Model):
    did=models.CharField(max_length=150)
    date=models.CharField(max_length=120)
    description=models.CharField(max_length=150)
    documents=models.CharField(max_length=120)
    medicines=models.CharField(max_length=120)
    prescription=models.CharField(max_length=120)
    user_id=models.CharField(max_length=120)
    timing=models.CharField(max_length=120)
    clinic_name=models.CharField(max_length=120)
    timingss=models.CharField(max_length=120)
    notes=models.CharField(max_length=120)

class result_tbl(models.Model):
     emotion=models.CharField(max_length=120)
     result=models.CharField(max_length=120)  
     uid=models.CharField(max_length=120)
     date_time=models.CharField(max_length=120)

class payment_tbl(models.Model):
    userid=models.CharField(max_length=120)
    did=models.CharField(max_length=120)
    amount=models.CharField(max_length=120)
    date=models.CharField(max_length=120)

class feedback_tbl(models.Model):
    userid=models.CharField(max_length=120)
    description=models.CharField(max_length=120)




class fee_tbl(models.Model):
    did=models.CharField(max_length=150)
    
    user_id=models.CharField(max_length=120)
    amount=models.CharField(max_length=120)
    clinic_name=models.CharField(max_length=120)

class payment_tbl(models.Model):
    did=models.CharField(max_length=150)
    date=models.CharField(max_length=120)
    card_name=models.CharField(max_length=150)
    card_no=models.CharField(max_length=120)
    cvv=models.CharField(max_length=120)
    user_id=models.CharField(max_length=120)
    amount=models.CharField(max_length=120)
    clinic_name=models.CharField(max_length=120)



class med_tbl(models.Model):
    med_name=models.CharField(max_length=150)
    
    timingss=models.CharField(max_length=120)
    notes=models.CharField(max_length=120)
