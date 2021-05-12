from import_export import resources
from .models import *

class BookResource(resources.ModelResource):

    class Meta:
        model = CompanyInformation
        fields='id,Name,Address,Phone,Fax,Email,Web,Bin,Logo'



class MrResource(resources.ModelResource):

    class Meta:
        model = Mrcreate
        fields='id,Branch_name,Mr_No,Class,Doc_No,Date,Insured_Name,Insured_Address,Bank_Name,Bank_Address,Premium,Vat,' \
               'Stamp,ServiceCharge,Total_amount,Mode_Of_Payment'