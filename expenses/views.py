from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.db.models import Sum
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def summary(request):
    total_sum = Expense.objects.aggregate(Sum('amount'))
    return render(request, 'expenses/summary.html', {'total_sum': total_sum['amount__sum']})

def expenses_list(request):
    total_sum = Expense.objects.aggregate(Sum('amount'))
    expenses = Expense.objects.order_by('-expense_date')
    return render(request, 'expenses/expenses_list.html', {'total_sum': total_sum['amount__sum'], 'expenses': expenses})

@login_required
def expense_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save()
            return redirect('expenses_list')
    else:
        form = ExpenseForm()
    
    return render(request, 'expenses/expense_edit.html', {'form': form})

@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save()
            return redirect('expenses_list')
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'expenses/expense_edit.html', {'form': form})

@login_required
def expense_remove(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expenses_list')