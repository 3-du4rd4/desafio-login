import re
from .models import *
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def Home(request):
    user_name = request.user.first_name or "Usuário"
    return render(request, 'index.html', {'name': user_name})


def RegisterView(request):
    if request.method ==  'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        has_error = False

        if not (re.fullmatch(r'[\u00C0-\u00FFA-Za-z ]+', name)):
            has_error = True
            messages.error(request, 'O nome deve conter apenas letras e espaços. Evite caracteres especiais.')

        try:
            EmailValidator()(email)
        except ValidationError:
            has_error = True
            messages.error(request, 'Por favor, insira um e-mail válido.')

        if User.objects.filter(email=email).exists():
            has_error = True
            messages.error(request, 'Esse e-mail já está registrado. Tente fazer login ou use outro e-mail.')

        if not re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$', password):
            has_error = True
            messages.error(request, 'A senha precisa ter pelo menos 8 caracteres, incluindo 1 número, 1 caractere especial e 1 letra maiúscula.')

        if password != password_confirm:
            has_error = True
            messages.error(request, 'As senhas não coincidem. Verifique e tente novamente.')

        if has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                username=email,
                first_name=name,
                email=email,
                password=password
            )

            subject = "Confirmação de Registro no Desafio Técnico"
            body = f"Olá {name},\n\nSeu registro no Desafio Técnico da Fidelity foi realizado com sucesso!\n\nAtenciosamente,\nMaria Eduarda"

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [email],  
                fail_silently=False,
            )

            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('login')
        
    return render(request, 'register.html')


def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=email)
        except User.DoesNotExist:
            messages.error(request, 'Não encontramos um usuário com esse e-mail. Verifique e tente novamente.')
            return redirect('login')

        user = authenticate(request=request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'A senha informada está incorreta. Tente novamente.')
            return redirect('login')

    return render(request, 'login.html')


def LogoutView(request):
    logout(request)

    return redirect ('login')  
