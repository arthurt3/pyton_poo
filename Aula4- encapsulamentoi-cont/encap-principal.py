from restaurante import Servico


servico = Servico()

print("Número de pedidos inicial:", servico.exibirPedido())

servico.novoPedido()
servico.novoPedido()
print("Número de pedidos após novo pedido:", servico.exibirPedido())

servico.novoPedido()
print("Número de pedidos após outro novo pedido:", servico.exibirPedido())

servico.cancelarPedido()
print("Número de pedidos após cancelar pedido:", servico.exibirPedido())

servico.cancelarPedido()
print("Número de pedidos após cancelar outro pedido:", servico.exibirPedido())

servico.cancelarPedido()
# exibir a mensagem de aviso: "Aviso: Não há pedidos para cancelar."