@echo off

cls
title Command Prompt
doskey files=explorer.exe .
doskey clear=cls

set "home_dir=C:%HOMEPATH%"
rem if %home_dir% in $P, replace %home_dir% part of $P with ~

rem space at end is important
prompt [%TIME:~0,8%] $P %USERNAME% =$G 

set "home_dir="

if not defined VisualStudioVersion (
	neofetch
)