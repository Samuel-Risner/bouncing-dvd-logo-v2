copy /v bouncing_dvd_logo.xml %TEMP%
powershell start-process create_task.cmd -verb runas

xcopy images %TEMP%\images /v /s /i
copy /v last_name.txt %TEMP%
copy /v launch.exe %TEMP%
copy /v main.exe %TEMP%
copy /v valid_names.txt %TEMP%

C:
cd %USERPROFILE%

mkdir bouncing_dvd_logo
cd bouncing_dvd_logo

xcopy %TEMP%\images images /v /s /i
copy /v %TEMP%\last_name.txt
copy /v %TEMP%\launch.exe
copy /v %TEMP%\main.exe
copy /v %TEMP%\valid_names.txt

cd %TEMP%
rmdir images /s /q
del last_name.txt /q
del launch.exe /q
del main.exe /q
del valid_names.txt /q

@pause