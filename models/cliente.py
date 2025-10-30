class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "fone": self.fone}

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
