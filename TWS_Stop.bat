@echo  off

rem   The following line is needed only if you haven't added Bluetooth Command Line Tools to system PATH
rem   set PATH=c:\program files\bluetooth command line tools\bin;%PATH%

rem   Change the following 2 lines to match your device
set DEVICE_ADDRESS=D3:F8:F3:80:A7:16

rem   If your device requires PIN code other than '0000', uncomment and change the following line
rem set PIN=1234

rem   Remove the device. Ignoring possible error here 
rem   btpair -u -b"%DEVICE_ADDRESS%"

rem   Pair the device
rem   btpair -b"%DEVICE_ADDRESS%"
rem   if errorlevel 1 goto error

rem   Desable the service

set SERVICE_UUID=110D
set SERVICE_UUID=110E
set SERVICE_UUID=111E
btcom -b D3:F8:F3:80:A7:16 -r -s110D
btcom -b D3:F8:F3:80:A7:16 -r -s110E
btcom -b D3:F8:F3:80:A7:16 -r -s111E

powershell -executionpolicy remotesigned -command .\bluetooth.ps1 -BluetoothStatus Off

goto success

rem   Allow user to read error message before window is closed
:error
pause
exit

:success
exit