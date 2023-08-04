from django import forms
from bankapp.models import Bank
from bankapp.models import Employee

# Create your forms here.
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'



class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'


