from modelos.aluno import Aluno
from modelos.personal import Personal
from modelos.planos import Plano, Basico, Pro, Premium


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
            if aluno.pagar(plano.preco):
                aluno.plano = plano
                aluno.matriculado = True
                self.alunos.append(aluno)
                return f"Aluno {aluno.nome} matriculado com sucesso"
            else:
                return "Não foi possível concluir a matrícula. Pagamento não concluido"

    def designar_personal(self, personal, aluno):
        if personal not in self.personais:
            return "Personal não está cadastrado."
        if aluno not in self.alunos:
            return "O aluno não está matriculado."
        if not isinstance(aluno.plano, Premium):
            return "Apenas alunos Premium podem ter personal."

        aluno.personal = personal
        return f"Personal {personal.nome} designado para {aluno.nome}!"

    def contratar_personal(self, personal, aluno):
        if aluno not in self.alunos:
            return "O aluno não tem matrícula ativa."
        if not isinstance(aluno.plano, Premium):
            if aluno.pagar(personal.taxa):
                aluno.personal = personal
                return f"Personal contratado para {aluno.nome} por uma taxa de R${personal.taxa}"
            else:
                return "Saldo insuficiente para contratar personal"
        return f"Assinantes Premium não precisam contratar personal, pois já está incluso no plano."

