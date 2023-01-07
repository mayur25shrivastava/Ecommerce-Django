from math import ceil
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import product,Contact,Orders,OrderUpdate
import json
# from django.shortcuts import render


# for payment gateway
# from django.views.decorators.csrf import csrf_exempt
# from PayTm import Checksum
# MERCHANT_KEY = 'Your-Merchant-Key-Here'
# MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'






# Create your views here.




def index(request):
    # products=product.objects.all()
    # print(products)
    # n=len(products)
    # nslides=n//4 + ceil((n/4))

    # ------------>acc to lec 36 
    allProds=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4 + ceil((n/4))
        allProds.append([prod,range(1,nslides),nslides])

    # params={'no_of_slides':nslides , 'range':range(1,nslides) , 'product':products}
    # allProds=[[products,range(1,nslides),nslides],
    # [products,range(1,nslides),nslides]]

    params={'allProds':allProds}

    return render(request,'shop/index.html',params)
    # return HttpResponse("Indexxx bloggg")


def about(request):
    return render(request,'shop/about.html')
    # return HttpResponse("we are at about")

def contact(request):

    if request.method=="POST":
        print(request)

        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)


        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'shop/contact.html')
    # return HttpResponse("we are at about")


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    # response = json.dumps(updates, default=str)
                    response = json.dumps([updates,order[0].items_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def search(request):
    # return render(request,'shop/index.html')
    return render(request,'shop/search.html')


def productview(request,myid):
    # return render(request,'shop/index.html')

    # fetch the product using id 
    Product=product.objects.filter(id=myid)
    print(Product)
    return render(request,'shop/productview.html',{'product':Product[0]})

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        amount=request.POST.get('amount', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone,amount=amount)
        order.save()

        update= OrderUpdate(order_id= order.order_id, update_desc="The order has been placed")
        update.save()

        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request,'shop/checkout.html')
        #remember to uncomment upper part 🙄 ----->comment becz of payment gateway 😅😅😪



        # paytm payment gateway add 
        # Request paytm to transfer the amount to your account after payment by user

        #😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂
    #     param_dict = {

    #             'MID': 'worldP64425807474247',
    #             'ORDER_ID': str(order.order_id),
    #             'TXN_AMOUNT': str(amount),
    #             'CUST_ID': email,
    #             'INDUSTRY_TYPE_ID': 'Retail',
    #             'WEBSITE': 'WEBSTAGING',
    #             'CHANNEL_ID': 'WEB',
    #             'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

    #     }
    #     param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    #     return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    
    # return render(request, 'shop/checkout.html')



#payment gateway
# 😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂
# @csrf_exempt
# def handlerequest(request):
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'shop/paymentstatus.html', {'response': response_dict})

#     return HttpResponse('done')
#     pass