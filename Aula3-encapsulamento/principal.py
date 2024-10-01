from contaBancaria import Conta

minhaconta = Conta (123, "Gilmar", 1000, 500)

minhaconta.detalhes()

minhaconta.saldo = 20000
minhaconta.detalhes()

print(f"O limite atual é {minhaconta.getLimite}")


