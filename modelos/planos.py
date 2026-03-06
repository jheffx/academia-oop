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