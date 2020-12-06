import jwt
from functools import wraps

from django.http import JsonResponse
from my_settings import ALGORITHM, SECRET

from .models import Seller


def login_decorator(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message': 'INVALID_SELLER'}, status=401)

        try:
            access_token = request.headers['Authorization']
            data = jwt.decode(access_token, SECRET['secret'], algorithm=ALGORITHM)
            seller = Seller.objects.get(id=data['seller_id'])
            request.seller = seller

        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=400)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'TOKEN_EXPIRED'}, status=400)
        except Seller.DoesNotExist:
            return JsonResponse({'message': 'SELLER_NOT_EXIST'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper
