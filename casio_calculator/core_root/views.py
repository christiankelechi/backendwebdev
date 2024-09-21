from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from core_root.forms import RegisterForm
# Create your views here.
def index(request):
    current_context={"current_value":"","number_seven":"7","number_eight":"8"}
    
    if request.method=='POST':
        
        if request.POST['number_index']=='8':
            print("is eight")
        if request.POST['number_index']=='7':
            print("is seven")
            current_context['current_value']=current_context['number_seven']
            
                
            with open("core_root/values.txt","a") as fileObject:
                fileObject.write(str(current_context['number_seven']))
                
            with open("core_root/values.txt","r") as fileObjectRead:
                current_number_value=fileObjectRead.read()
            current_context['current_value']=current_number_value
            
            if len(current_context['current_value'])<len(current_number_value):
                with open("core_root/values.txt","w") as fileObject:
            
                    fileObject.write(str(current_context['current_value']))
                
            
        
        
    return render(request,"index.html",current_context)



def members(request):
    return HttpResponse("Hello world!")
from django.shortcuts import render, redirect
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)  # Use request.POST for form data
        if form.is_valid():
            # Save the new user (you might need to create the user manually if not using UserCreationForm)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Set the password
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  # Redirect to the login page (or wherever appropriate)
    else:
        form = RegisterForm()  # Create a new form instance for GET request

    context = {"form": form}
    return render(request, 'authentication/signup.html', context)
