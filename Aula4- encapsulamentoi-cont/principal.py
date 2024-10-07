from funcionario import funcionario

funcionario1 = funcionario(  'Desenvolvedor', 38000)
print("Seu cargo atual é : ", funcionario1.getCargo())
#print("Seu salário atual é : ", funcionario1.salario)


#tentando mudar  o cargo

funcionario1.__cargo="DEV Senior"#acessando o atributo direto
funcionario1.setCargo("Engineer")#acessando método para mudar

print("Seu cargo atual é : ", funcionario1.getCargo())


funcionario2 = funcionario('Gerente', 50000)

print("Seu cargo atual é : ", funcionario2.getCargo())
#print("Seu salário atual é : ", funcionario2.salario)

#EXBINDO O SALÁRIO 

print("O seu salário  é : ", funcionario1.salario) #acessando o atributo direto

print("O seu salário  é : ", funcionario1.salario) #acessando o método para acessar o atributo

funcionario1.salario =  60000 #acessando o atributo direto
#funcionario1.setSalario(60000) #acessando o método para mudar
print("O seu salário  é : ", funcionario1.salario) #acess