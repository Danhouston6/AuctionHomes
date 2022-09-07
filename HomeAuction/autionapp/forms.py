from django import forms
from django.core.exceptions import ValidationError

from django.core import validators
from django.forms import ModelForm
from django.contrib.auth.models import User

from autionapp.models import House,Owner,Transaction,Buyer,NewTrans

class FormName (forms.ModelForm):
    class Meta():
        model = Buyer
        fields = '__all__'

class UserForm(ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')

# class HomeForm(ModelForm):
#     class Meta():
#         model = House
#         fields = ('house_id','house_name','max_bid_price')

class UserBidForm(ModelForm):
    # highest_bid = forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta():
        model = NewTrans
        fields = ('house_id','highest_bid_amount')

        # widget = {
        #     'highest_bid_amount': forms.DecimalField(attrs={'class':'numericinputclass'})
        # }

    #         fields = ('house_id','username','highest_bid_amount')

    # def clean_maxbid(self,bid_amount,databasemax):
    #     data = self.cleaned_data['highest_bid_amount']
    #     if int(bid_amount) < int(databasemax):
    #         alert ("You need to increase your bid!from Forms")
    #     return data


class housebidform(ModelForm):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta():
        model = House
        fields = ('house_id','max_bid_price')

        # if highest_bid <= max_bid_price:
        #     raise forms.ValidationError("you have been outbided!")

# from django import forms
# from django.core import validators
# from autionapp.models import House,Owner,Transaction,Buyer
#
# class auctionformclass (forms.Form):
#     #validation Area
#     class meta:
#         fields
