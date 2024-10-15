from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Página inicial
def home(request):
    return render(request, 'home.html')

# Formulário de cadastro dos usuários
def create(request):
    return render(request, 'create.html')

# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_conf = request.POST.get('password-conf')
        
        if name and email and password and password_conf:
            if password != password_conf:
                data['msg'] = 'As senhas não coincidem'
                data['class'] = 'alert-danger'
            else:
                try:
                    # Lógica para inserir os dados no banco de dados, caso as senhas coincidam
                    user = User.objects.create_user(username=email, email=email, password=password)
                    user.first_name = name
                    user.save()
                    data['msg'] = 'Usuário cadastrado com sucesso!'
                    data['class'] = 'alert-success'
                except Exception as e:
                    data['msg'] = f'Erro ao cadastrar o usuário: {e}'
                    data['class'] = 'alert-danger'
        else:
            data['msg'] = 'Preencha todos os campos'
            data['class'] = 'alert-danger'
    
    return render(request, 'create.html', data)

# Formulário de login
def painel(request):
    return render(request, 'painel.html')

# Autenticação de usuários
def dologin(request):
    data = {}
    
    if request.method == "POST":
        username = request.POST.get('user')  # Certifique-se que este campo está correto no HTML
        password = request.POST.get('password')
        
        if username and password:  # Verifica se os campos não estão vazios
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
            else:
                data['msg'] = 'Usuário ou senha inválidos'
                data['class'] = 'alert-danger'
        else:
            data['msg'] = 'Preencha todos os campos'
            data['class'] = 'alert-danger'
    
    return render(request, 'painel.html', data)

# Página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

def logouts(request):
    logout(request)
    return redirect('/painel/')

""" def changePassoword(request):
    User.objects.get(email=request.user.email)
    u.set_password(request.POST.get('password')
    u.save()
    logout(request)
    return redirect('/painel/') """
    