schtasks /create /tn bouncing_dvd_logo /XML %TEMP%\bouncing_dvd_logo.xml
del %TEMP%\bouncing_dvd_logo.xml /q
@pause