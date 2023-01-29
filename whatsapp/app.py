import pywhatkit

# Enviar mensagem para um contato
num_cel = input("Insira número de telefone: ")

pywhatkit.sendwhatmsg(num_cel, "Teste", 7, 21)
pywhatkit.sendwhatmsg(num_cel, "Teste", 7, 25, 15, True, 2)

# Eniviar mensagem para Grupo
grupo_id = input("Insira o id do grupo: ")

pywhatkit.sendwhatmsg_to_group(grupo_id, "Teste de Grupo", 7, 31)
