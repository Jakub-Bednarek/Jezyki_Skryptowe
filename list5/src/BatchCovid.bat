@echo off

set country=%1
set month=%2
set /a sum=0

for /f "skip=1 tokens=3,5,7" %%a in (Covid.txt) do (
    if %%c equ %country% (
        if %%a equ %month% (
            set /a sum=sum+%%b
        )
    )
)

echo %sum%