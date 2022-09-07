from django import forms

from autionapp.models import House,Owner,Transaction,Buyer

class NewBuyerForm (forms.ModelForm):
    class Meta():
        model = Buyer
        fields = '__all__'
