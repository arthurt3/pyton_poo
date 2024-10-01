from contaBancaria import Conta

minhaconta = Conta (123, "Gilmar", 1000, 500)

minhaconta.detalhes()

minhaconta.saldo = 20000
minhaconta.detalhes()

print(f"O limite atual é {minhaconta.getLimite}")

minhaconta.setLimite(259)#alterando o valor do limite

print(f"O limite atual é {minhaconta.getLimite}")

minhaconta.depositar(100)
minhaconta.detalhes ()

minhaconta.sacar(500)
minhaconta.detalhes()


