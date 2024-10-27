# Definindo a classe Heroi
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "realizou um ataque desconhecido"
        
        print(f"O {self.tipo} atacou usando {ataque}.")

# Criando instâncias (objetos) da classe Heroi
heroi1 = Heroi("Aragorn", 30, "guerreiro")
heroi2 = Heroi("Gandalf", 100, "mago")

# Testando os ataques dos heróis
heroi1.atacar()  # Saída: O guerreiro atacou usando espada.
heroi2.atacar()  # Saída: O mago atacou usando magia.
