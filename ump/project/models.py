from django.db import models


class CompanyInformation(models.Model):
    Name=models.CharField(max_length=255,null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Phone=models.CharField(max_length=100,null=True,blank=True)
    Fax=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Web=models.CharField(max_length=100,null=True,blank=True)
    Bin=models.CharField(max_length=255,null=True,blank=True)
    Logo=models.ImageField(upload_to='logo',null=True,blank=True)
    objects=models.Manager()


    def __str__(self):
        return self.Name


class Mrcreate(models.Model):
    Branch_name=models.CharField(max_length=255,null=True,blank=True)
    Mr_No=models.CharField(max_length=255,null=True,blank=True)
    Class=models.CharField(max_length=100,null=True,blank=True)
    Doc_No=models.CharField(max_length=255,null=True,blank=True)
    Date = models.DateField(null=True, blank=True)
    Insured_Name=models.CharField(max_length=1500,null=True,blank=True)
    Insured_Address=models.CharField(max_length=1500,null=True,blank=True)
    Bank_Name=models.CharField(max_length=1500,null=True,blank=True)
    Bank_Address=models.CharField(max_length=1500,null=True,blank=True)
    Premium=models.CharField(max_length=255,null=True,blank=True)
    Vat=models.CharField(max_length=255,null=True,blank=True)
    Stamp=models.CharField(max_length=255,null=True,blank=True)
    ServiceCharge=models.CharField(max_length=255,null=True,blank=True)
    Total_amount=models.CharField(max_length=255,null=True,blank=True)
    Mode_Of_Payment=models.CharField(max_length=255,null=True,blank=True)
    inword=models.CharField(max_length=1000,null=True,blank=True)
    objects=models.Manager()


    def __str__(self):
        return self.Mr_No






