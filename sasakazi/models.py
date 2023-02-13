from django.db import models

# Create your models here.

# Need #1
# We need model classes - customer, account and card
# The customer may have many bank accounts, hence a relationship
# exists between the customer and the account(s). 
# Have a foreign key in the account class to link the 
# database - user/customer_id used. 

class Customer (models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('Email Address', blank=True, null=False)
    phone_number = models.CharField(max_length=10, null=False, blank=True)
    age_number = models.IntegerField(null=False, blank=False, default='18')
    location = models.CharField(max_length=100, blank=True, null=False)
    
    # chose to return the name of the customer 
    def __str__(self):
        return f'{self.first_name}, {self.middle_name}, {self.last_name}'

    
    # chose to save to the database
    




#  the accounts should/could be debit or credit accounts. 
# hence the account class should have a model with 
# specificity on what type the card is. 
# Have a balance, interest rate, etc information

class Accounts(models.Model):
    
    Account = (
        ('Debit', "Debit Account"), 
        ('Credit', "Credit Account"),
    )
      

    account_holder = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=30, choices=Account,  default='Debit')
    account_balance = models.IntegerField(null=False, blank=False)


    # chose to return the type of the account when saving
    def __str__(self):
        return f'{self.account_type}'



# the card class considers - a client can have more than
# more than one card number - take a number for each card
# have a foreign key linking the accounts and card models
# having each card reflect an amount linked to the account. 

class Cards(models.Model):
    card_name = models.CharField(max_length=100, null=False, blank=False)
    client_account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    card_number = models.IntegerField(max_length=100, blank=False, null=False)
    card_expiry = models.DateField(null=False, blank=False)



    def __str__(self):
        # chose to return the name of the card
        return f'{self.card_name}'
