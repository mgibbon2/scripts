Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c WF.bat"
oShell.Run strArgs, 0, false