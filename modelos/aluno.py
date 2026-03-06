from modelos.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, saldo: float, personal=None, plano=None):
        super().__init__(nome, idade)
        self.personal = personal
        self.plano = plano
        self.matriculado = False
        self.saldo = saldo

    def __str__(self):
        return (f"Nome do aluno: {self.nome}\n"
                f"Idade do aluno: {self.idade}\n"
                f"Personal do aluno: {'Sem personal' if self.personal is None else self.personal.nome}\n"
                f"Plano: {'Sem matrícula' if self.plano is None else self.plano.nome}\nSaldo: R${self.saldo:.2f}")

    @property
    def matriculado(self):
        return self._matriculado

    @matriculado.setter
    def matriculado(self, atualizar: bool):
        self._matriculado = atualizar

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser menor que 0")
        self._saldo = valor

    def pagar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Pagamento de R${valor:.2f} efetuado")
            return True
        else:
            return False
