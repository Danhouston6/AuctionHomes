from django.contrib import admin
from autionapp.models import House, Owner, Buyer, Transaction, NewTrans
# Register your models here.

admin.site.register(House)
admin.site.register(Owner)
admin.site.register(Buyer)
admin.site.register(Transaction)
admin.site.register(NewTrans)
