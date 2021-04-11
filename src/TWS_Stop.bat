@echo  off

rem   The following line is needed only if you haven't added Bluetooth Command Line Tools to system PATH
rem   set PATH=c:\program files\bluetooth command line tools\bin;%PATH%

rem   Change the following 2 lines to match your device
set DEVICE_ADDRESS=XX:XX:XX:XX:XX:XX

rem   If your device requires PIN code other than '0000', uncomment and change the following line
rem set PIN=1234

rem   Remove the device. Ignoring possible error here 
rem   btpair -u -b"%DEVICE_ADDRESS%"

rem   Pair the device
rem   btpair -b"%DEVICE_ADDRESS%"
rem   if errorlevel 1 goto error

rem   Desable the service


powershell -executionpolicy remotesigned -command .\bluetooth.ps1 -BluetoothStatus Off

goto success

rem   Allow user to read error message before window is closed
:error
pause
exit

:success
exit