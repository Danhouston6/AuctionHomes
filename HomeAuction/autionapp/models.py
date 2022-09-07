from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.

class Owner (models.Model):
    owner_id = models.IntegerField(unique = True)
    owner_name = models.CharField (max_length=264)
    owner_type = models.CharField (max_length=264)

    def __str__(self):
        return self.owner_name

# def check_if_max_bid(value):
#     housedata = get_object_or_404(House,pk=house_id)
#     max = housedata.max_bid_price
#
#     print("value "+char(value))
#     print("max "+char(max))
#
#     if value < max:
#         raise forms.ValidationError("Enter a higer bid amount")

class House (models.Model):
    house_id = models.IntegerField (unique = True)
    house_name = models.CharField (max_length=264)
    house_area = models.CharField (max_length=264)
    owner_id = models.ForeignKey (Owner, on_delete=models.CASCADE)
    no_of_bed = models.IntegerField()
    no_of_bath = models.IntegerField()
    total_area = models.DecimalField(max_digits=14, decimal_places=0)
    list_price = models.DecimalField(max_digits=14, decimal_places=0)
    starting_price = models.DecimalField(max_digits=14, decimal_places=0)
    max_bid_price = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    # max_bid_price = models.DecimalField(validators=[check_if_max_bid],max_digits=10, decimal_places=0, default=0)

    max_bidder = models.CharField(max_length=264,default='None')
    # max_bid_price = models.DecimalField(max_digits=10, decimal_places=0, null=True,blank=True)
    house_main_pic = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    house_detail_url = models.URLField(max_length=200)
    auction_end_date = models.DateField(null=True,blank=True)
    # auction_end_time = models.TimeField(null=True,blank=True)

    # add the date of change and max bidder
    def publish(self):
        self.save()

    def __str__(self):
        return self.house_name
    # def __str__(self):
    #     return self.max_bid_price

def check_if_max_bid(value):
    housedata = get_object_or_404(House,pk=house_id)
    max = housedata.max_bid_price

    print("value "+char(value))
    print("max "+char(max))

    if value < max:
        raise forms.ValidationError("Enter a higer bid amount")



class Buyer (models.Model):
    buyer_id = models.IntegerField (unique = True)
    buyer_name = models.CharField (max_length= 264)
    # first_name = models.CharField(max_length=264 )
    # last_name = models.CharField(max_length=264)
    # email = models.CharField(max_length=264,default='a@gmail.com')
    buyer_account_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.buyer_name

class Transaction (models.Model):
    house_id = models.ForeignKey (House, on_delete=models.CASCADE)
    # highest_bidder_id = models.ForeignKey (Buyer, on_delete=models.CASCADE)
    highest_bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # auction_end_time = models.DateField()
    # auction_end_time = models.TimeField()
    # username = models.OneToOneField(User, on_delete=models.CASCADE, )



class NewTrans (models.Model):
    house_id = models.ForeignKey (House, on_delete=models.CASCADE)
    # highest_bidder_id = models.ForeignKey (Buyer, on_delete=models.CASCADE)
    highest_bid_amount = models.DecimalField(max_digits=14, decimal_places=2)
    # auction_end_time = models.DateField()
    # auction_end_time = models.TimeField()
    # taken out for the time being
    # username = models.ForeignKey (User, on_delete=models.CASCADE )
    Bidder = models.CharField (max_length= 264,null=True,blank=True)

    # max_bid_price = models.ForeignKey (House, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.username

    # def checkbidamount (self):
    #     if highest_bid_amount <= House.max_bid_price:
    #         print("you need to increase bid")
    #         bidflag = False
    #     else:
    #         print("Good Luck from model")
    #         bidflag = True
    #     return bidflag
