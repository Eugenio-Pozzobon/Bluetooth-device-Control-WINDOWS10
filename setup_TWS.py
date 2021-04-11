import subprocess, os

input("GARANTA QUE SEU FONE BLUETOOTH ESTÁ CONECTADO! \nPressione Enter para continuar")

print("\nMapeando Dispositivo e Serviços...\n")

result = subprocess.run('btdiscovery -s"%si%"', stdout=subprocess.PIPE)

mac_adress = result.stdout[1:18]
mac_adress_decode = mac_adress.decode("utf-8")
print("ENDEREÇO DO DISPOSITIVO: " + mac_adress_decode)

result_split = result.stdout.split(b'\r\n')
SERVICE_UUID = []
for result in range(1, len(result_split)-1):
	SERVICE_UUID.append(result_split[result].decode("utf-8"))


print("SERVIÇOS BLUETOOTH USADOS PELO FONE: " + ','.join(SERVICE_UUID))

#input file
tws_start_origin_file = open("src/TWS_Start.bat", "rt")
tws_end_origin_file = open("src/TWS_Stop.bat", "rt")

#output file to write the result to
try:
	os.remove("TWS_Start.bat")
	os.remove("TWS_Stop.bat")
except:
	pass

tws_start_out_file = open("TWS_Start.bat", "at")
tws_end_out_file = open("TWS_Stop.bat", "at")

def append_uuid(file):
	for UUID in SERVICE_UUID:
		file.write('set SERVICE_UUID=' + UUID + '\n')

def append_remove_comand(file):
	for UUID in SERVICE_UUID:
		file.write('btcom -b ' + mac_adress_decode + ' -r -s' + UUID + '\n')

def append_connect_comand(file):
	for UUID in SERVICE_UUID:
		file.write('btcom -b ' + mac_adress_decode + ' -c -s' + UUID + '\n')

#for each line in the input file
counter = 0
print('\nCriando Arquivos de Script...')
for line in tws_start_origin_file:
	counter +=1
	#read replace the string and write to output file
	tws_start_out_file.write(line.replace('XX:XX:XX:XX:XX:XX', mac_adress_decode))
	if counter == 23:
		append_uuid(tws_start_out_file)
		append_remove_comand(tws_start_out_file)
		append_connect_comand(tws_start_out_file)

counter = 0
for line in tws_end_origin_file:
	counter +=1
	#read replace the string and write to output file
	tws_end_out_file.write(line.replace('XX:XX:XX:XX:XX:XX', mac_adress_decode))
	if counter == 20:
		append_uuid(tws_end_out_file)
		append_remove_comand(tws_end_out_file)

#close input and output files
tws_start_origin_file.close()
tws_start_out_file.close()
tws_end_origin_file.close()
tws_end_out_file.close()

input("\nSETUP COMPLETO!\n"
	  "\nPara se Conectar, rode TWS_Start.bat "
	  "\nPara se Desconectar, rode TWS_Stop.bat\n"
	  "\nPressione Enter para Sair")

# nuitka cmd script to generate exe file:
# py -m nuitka --onefile --windows-company-name=Eugenio --windows-product-version=1.0 setup_TWS.py