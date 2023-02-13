from rest_framework import serializers 
from .models import Customer, Accounts, Cards 

# let us change our data into JSON format for the API
class CustomerSerializer(serializers.ModelSerializer):

    # first_name = serializers.CharField(max_length=30)
    # middle_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)

    class Meta:
        model = Customer
        fields = '__all__'

class AccountsSerializer(serializers.ModelSerializer):

    # account_holder = serializers.ForeignKey(Customer, on_delete=models.CASCADE)
    # account_type = serializers.CharField(max_length=30, choices=Account,  default='Debit')
    # account_balance = serializers.IntegerField(null=False, blank=False)

    class Meta:
        model = Accounts 
        fields = '__all__'

class CardsSerializer(serializers.ModelSerializer):

    # card_name = serializers.CharField(max_length=100, null=False, blank=False)
    # client_account = serializers.ForeignKey(Accounts, on_delete=models.CASCADE)
    # card_number = serializers.IntegerField(max_length=100, blank=False, null=False)
    # card_expiry = serializers.DateField(null=False, blank=False)

    class Meta:
        model = Cards 
        fields = '__all__'

        