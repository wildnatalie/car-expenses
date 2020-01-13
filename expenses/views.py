from django.shortcuts import render
from .models import Expense
from django.db.models import Sum

# Create your views here.

def summary(request):
    total_sum = Expense.objects.aggregate(Sum('amount'))
    return render(request, 'expenses/summary.html', {'total_sum': total_sum['amount__sum']})