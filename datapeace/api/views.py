from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .models import Users
from .serializers import UserSerializer
from rest_framework import status
import json


class UserView(APIView):
    def get(self, request, uid=0, page=0, limit=0, name='', sort=''):
        try:
            if uid:
                user_data = Users.objects.get(id=uid)
                serialized_data = UserSerializer(user_data)
            elif page:
                user_data = Users.objects.all()
                paginator = Paginator(user_data, limit)

                paged_data = paginator.get_page(page)

                serialized_data = UserSerializer(paged_data, many=True)

                name_list = []
                for odict in serialized_data.data:
                    if odict['first_name']:
                        name_list.append(odict['first_name'])
                    if odict['last_name']:
                        name_list.append(odict['last_name'])

                x = [s for s in name_list if name.lower() in s.lower()]

                final_data = []
                if len(x):
                    for element in x:
                        for ordict in serialized_data.data:
                            if (ordict['first_name'] == element) or (ordict['last_name'] == element):
                                final_data.append(ordict)
                    if sort[0] == '-':
                        new_final_list = sorted(final_data, key=lambda k: k[sort[1:]], reverse=True)
                    else:
                        new_final_list = sorted(final_data, key=lambda k: k[sort])
                    return Response(data=new_final_list, status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_200_OK)

            else:
                user_data = Users.objects.all()
                serialized_data = UserSerializer(user_data, many=True)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = json.loads(request.body)
            uid = data.get('id')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            company_name = data.get('company_name')
            age = data.get('age')
            city = data.get('city')
            state = data.get('state')
            zip_code = data.get('zip_code')
            email = data.get('email')
            web = data.get('web')

            data_to_save = uid, first_name, last_name, company_name, age, city, state, zip_code, email, web

            user_obj = Users(*data_to_save)
            user_obj.save()

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request, uid=0):
        if uid:
            try:
                data = json.loads(request.body)
                first_name = data.get('first_name')
                last_name = data.get('last_name')
                age = data.get('age')
                user_object = Users.objects.get(id=uid)

                user_object.first_name = first_name
                user_object.last_name = last_name
                user_object.age = age
                user_object.save()

            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uid=0):
        if uid:
            try:
                user_data = Users.objects.get(id=uid)
                user_data.delete()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

