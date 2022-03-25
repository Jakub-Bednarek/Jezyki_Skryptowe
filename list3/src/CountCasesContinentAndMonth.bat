@echo off
set continent=%1
set /A month=%2
set /A sum=0

for /F "skip=1 tokens=3,5,11" %%a in (Covid.txt) do (
   if %%a equ %month% (
      if %%c equ %continent% (
         set /A sum=sum+%%b
      )
   )
)

@echo Suma przypadkow dla kontynentu %continent% jest rowna: %sum%