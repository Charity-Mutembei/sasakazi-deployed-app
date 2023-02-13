from django import forms
from django.forms import ModelForm
from .models import Customer, Accounts, Cards


#  create an accounts form
class AccountForm(ModelForm):
    class Meta:
        model = Accounts
        fields = (
            'account_holder', 'account_type', 'account_balance'
        )


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'