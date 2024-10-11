from django.db import models
from django.utils import timezone


# Model for Supplier Registration
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco_rua = models.CharField(max_length=150)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    endereco_cep = models.CharField(max_length=9)
    telefone_fixo = models.CharField(max_length=14)
    telefone_celular = models.CharField(max_length=14)
    email = models.EmailField()
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome

# Model for Customer Registration


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    endereco_rua = models.CharField(max_length=150)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    endereco_cep = models.CharField(max_length=9)
    data_cadastro = models.DateField(default=timezone.now)
    telefone_fixo = models.CharField(max_length=14)
    telefone_celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


# Model for Employee Registration
class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Escolaridade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    endereco_rua = models.CharField(max_length=150)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    endereco_cep = models.CharField(max_length=9)
    data_cadastro = models.DateField(default=timezone.now)
    telefone_fixo = models.CharField(max_length=14)
    telefone_celular = models.CharField(max_length=14)
    email = models.EmailField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Model for Service Order
class OrdemServico(models.Model):
    tecnico = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao_problema = models.TextField()
    data = models.DateField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ordem de Serviço {self.id} - Cliente: {self.cliente.nome}"


# Model for Service Order Items
class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class ItemOrdemServico(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total_item = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Baixar do estoque ao salvar item da OS
        self.produto.quantidade_estoque -= self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item {self.id} - Produto: {self.produto.nome}"

# Model for Accounts Receivable
class ContaReceber(models.Model):
    ordem_servico = models.OneToOneField(OrdemServico, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Conta a Receber - Ordem de Serviço {self.ordem_servico.id}"


# Model for Company Information
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    endereco_rua = models.CharField(max_length=150)
    endereco_bairro = models.CharField(max_length=100)
    endereco_numero = models.CharField(max_length=10)
    endereco_cep = models.CharField(max_length=9)
    telefone_fixo = models.CharField(max_length=14)
    telefone_celular = models.CharField(max_length=14)
    email = models.EmailField()
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome