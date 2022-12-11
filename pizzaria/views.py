from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'pizzaria/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')

    context = {'all_pizzas':pizzas}                

    return render(request, 'pizzaria/pizzas.html', context)


def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    comment = Comment.objects.filter(pizza=p)     

    context = {'pizza':p, 'toppings':toppings, 'comment':comment}

    return render(request, 'pizzaria/pizza.html', context)

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzaria:pizza',pizza_id=pizza_id)
    
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzaria/new_comment.html', context)