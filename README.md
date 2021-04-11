# TWS Control with Windows 10
[PT-BR Abaixo]

---

Controle Dispositivos TWS como fones de ouvido por meio de um simples clique.
Usando esse software é possível poupar o tempo de abrir as configurações e conectar ou desconectar manualmente o dispostivo quando ele não se conecta automaticamente.

### Guia de Instalação

1. Instale [esse software](https://bluetoothinstaller.com/bluetooth-command-line-tools/BluetoothCLTools-1.2.0.56.exe) disponibilizado [aqui](https://bluetoothinstaller.com/bluetooth-command-line-tools).
2. Instale [esse arquivo](https://github.com/Eugenio-Pozzobon/TWS-DEVICE-CONTROL---WINDOWS10/raw/master/Output/twsControl_installer.exe) ou baixe os arquivos desse repositório.

-> Atente-se para gerar os atalhos da área de trabalho no final.

### Como Utilizar

1. Emparelhe o seu dispositivo primeiro e estabeleça um pareamento inicial.
2. Rode o arquivo 'Setup TWS'. Siga as instruções que aparecerão em sua tela.
3. Pronto! Você pode excluir o atalho 'Setup TWS'. As funções agora estão habilitadas.
4. Se você desejar, é possível criar teclas de atalho no teclado para facilmente conectar/desconectar o dispotivo. 
Para fazer isso, clique no atalho com botão direito. No menu "Atalho", clique sobre a seção de tecla de atalho e clique nas teclas que deseja usar. Finalize clicando em "Aplicar"
5. O aplicativo 'TWS Start' inicia a conexão Bluetooth do computador e realiza o pareamento com o dispotivo configurado antes.
6. O aplicativo 'TWS Stop' encerra os servições Bluetooth com o dispositivo, porém como por vezes isso não é o suficiente para encerrar a conexão, o sistema desativa o bluetooth da sua máquina, garantindo que ocorrerá o despareamento. 

![image](https://user-images.githubusercontent.com/57693382/114294423-e42d7400-9a74-11eb-9548-80e3c2008891.png)

Observação 1: O tempo que o programa precisa para fazer as atividades ocorrerem é relativamente o mesmo que você levaria para realizar a conexão manualmente. O benefício é não ter que ficar repetindo o mesmo trabalho.

Observação 2: É possível que ao rodar o arquivo TWS Start você perceba que o prompt libera uma mensagem de erro, mesmo que conectando o fone. Não se assuste, está tudo bem. Isso acontece pois o programa tenta se conectar em todos os serviços possívels, porém dependendo do fone pode ser que um deles seja um serviço 'oculto' onde a conexão ocorre automaticamente e não precisaria do programa para acontecer, por isso você recebe um erro.

---

### Licença

    TWS Control with Windows 10
    Copyright (C) 2021  Eugênio Piveta Pozzobon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

### Créditos

Agradecimento ao desenvolvedor do script "bluetooth.ps1", descrito [aqui](https://superuser.com/a/1293303/1296346)
Agradecimento ao desenvolvedor da ferramenta de [conexão Bluetooth pela linha de comando](https://bluetoothinstaller.com/bluetooth-command-line-tools/)




