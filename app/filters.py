import django_filters
from django import forms
from django_filters import CharFilter, filters

from .models import *


class ProductFilter(django_filters.FilterSet):
    ProductName = CharFilter(field_name='ProductName', label='', lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Title ', 'class': 'form-control'}))


    class Meta:
        model = product
        fields = ('ProductName', )


class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', )

    class Meta:
        model = Customer
        fields = ('name',)




class OrderFilter(django_filters.FilterSet):
    id = CharFilter(field_name='id', label='Order ID', lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Order ID ', 'class': 'form-control'}))

    class Meta:
        model = Order
        fields = ('id',)


