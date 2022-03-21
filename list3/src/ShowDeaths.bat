@echo off
set country=%1
set count=%2
set best=%3
set temp_file_name=temp.txt

for /F "skip=1 tokens=1,6,7" %%a in (Covid.txt) do (
    if %%c equ %country% (
        echo %%b %%a %%c >> %temp_file_name%
    )
)

SortDeaths %temp_file_name%

if %best% equ y (
    Head /S %count% temp_sorted.txt
) else (
    Tail /S %count% temp_sorted.txt
)

del %temp_file_name%
del temp_sorted.txt