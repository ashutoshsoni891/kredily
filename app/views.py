from django.http import HttpResponse , JsonResponse
from django.core.serializers import serialize
import json
from datetime import datetime
# Create your views here.

from .models import Product , Order , kredilyUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_user(request):
    try :
        if request.method == 'POST':
            payload = json.loads(request.body)
            payload['password'] = make_password(payload['password'])
            print('PAYLOAD :---> ' , payload)

            user = User.objects.create(**payload)
            create = kredilyUser.objects.create(user = user)

            serial = serialize('json' , [create] ,use_natural_foreign_keys=True ,use_natural_primary_keys=True)
            return JsonResponse({'data' :  serial, 'success' : True , 'status' : 200 })

    except Exception as e:
        message = e
    finally:
        return JsonResponse({'message' : message , 'success' : False , 'status' : 400})


@csrf_exempt
def add_product(request):
    try :
        if request.method == 'POST':
            payload = json.loads(request.body)
            payload['createdAt'] = datetime.now()
            payload['updatedAt'] = datetime.now()
            create = Product.objects.create(**payload)
            serial = serialize('json' , [create] ,use_natural_foreign_keys=True ,use_natural_primary_keys=True)

            return JsonResponse({'data' :  serial, 'success' : True , 'status' : 200 })
        else:
            return HttpResponse('METHOD NOT ALLOWED!')
    except Exception as e:
        message = e
    finally:
        return JsonResponse({'message' : message , 'success' : False , 'status' : 400})

@csrf_exempt
def add_order(request):

    try :
        if request.method == 'POST':
            payload = json.loads(request.body)
            payload['createdAt'] = datetime.now()
            payload['updatedAt'] = datetime.now()
            pid = []
            for product in payload['products']:
                p = Product.objects.get(uuid = product['product'])
                if p.quantity < product['quantity']:
                    # return  HttpResponse('OUT OF STOCK!')
                    print('out of stock!')
                    p.quantity -= product['quantity']
                    p.save()
                pid.append(product['product'])
            payload['products'] = pid
            print('PAY : ', payload)
            create = Order.objects.create(**payload)
            serial = serialize('json' , [create] ,use_natural_foreign_keys=True ,use_natural_primary_keys=True)

            #get the product
            return JsonResponse({'data' :  serial, 'success' : True , 'status' : 200 })
        else:
            return HttpResponse('METHOD NOT ALLOWED!')
    except Exception as e:
        message = e
    finally:
        return JsonResponse({'message' : message , 'success' : False , 'status' : 400})
@csrf_exempt
def order_history(request):

    try:
        if request.method == 'POST':
            payload = json.loads(request.body)
            keys = payload.keys()
            query = {}
            if 'user_id' in keys:
                query['user_id'] = payload['user_id']

            if 'date' in keys:
                                
                query['createdAt__gte'] = datetime.strptime(payload['date']['from'] , '%Y-%m-%d')
                query['createdAt__lte'] = datetime.strptime(payload['date']['to'] , '%Y-%m-%d')
            filter = Order.objects.filter(**query)
            serial = serialize('json' , filter ,use_natural_foreign_keys=True ,use_natural_primary_keys=True)

            return JsonResponse({'data' :  serial, 'success' : True , 'status' : 200 })

        else:
            return HttpResponse('METHOD NOT ALLOWED!')
   
    except Exception as e:
        message = e
    finally:
        return JsonResponse({'message' : message , 'success' : False , 'status' : 400})

@csrf_exempt
def get_products(request):

    try:
        if request.method == 'POST':
            payload = json.loads(request.body)
            keys = payload.keys()
            query = {}
            
            if 'name' in keys:
                query['name__icontains'] = payload['name']

            if 'quantity' in keys:
                query['quantity__gte'] = payload['quantity'] 

            if 'price' in keys:
                query['price__gte'] = payload['price']['minimum']
                query['price__lte'] = payload['price']['maximum']

            if 'uuid' in keys:
                query['uuid'] = payload['uuid']
            
            filter = Product.objects.filter(**query)

            if 'pagination' in keys:                     
                page = payload['pagination']['page']
                size = payload['pagination']['size']
                total = len(filter)
                filter = filter[page *(total // size) : page *(total // size) + size]

            serial = serialize('json' , filter ,use_natural_foreign_keys=True ,use_natural_primary_keys=True)

            return JsonResponse({'data' :  serial, 'success' : True , 'status' : 200 })

        else :
            return HttpResponse('METHOD NOT ALLOWED!')
            
    except Exception as e:
        message = e
    finally:
        return JsonResponse({'message' : message , 'success' : False , 'status' : 400})


