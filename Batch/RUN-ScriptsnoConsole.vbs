Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c RUN-Scripts.bat"
oShell.Run strArgs, 0, false