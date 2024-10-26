from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from Pizza_app.models import Register, Pizza
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.files.base import ContentFile



# Create your views here.
def home(request):
    pizzas = Pizza.objects.all()  # Fetch all pizza data
    return render(request, 'index.html', {'pizzas': pizzas})

def about(request):
    return render(request,'about.html')

def menu(request):
    # Fetch all pizza data
    pizzas = Pizza.objects.all()

    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        
        pizza_name = data.get("pizza_name")
        pizza_description = data.get("pizza_description")
        
        # Get list of selected types
        pizza_types = data.getlist("pizza_type")
        pizza_types_str = ", ".join(pizza_types)
        
        # Get list of selected sizes
        pizza_sizes = data.getlist("pizza_size")
        pizza_sizes_str = ", ".join(pizza_sizes)
        
        pizza_picture = files.get('pizza_picture')
        
        pizza = Pizza(
            name=pizza_name,
            description=pizza_description,
            type=pizza_types_str,
            size=pizza_sizes_str,
            pizza_picture=pizza_picture
        )
        pizza.save()
        
        return redirect('pizza')
    
    pizza =Pizza.objects.all()
    if request.GET.get("search_input"):
            pizza = pizza.filter(name__icontains=request.GET.get("search_input"))

    # Render the pizza_list.html template with pizza data
    # return render(request, 'pizza.html', {'pizzas': pizzas})

    return render(request,'menu.html', {'pizzas': pizzas})

def register(request):
    if request.method == 'POST':
        data = request.POST

        # Get form data
        name = data.get("full_name")
        email = data.get("email_id")
        paswd = data.get("pass")
        conf_paswd = data.get("conf_pass")

        # Check if passwords match
        if paswd != conf_paswd:
            return HttpResponse("Passwords do not match.")
        
        signup = Register(
            name=name,
            email=email,
            paswd=paswd,
            conf_paswd=conf_paswd
        )
        signup.save()

        # Redirect the user from signup to login page
        return redirect('home')  # Ensure the name matches your URL pattern name

    # Render the register.html template
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get("email_id")
        passwd = data.get("pass")
        
        # Authenticate using the correct parameters
        user = authenticate(request, username=email, password=passwd)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Enter a valid email and password")

    return render(request, 'login.html')

def pizza_list(request):
    # Fetch all pizza data
    pizzas = Pizza.objects.all()

    if request.method == 'POST':
        data = request.POST
        files = request.FILES
        
        pizza_name = data.get("pizza_name")
        pizza_description = data.get("pizza_description")
        
        # Get list of selected types
        pizza_types = data.getlist("pizza_type")
        pizza_types_str = ", ".join(pizza_types)
        
        # Get list of selected sizes
        pizza_sizes = data.getlist("pizza_size")
        pizza_sizes_str = ", ".join(pizza_sizes)
        
        pizza_picture = files.get('pizza_picture')
        
        pizza = Pizza(
            name=pizza_name,
            description=pizza_description,
            type=pizza_types_str,
            size=pizza_sizes_str,
            pizza_picture=pizza_picture
        )
        pizza.save()
        
        return redirect('pizza')
    
    pizza =Pizza.objects.all()
    if request.GET.get("search_input"):
            pizza = pizza.filter(name__icontains=request.GET.get("search_input"))

    # Render the pizza_list.html template with pizza data
    return render(request, 'pizza.html', {'pizzas': pizzas})
    # return render(request, 'pizza.html', {'pizzas': pizzas})


def pizza_edit(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    
    if request.method == 'POST':
        pizza.name = request.POST.get('pizza_name')
        pizza.description = request.POST.get('pizza_description')
        
        # Handle multiple types and sizes
        pizza_types = request.POST.getlist('pizza_type')
        pizza_types_str = ", ".join(pizza_types)
        pizza.type = pizza_types_str
        
        pizza_sizes = request.POST.getlist('pizza_size')
        pizza_sizes_str = ", ".join(pizza_sizes)
        pizza.size = pizza_sizes_str

        if 'pizza_picture' in request.FILES:
            pizza.pizza_picture = request.FILES['pizza_picture']
        
        pizza.save()
        return redirect('pizza')
    
    return render(request, 'pizza_edit.html', {'pizza': pizza})

def pizza_delete(request, id):
    pizza = get_object_or_404(Pizza, id=id)
    pizza.delete()
    return redirect('pizza')

        

