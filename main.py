from modelos.aluno import Aluno
from modelos.personal import Personal
from modelos.planos import Basico, Pro, Premium
from sistema.academia import Academia
from utils.cadastro import cadastrar_aluno

if __name__ == "__main__":
    aluno = cadastrar_aluno()
    personal = Personal("José", 35, ["Musculação", "Cárdio"], 25.0)

    academia = Academia("Espaço fitness", [Basico(
    ), Pro(), Premium()])
    academia.cadastrar_personal(personal)
    academia.matricular(aluno, Basico())
    academia.designar_personal(personal, aluno)
    print(academia.contratar_personal(personal, aluno))
    print(aluno)
