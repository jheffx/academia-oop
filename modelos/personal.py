from modelos.pessoa import Pessoa

class Personal(Pessoa):
    def __init__(self, nome, idade, especialidade, taxa):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.taxa = taxa

    def __str__(self):
        return (f"Nome do Personal: {self.nome}\n"
                f"Idade do Personal: {self.idade}\n"
                f"Especialidades: {self.especialidade}")