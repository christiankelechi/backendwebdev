from django.shortcuts import render
def index(request):
    with open("incrementer/current_value.txt","r") as originalvalue:
        current_value=int(str(originalvalue.read()))
    
    if request.method=='POST':
        with open("incrementer/current_value.txt","r") as originalvalue:
            current_value=int(str(originalvalue.read()))
        current_value+=1
        
        with open("incrementer/current_value.txt","w") as orginal_value:
            orginal_value.write(str(current_value))
        
        return render(request,"index.html",{"current_value":current_value})
    return render(request,"index.html",{"current_value":current_value})

from django.shortcuts import render

def process_decrease(request):
    # Read the current value from the file
    with open("incrementer/current_value.txt", "r") as original_value:
        current_value = int(original_value.read())

    # Check if the request method is POST
    if request.method == 'POST':
        # Decrease the value
        current_value -= 1

        # Write the updated value back to the file
        with open("incrementer/current_value.txt", "w") as original_value:
            original_value.write(str(current_value))

        # Render the template with the updated value
        return render(request, "process.html", {"current_value": current_value})

    # If the method is not POST, render the current value as it is
    return render(request, "process.html", {"current_value": current_value})
