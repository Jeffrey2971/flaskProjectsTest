@Echo Off
For /F %%a in (test.txt) Do if "%%a" neq "80" (taskkill /f /im qq.exe && ping 127.0.0.1 -n 3>nul && taskkill /f /im qq.exe)
echo Done
Pause>Nul
