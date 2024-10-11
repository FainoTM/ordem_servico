from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Fornecedor, Cliente, Funcionario, Cargo, Escolaridade, OrdemServico, Produto, Marca, ItemOrdemServico, ContaReceber, Empresa


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ['nome']


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_estoque', 'valor_venda')
    list_editable = ['valor_venda']


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email')


@admin.register(Escolaridade)
class EscolaridadeAdmin(admin.ModelAdmin):
    list_display = ['nome']