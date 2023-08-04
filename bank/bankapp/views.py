from django.shortcuts import render, redirect
from bankapp.models import Bank, Employee
from bankapp.forms import BankForm, EmployeeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/show")  
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

        
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def show(request):
    employees = Employee.objects.all()
    banks = Bank.objects.all()
    return render(request, 'show.html', {'employees':employees,'banks':banks})



@login_required(login_url='login')
def emp(request):
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass    
    else:
        form = EmployeeForm()
    return render(request, 'index2.html', {'form':form})                


@login_required(login_url='login')
def bnk(request):
    if request.method =="POST":
        bankform = BankForm(request.POST)
        if bankform.is_valid():
            try:
                bankform.save()
                return redirect("/show")
            except:
                pass    
    else:
        bankform = BankForm()
    return render(request, 'index.html', {'bankform':bankform})                



    
    

@login_required(login_url='login')
def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit2.html', {'employee':employee})    

@login_required(login_url='login')
def change(request,id):
    bank = Bank.objects.get(id=id)
    return render(request, 'edit.html', {'bank':bank})    

@login_required(login_url='login')
def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit2.html', {'employee':employee})    



@login_required(login_url='login')
def modify(request,id):
    bank = Bank.objects.get(id=id)
    form = BankForm(request.POST, instance = bank)
    if form.is_valid():
        form.save()
        return redirect("/show")

    return render(request, 'edit.html', {'bank':bank})    

@login_required(login_url='login')
def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")  

@login_required(login_url='login')   
def destroy(request,id):
    bank = Bank.objects.get(id=id)
    bank.delete()
    return redirect("/show")  
