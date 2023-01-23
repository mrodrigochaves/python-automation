import os

# Defina a data e hora corretas
date = os.popen("date /T").read().strip()
time = os.popen("time /T").read().strip()

# Use o comando "net" para ajustar a data e hora
os.system("net time /setsntp:pool.ntp.org")
os.system("net time /set /yes")

# Exiba a data e hora atuais
print("Data e hora atual: " + date + " " + time)
