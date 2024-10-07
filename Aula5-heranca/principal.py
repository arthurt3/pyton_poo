from funcionario import  Pessoa, Engenheiro, Secretario

f1 =  Pessoa('João', 'Gerente')
engenheiro1 =  Engenheiro('Roberto', 'Engenheiro pleno')
sec = Secretario ('Maria', 'Secretaria')


f1.informacoes()
engenheiro1.informacoes()
engenheiro1.mostraDetalhes()
sec.relatorio()