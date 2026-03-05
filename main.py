class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


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
                f"Personal do aluno: {'Sem personal' if self.personal is None else self.personal}\n"
                f"Plano: {'Sem matrícula' if self.plano is None else self.plano.nome}\nSaldo: R${self.saldo:.2f}")

    @property
    def matriculado(self):
        return self._matriculado

    @matriculado.setter
    def matriculado(self, atualizar: bool):
        self._matriculado = atualizar

    def pagar(self, plano):
        if self.saldo >= plano.preco:
            self.saldo -= plano.preco
            print(f"Pagamento de R${plano.preco:.2f} efetuado")
            return True
        else:
            return False

    @property
    def personal(self):
        return self._personal
    
    @personal.setter
    def personal(self, personal):
        self._personal = personal



class Personal(Pessoa):
    def __init__(self, nome, idade, especialidade):
        super().__init__(nome, idade)
        self.especialidade = especialidade

    def __str__(self):
        return (f"Nome do Personal: {self.nome}\n"
                f"Idade do Personal: {self.idade}\n"
                f"Especialidades: {self.especialidade}")


class Plano:
    def detalhes(self):
        raise NotImplementedError(
            f"Você esqueceu de dar detalhes sobre o plano {self}.")


class Basico(Plano):
    def __init__(self):
        self.nome = "Básico"
        self.preco = 50.0
        self.beneficios = ["Musculação"]

    def __str__(self):
        return self.nome

    def detalhes(self):
        return f"Plano: {self.nome} | R${self.preco:.2f} | {', '.join(self.beneficios)}"


class Pro(Plano):
    def __init__(self):
        self.nome = "Pro"
        self.preco = 70.0
        self.beneficios = ["Musculação", "Cardio"]

    def __str__(self):
        return self.nome

    def detalhes(self):
        return f"Plano: {self.nome} | R${self.preco:.2f} | {', '.join(self.beneficios)}"


class Premium(Plano):
    def __init__(self):
        self.nome = "Premium"
        self.preco = 100.0
        self.beneficios = ["Musculação", "Cardio", "Personal incluso"]

    def __str__(self):
        return self.nome

    def detalhes(self):
        return f"Plano: {self.nome} | R${self.preco:.2f} | {', '.join(self.beneficios)}"


class Academia:
    def __init__(self, nome, planos):
        self.nome = nome
        self.alunos = []
        self.personais = []
        self.planos = planos

    def __str__(self):
        planos = [plano.nome for plano in self.planos]
        return f"Academia: {self.nome} | Planos ofertados: {planos}"

    def cadastrar_personal(self, personal):
        if personal in self.personais:
            return "O personal já está cadastrado."
        self.personais.append(personal)
        return f"personal adicionado com sucesso!"

    def matricular(self, aluno, plano):
        if aluno in self.alunos:
            return "O aluno já está matriculado"
        if aluno not in self.alunos:
            if aluno.pagar(plano):
                aluno.plano = plano
                aluno.matriculado = True
                self.alunos.append(aluno)
                return f"Aluno {aluno.nome} matriculado com sucesso"
            else:
                return "Não foi possível concluir a matrícula. Pagamento não concluido"

    def designar_personal(self, personal, aluno):

        if personal in self.personais and aluno in self.alunos:
            if isinstance(aluno.plano, Premium):
                aluno.personal = personal
       

        if personal not in self.personais:
            return "Personal não está cadastrado"

        if aluno not in self.alunos:
            return "O aluno não está matriculado."
             
                


if __name__ == "__main__":
    aluno = Aluno("Jhefferson", 28, 2000)
    personal = Personal("José", 35, ["Musculação", "Cárdio"])

    academia = Academia("Espaço fitness", [Basico(), Pro(), Premium()])
    academia.cadastrar_personal(personal)
    academia.matricular(aluno, Premium())
    academia.designar_personal(personal, aluno)
    print(aluno)
