from django.contrib import admin
from .models import Customer, Accounts, Cards 

# Register your models here.
# 1 register customer model
admin.site.register(Customer)

# 2. register the Accounts model class
admin.site.register(Accounts)

# 3. register the Cards model Class 
admin.site.register(Cards)

