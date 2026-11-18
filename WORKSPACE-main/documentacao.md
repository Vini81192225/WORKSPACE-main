# comandos do django

1. `"pip install django"` -> instala o Django no projeto.
2. `"django-admin startproject nome_do_projeto"` . -> criando um novo projeto em django.
3. `"python manage.py runserver"` -> subindo o servidor.
4. `"python manage.py startapp nome_do_app"` -> criando um novo app.
5. `"python manage.py migrate"` -> realiza as migrações (ativa) do projeto
6. `"python manage.py createsuperuser"` -> criar um super usuário.
7. `"python manage.py changepassword nomedousuario"` -> Altera a senha, caso você esqueça.
8. `"python manage.py makemigrations"` -> Cria/gere um novo pacote de migração (Útil para novo app e alteração do BO)

# tags do django html
> {% load static %} -> Habilita o static no arquivo. Cada template que usa `{% static %}` precisa ser carregado.
> {% block title %} -> Insere o título da aba. As páginas filhas trocam
> {% block header %} -> O header público (logo+entrar). O `O base_logado.html` troca por inteiro.
> {% block header_actions %} -> Só o botão "entrar". O `login.html` esvazia o bloco.
> {% inclue ... %} -> Insere as mensagens e/ou blocos de código.
> {% block content %} -> O miolo da página, cada filho vai ter seu próprio <main>.

## tags de rota
> {% url 'sistema:medico-list' %} -> Fica nos templates e se refere a uma lista de médicos que está no app sistema.
> {% url 'sistema:medico-update' medico.pk %} -> Utilização no template com parâmetro para update do médico.
> {% url url_voltar %} -> url_voltar é o nome de uma variável que guarda uma lógica de retorno a página anterior.
> redirect('sistema:medico_list') -> Fica numa view e informa que quando uma ação for realizada, o usuário será redirecionado. 