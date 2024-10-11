from django.db import transaction
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy

from .forms import ClienteForm, FuncionarioForm, ProdutoForm, OrdemServicoForm
from .models import Fornecedor, Cliente, Produto, ItemOrdemServico
from django.views.generic import CreateView
from .models import OrdemServico, Funcionario


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


# View para cadastrar um Fornecedor
class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields = '__all__'
    template_name = 'fornecedor_form.html'
    success_url = reverse_lazy('fornecedor_list')


# View para listar os Fornecedores
class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedor_list.html'


# View para cadastrar um Cliente
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('landing_page')


# View para cadastrar uma Ordem de Serviço
class OrdemServicoCreateView(CreateView):
    model = OrdemServico
    form_class = OrdemServicoForm
    template_name = 'ordem_servico_form.html'
    success_url = reverse_lazy('ordem_servico_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos'] = Produto.objects.all()  # Pega todos os produtos do banco de dados
        return context

    def form_valid(self, form):
        # Salva a ordem de serviço
        response = super().form_valid(form)
        ordem_servico = form.instance

        # Obtém os produtos do formulário
        produtos_ids = self.request.POST.getlist('produto')
        quantidades = self.request.POST.getlist('quantidade')

        # Atualiza o estoque dos produtos e cria os itens da ordem de serviço
        with transaction.atomic():  # Garante que todas as operações sejam atômicas
            for produto_id, quantidade in zip(produtos_ids, quantidades):
                produto = Produto.objects.get(pk=produto_id)
                quantidade = int(quantidade)

                if produto.quantidade_estoque >= quantidade:
                    # Reduz o estoque do produto
                    produto.quantidade_estoque -= quantidade
                    produto.save()

                    # Cria um item da ordem de serviço
                    ItemOrdemServico.objects.create(
                        ordem_servico=ordem_servico,
                        produto=produto,
                        quantidade=quantidade,
                        valor_total_item=quantidade * produto.valor_venda
                    )
                else:
                    form.add_error(None, f"Estoque insuficiente para o produto: {produto.nome}")
                    return self.form_invalid(form)

        return response


# View para listar as Ordens de Serviço
class OrdemServicoListView(ListView):
    model = OrdemServico
    template_name = 'ordem_servico_list.html'


# View para ver detalhes de uma Ordem de Serviço
class OrdemServicoDetailView(DetailView):
    model = OrdemServico
    template_name = 'ordem_servico_detail.html'



class FuncionarioCreateView(CreateView):
    model = Funcionario
    form_class = FuncionarioForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('landing_page')


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('landing_page')

