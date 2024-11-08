from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

class userLogin(APIView):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            user_details = {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
            request.session['user_details'] = user_details
            request.session['access_token'] = access_token

            return redirect('note_list')
            
            # return Response({"success": True, 'details': 'Success', 'access_token': access_token, 'userdetails': user_details}, status=status.HTTP_200_OK)
        else:
            return render(request, 'registration/login.html', {'messages':['Invalid credentials.']})
            # return Response({"success": False, 'details': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class signUp(APIView):
    def get(self,request):
        return render(request, 'registration/signup.html')
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/signup.html', {'messages':['Email is already registered.']})
            # return Response({"success": False, "details": "Email is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            user_details = {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }

            context = {
                "success": True,
                "messages": ["User created successfully."],
                "access_token": access_token,
                "userdetails": user_details
            }

            return render(request, 'registration/signup.html', context=context)

            # return Response({
            #     "success": True,
            #     "details": "User created successfully.",
            #     "access_token": access_token,
            #     "userdetails": user_details
            # }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return render(request, 'registration/signup.html', {'messages':e})
            # return Response({"success": False, "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)