#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


Gui, Add, Text, x20 y20 w290 h20 , Enter when your lecture ends:
Gui, Add, Text, x20 y50 w100 h20 , Hour (0-23)
Gui, Add, Edit, vEnd_hour
Gui, Add, Text, x20 y100 w100 h20 , Minute (0-59)
Gui, Add, Edit, vEnd_minute
Gui, Add, Button, Default x20 y160 w84 h30 ,Launch
Gui, Show, x127 y87 h200 w332, Anti-distractor
return


ButtonLaunch:
Gui, Submit
if (RegExMatch(End_hour, "[^0-9]") != 0) or (RegExMatch(End_minute, "[^0-9]") != 0)
{
	MsgBox, You need to enter integers.
	ExitApp
}
if (End_hour < 0 or End_hour > 24 or End_minute < 0 or End_minute > 59)
{
	MsgBox, Your values are out of given range.
	ExitApp
}

MsgBox, Press Ctrl+A to start the program. WARNING: IT WILL BLOCK ALL INPUT UNTIL SELECTED TIME
SysGet, Mon1, Monitor
HalfHeight := (Mon1Bottom/2)
HalfWidth := (Mon1Right/2)
^a::
Loop
{
	if (A_Hour < End_hour or A_Min < End_minute)
	{
		BlockInput, On
		CoordMode, Mouse, Screen
		MouseMove, HalfWidth, 0
	}
	else
	{	
		break
	}
}
BlockInput, Off
Send, {Ctrl}
ExitApp
return



	

