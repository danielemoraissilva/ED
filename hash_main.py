from hash__table import Hash__table

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome} - Matrícula: {self.matricula}\n"

a = Aluno("Ana", 1123)
b = Aluno("Pedro", 1124)
c = Aluno("Luiz", 1126)

ht = Hash__table(10)
ht.insert(a.nome, a)
ht.insert(b.nome, b)
ht.insert(c.nome, c)

print(ht.get(a.nome))
print(ht.get(b.nome))
print(ht.get(c.nome))

ht.print()


