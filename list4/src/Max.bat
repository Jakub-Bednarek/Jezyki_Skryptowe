@echo off
set highest_value=

setlocal enabledelayedexpansion
for %%a in (%*) do (
    set current_val=%%a
    echo !current_val! | findstr /r "[-][1-9][0-9]* [1-9][0-9]*">nul && (
        if !current_val! gtr !highest_value! (
            set /a highest_value=current_val
        )
    )
)

echo %highest_value%