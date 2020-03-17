from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

# for stripe
import stripe

stripe.api_key = "sk_test_3E0FXJHdJTyGaNl9ZNHiAc9O00IESuhi5h"

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


# this will process the card information
def charge(request):

    if request.method == 'POST':
        print('Data:', request.POST)
        amount = int(request.POST['amount'])
        # creating a customer
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        # print(customer)

        # creating a charge
        charge = stripe.Charge.create(
            customer=customer,
            # as stripe consider amount to penny
            amount=amount*100,
            currency='usd',
            description="Donation"
        )

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'core/success.html', {'amount': amount})
