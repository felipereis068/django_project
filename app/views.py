from django.shortcuts import render
from django.http import HttpResponse
from app import templates
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Formulario de cadastro dos usuários
def create(request):
    return render(request,'create.html')

# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    
    if request.method == "POST":
        password = request.POST.get('password')
        password_conf = request.POST.get('password-conf')
        
        if password and password_conf:
            if password != password_conf:
                data['msg'] = 'As senhas não coincidem'
                data['class'] = 'alert-danger'
            else:
                # Lógica para inserir os dados no banco de dados, caso as senhas coincidam
                user = User.objects.create_user(
                    request.POST['name'],
                    request.POST['email'],
                    password  # Aqui usamos a variável `password`
                )
                user.first_name = request.POST['name']
                user.save()
                data['msg'] = 'Usuário cadastrado com sucesso!'
                data['class'] = 'alert-success'
        else:
            data['msg'] = 'Preencha todos os campos'
            data['class'] = 'alert-danger'
    
    return render(request, 'create.html', data)
