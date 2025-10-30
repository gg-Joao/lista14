
from models.cliente import Cliente
from models.clienteDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO
from models.horario import Horario
from models.horarioDAO import HorarioDAO

class View:

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_inserir(nome, email, fone):
        ClienteDAO.inserir(Cliente(0, nome, email, fone))

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        ClienteDAO.atualizar(Cliente(id, nome, email, fone))

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO.excluir(id)

    @staticmethod
    def servico_listar():
        return ServicoDAO.listar()

    @staticmethod
    def servico_inserir(descricao, valor):
        ServicoDAO.inserir(Servico(0, descricao, valor))

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        ServicoDAO.atualizar(Servico(id, descricao, valor))

    @staticmethod
    def servico_excluir(id):
        ServicoDAO.excluir(id)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar()

    @staticmethod
    def profissional_inserir(nome, especialidade, fone, email, senha):
        ProfissionalDAO.inserir(Profissional(0, nome, especialidade, fone, email, senha))

    @staticmethod
    def profissional_atualizar(id, nome, especialidade, fone, email, senha):
        ProfissionalDAO.atualizar(Profissional(id, nome, especialidade, fone, email, senha))

    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO.excluir(id)

    @staticmethod
    def autenticar_profissional(email, senha):
        profissionais = ProfissionalDAO.listar()
        for p in profissionais:
            if p.email == email and p.senha == senha:
                return p
        return None

    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()

    @staticmethod
    def horario_inserir(data, hora, idProfissional):
        HorarioDAO.inserir(Horario(0, data, hora, idProfissional))

    @staticmethod
    def horario_atualizar(id, data, hora, idProfissional):
        HorarioDAO.atualizar(Horario(id, data, hora, idProfissional))

    @staticmethod
    def horario_excluir(id):
        HorarioDAO.excluir(id)
   
    @staticmethod
    def autenticar_cliente(email, fone):
        clientes = ClienteDAO.listar()
        for c in clientes:
            if c.email == email and c.fone == fone:
                return c
        return None
