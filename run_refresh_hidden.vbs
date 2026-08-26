' ---------------------------------------------------------------------------
' Windowless launcher for refresh_calendar.bat.
'
' WScript.Shell.Run with intWindowStyle 0 gives a genuinely invisible run -- no
' console flash, unlike "powershell -WindowStyle Hidden". Because nothing is on
' screen, stdout+stderr are appended to refresh.log; that file is the only way
' to see what a nightly run did.
'
' Run() MUST wait (bWaitOnReturn = True). Fire-and-forget makes wscript exit
' immediately, and Task Scheduler then tears down the orphaned process tree --
' the run dies partway with a success exit code and a truncated log. Waiting
' also makes ExecutionTimeLimit and IgnoreNew actually mean something.
'
' Scheduled Task calls:  wscript.exe "<this file>"
' ---------------------------------------------------------------------------
Dim sh, repo, bat, log, cmd, rc
Set sh = CreateObject("WScript.Shell")
repo = "C:\Users\ssagl\repos\sma-outfit-opex"
bat  = repo & "\refresh_calendar.bat"
log  = repo & "\refresh.log"
cmd  = "cmd /c """"" & bat & """ >> """ & log & """ 2>&1"""
rc = sh.Run(cmd, 0, True)     ' 0 = hidden window, True = wait for it to finish
WScript.Quit rc               ' surface the real exit code to Task Scheduler
