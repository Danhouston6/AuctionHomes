from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
# from django.forms import ValidationError
from django.core.exceptions import ValidationError
from django.contrib import messages
from . import models
from . import forms
import random
#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from autionapp.forms import UserBidForm, UserForm, housebidform
from autionapp.models import House,Owner,Transaction,Buyer
from django.views.generic import ListView, DetailView
# from . import models

# Create your views here.
# added classed based views
class HouseListView(ListView):
    context_object_name = 'homes'
    model = models.House



class HouseDetailView(DetailView):
    context_object_name = 'house'
    model = models.House
    template_name = 'autionapp/house_detail.html'

    def get_queryset(self):
        housedata = get_object_or_404(House,house_id=self.house_id)
        return housedata
        # self.house_id=get_object_or_404(House,house_id=self.kwargs['house_id'])
        # return House.objects.filter(pk = housedata.pk)



# class HouseDetailView(DetailView):
#     queryset = House.objects.all()
#     context_object_name = 'house'

def auctiondetail(request):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["house_detail"] = House.objects.get(pk = self.pk)
    return render(request, "autionapp/Detail_view.html", context)


def index(request):
    return render (request,'autionapp/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def FormBuyerReg(request):
    return render (request,'autionapp/FormBuyerReg.html')

def bid(request):
    return render (request,'autionapp/bid.html')

def auctionlist(request):

    home_list = House.objects.order_by('id')
    home_list_dict = {'home_records': home_list}
    return render(request,'autionapp/auctionlist.html',context=home_list_dict)
    # return render(request,'autionapp/List_homes.html')

def checkbidamount(request,house_id,bid_amount):
    housedata = get_object_or_404(House,pk=house_id)
    registered_max_bid = housedata.max_bid_price
    registered_starting_price = housedata.starting_price
    # print('get404 max bid'+ str(max))
    # print('current bid'+str(bid_amount))
    # home_list = House.objects.order_by('id')
    # home_list_dict = {'home_records': home_list}
    # for homes in home_list:
        # print('datbase house_id '+str(homes.house_id))
        # print('input house_id '+str(house_id))
        # # print('datbase house area '+str(homes.total_area))
        # # print('database no of beds '+str(homes.no_of_bed))
        # print('database max bid Price'+str(homes.max_bid_price))
        # print('innput bid pice'+str(bid_amount))


        # if int(homes.house_id) == int(house_id):
            # registered_max_bid = homes.max_bid_price
            # registered_max_bid = 0
            # print("house_id matching "+str(homes.house_id))
            # print("registered max bid using loop"+str(registered_max_bid))
            # print("Bid Amount "+str(bid_amount))
    if (int(bid_amount) > int(registered_max_bid)) and (int(bid_amount) > int(registered_starting_price)) :


        print("Good Bid")
        bidsucessflag = True

    elif int(bid_amount) < int(registered_starting_price):
        print("bid has to be greater than starting_price")
        messages.error(request,"Your bid Amount has to be more than the starting price!")
        bidsucessflag = False

    else:
        print("Increae your bid")
        messages.info(request, "Your bid Amount has to be more than the max current max bid!")
        bidsucessflag = False

                # t = House.objects.get(house_id)
                # t.max_bid_price = int(bid_amount)
                # t.save()
                # update the datbase with the new data

        # else:
            # registered_max_bid = 0
            # print("house_id not matching "+str(homes.house_id))
            # print("house_id not matching databases "+str(house_id))
            # bidsucessflag = False


    return bidsucessflag

# Posting the highest bid to Home database
# def posthighestbid(house_id,highest_bid_amount):



# Create your views here.
def FormBuyerReg(request):
    # calling the instance for the NewuserFrom - bassically running it
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
            # returning as to the home page
        else:
            print('Erron Form Invalid')

    return render(request,'autionapp/FormBuyerReg.html',{'form':form})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
         user_form = UserForm()

    return render (request,'autionapp/registration.html',
                    {'user_form': user_form,
                     'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("someone tried to login and failed!")
            print("username: {} and password {}".format(username,password))
            return HttpResponse ("invalid login details supplied!")


    else:
        return render(request,'autionapp/login.html',{})

def bid_submit(request):
    higherbid = False
    # registered = False

    if request.method == "POST":
        bid_form = UserBidForm(data=request.POST)

        house_id = request.POST.get('house_id')
        highest_bid_amount = request.POST.get('highest_bid_amount')



        if bid_form.is_valid():
            bid = bid_form.save(commit=False)

            goodbid = checkbidamount(request,house_id,highest_bid_amount)
            if goodbid:
                # print("You register the highest bid! Good Luck!")
                bid = bid_form.save()
                # add for checkpoint
                # username = request.POST.get('username')
                # user = get_object_or_404(User,pk=username)
                # bid.username = user.username

                # added end

                bid.save()
                higherbid = True
                # Try to update House
                # House.objects.get(house_id=house_id).update(max_bid_price=highest_bid_amount)
                housedata = get_object_or_404(House,pk=house_id)
                housedata.max_bid_price = highest_bid_amount


                # Grab the current username
                # username = request.POST.get('username')
                # user = get_object_or_404(User,pk=username)
                # print('datbaseuser '+user.username)

                current_user = request.user

                housedata.max_bidder = current_user.username


                housedata.publish()
                bid_form = UserBidForm()
                messages.success(request, 'You register the highest bid for the property! Good Luck!')
                return HttpResponseRedirect(reverse('autionapp:auctionlist'))

                # after register intial
                # bid_form = UserBidForm()

            else:
                print("You have been outbided views")

                housedata = get_object_or_404(House,pk=house_id)
                databasemax = housedata.max_bid_price

                # datamaxchar = str(databasemax)

                messages.error(request, "You need to increase your bid amount!")
                # messages.debug(request, ' for the propery ')
                # return redirect ("auctionapp:list")
                # bid_form.clean_maxbid(highest_bid_amount,databasemax)


                # display the current highest bid

                bid_form = UserBidForm()
                higherbid = False
                # return HttpResponse("outbided")
                # write error message

                # alert('increase your bid from views ')

                # print('bid form error from views ')
                # print(bid_form.errors)

                # added begin
                # message = "The form has errors"
                # explanation = bid_form.errors.as_data()
                # # Also incorrect request but this time the only flag for you should be that maybe JavaScript validation can be used.
                # status_code = 400

                # added end



        else:
            print(bid_form.errors)

    else:
         bid_form = UserBidForm()

    return render (request,'autionapp/bid.html',
                    {'bid_form': bid_form,
                      'higherbid': higherbid})
