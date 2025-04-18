from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm

def list_usuario_view(request, id=None):
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
    'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)

def edit_usuario_view(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    emailUnused = True
    message = None
    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)
        # Verifica se o e-mail que o usuário está tentando utilizar
        # em seu perfil já existe em outro perfil
        verifyEmail = Usuario.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.
id).first()
        emailUnused = verifyEmail is None
    else:
        usuarioForm = UserUsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)
    if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
        usuarioForm.save()
        userForm.save()
        message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
    else:
        # Aqui verificamos se é do tipo post, para que na primeira vez que a página carregar a mensagem não apareça, já que no primeiro carregamento não enviamos um post, o form é dado como inválido e entra aqui.
        if request.method == 'POST':
            if emailUnused:
                # Se o e-mail não está em uso tiver algum dado inválido.

                message = { 'type': 'danger', 'text': 'Dados inválidos' }
            else:
                # Se o e-mail já está em uso por outra pessoa.
                message = { 'type': 'warning', 'text': 'E-mail já usado' }

        # Até aqui
    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
        'message': message
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)