from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('fornecedores/', views.FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedor/novo/', views.FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('ordens_servico/', views.OrdemServicoListView.as_view(), name='ordem_servico_list'),
    path('ordem_servico/novo/', views.OrdemServicoCreateView.as_view(), name='ordem_servico_create'),
    path('ordem_servico/<int:pk>/', views.OrdemServicoDetailView.as_view(), name='ordem_servico_detail'),
    path('funcionarios/novo/', views.FuncionarioCreateView.as_view(), name='funcionario_create'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
]
