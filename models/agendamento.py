class Agendamento:
    def __init__(self, id, data, hora, id_profissional, id_cliente=None,
                 id_servico=None, confirmado=False):
        self.id = id
        self.data = data
        self.hora = hora
        self.id_profissional = id_profissional
        self.id_cliente = id_cliente
        self.id_servico = id_servico
        self.confirmado = confirmado

    def __str__(self):
        status = "Confirmado" if self.confirmado else "Pendente"
        return f"{self.data} {self.hora} - Profissional {self.id_profissional} - {status}"

    def to_json(self):
        return self.__dict__

    @staticmethod
    def from_json(dic):
        return Agendamento(**dic)
