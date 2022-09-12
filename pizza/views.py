from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import MultiplePizzaForm, PizzaForm
from django.forms import formset_factory

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    form = PizzaForm()
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form_saved = form.save()
            form_saved_pk = form_saved.id
            
            size = form.cleaned_data.get("size")
            topping_1 = form.cleaned_data.get("topping_1")
            topping_2 = form.cleaned_data.get("topping_2")
            return redirect("home")
    context = {
        'multiple_form': multiple_form,
        'form': form,
        
    }    
    return render(request, "pizza/order.html", context)    
            
def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
       number_of_pizzas = filled_multiple_pizza_form.cleaned_data.get('number')
       PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
       formset = PizzaFormSet()
    if request.method == "POST":
       filled_formset = PizzaFormSet(request.POST)
       if filled_formset.is_valid():
        for form in filled_formset:
            form.save()
    return render(request, 'pizza/pizzas.html', {'formset':formset})
