import json
import jwt
import bcrypt
import datetime
import re

from django.views import View
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from my_settings import SECRET, ALGORITHM

from .models import Seller, SellerProperty, SellerStatus, SellerStatusHistory, ManagerInformation
from .utils import login_decorator


class SignUpView(View):
    def post(self, request):
        """회원가입 API

        회원가입을 위한 정보를 body 에 받음

        Args:
            request:
                brand_crm_number   : 브랜드 고객센터 번호
                password           : 비밀번호
                phone_number       : 담당자 핸드폰 번호
                account            : 계정
                brand_name_korean  : 브랜드명 ( 한글 )
                brand_name_english : 브랜드명 ( 영어 )
                seller_property_id : 셀러 속성 id ( 로드샵, 마켓 등 )

        Returns:
            200 : success , 회원가입 성공 시
            400 : 같은 계정이 존재할 때, key error
            500 : Exception

        """
        data = json.loads(request.body)
        try:
            if re.match(r'^[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}$', data['brand_crm_number']) is None:
                return JsonResponse({'message': 'INVALID_CRM_NUMBER'}, status=400)

            if re.match(r'^(?=.*[0-9])(?=.*[A-Za-z])(?=.*[^a-zA-Z0-9]).{8,20}$', data['password']) is None:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)

            if re.match(r'^010-[0-9]{3,4}-[0-9]{4}$', data['phone_number']) is None:
                return JsonResponse({'message': 'INVALID_PHONE_NUMBER'}, status=400)

            if len(data['account']) < 5:
                return JsonResponse({'message': 'SHORT_ACCOUNT'}, status=400)

            if Seller.objects.filter(account=data['account']).exists():
                return JsonResponse({'message': 'ALREADY_EXIST'}, status=400)

            password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            seller = Seller.objects.create(
                account=data['account'],
                password=password,
                brand_crm_number=data['brand_crm_number'],
                brand_name_korean=data['brand_name_korean'],
                brand_name_english=data['brand_name_english'],
                seller_property_id=data['seller_property_id']
            )
            ManagerInformation.objects.create(
                seller_id=seller.id,
                phone_number=data['phone_number'],
                ordering=1
            )

            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Exception as e:
            return JsonResponse({'message': '{}'.format(e)}, status=500)