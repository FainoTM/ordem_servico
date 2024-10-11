from django import forms
from django.contrib.auth.models import User

from .models import Cliente, Funcionario, OrdemServico, Produto
from django.contrib.auth.forms import UserCreationForm


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': 'XXX.XXX.XXX-XX'}),
            'telefone_fixo': forms.TextInput(attrs={'placeholder': '(XX)XXXXX-XXXX'}),
            'telefone_celular': forms.TextInput(attrs={'placeholder': '(XX)XXXXX-XXXX'}),
        }


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'


class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
