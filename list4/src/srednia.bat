@echo off

set /a sum=0
set /a count=0

setlocal enabledelayedexpansion
for %%a in (%*) do (
    set current_val=%%a
    echo !current_val! | findstr /r "[-][1-9][0-9]* [1-9][0-9]* 0">nul && (
        set /a sum=sum+!current_val!
        set /a count=count+1
    )
)

if %count% gtr 0 (
    set /a sum=sum*1000
    set /a count=count
    set /a avg=!sum! / !count!
    echo !avg:~0,-3!.!avg:~-3!
) else (
    echo 0.000
)