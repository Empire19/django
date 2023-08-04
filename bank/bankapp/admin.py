from django.contrib import admin
from bankapp.models import Bank
from bankapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list = ['eid', 'ename', 'email', 'dob', 'econtact', 'econtact2', 'qualification', 'doj', 'aadhar', 'pan', 'address', 'blood']
admin.site.register(Employee, EmployeeAdmin)



class BankAdmin(admin.ModelAdmin):
    list = ['eid', 'name', 'accno', 'ifsc', 'branch_name', 'city', 'state']
admin.site.register(Bank, BankAdmin)






