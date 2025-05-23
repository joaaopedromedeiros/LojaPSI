from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#acima são bibliotecas padrões necessárias do Django, e abaixo nossos models
from .Fabricante import Fabricante
from .Categoria import Categoria
from .Produto import Produto


PERFIL=(
    (1, 'Admin'),
    (2, 'Usuario')
)

from .Usuario import Usuario
from .Carrinho import Carrinho
from .Carrinho import CarrinhoItem
