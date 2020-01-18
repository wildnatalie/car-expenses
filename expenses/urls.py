from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary, name='summary'),
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('expenses/new/', views.expense_new, name='expense_new'),
    path('expense/<int:pk>/edit/', views.expense_edit, name='expense_edit'),
    path('expense/<int:pk>/remove/', views.expense_remove, name='expense_remove')
]