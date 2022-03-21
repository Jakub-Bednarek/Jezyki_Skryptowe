@echo off
@rem Wprowadz kraj do wyszukiwan
echo Podaj kraj:
set /p country=

@rem Wprowadz czy brac pod uwage przypadki czy zgony
choice /c PZ /m "Wybierz jedno: (P)rzypadki lub (Z)gony"
set result=%ERRORLEVEL%

@rem Ustaw zmienne pomocnicze
setlocal
set /a sum=0
set /a days=0

for /f "skip=1 tokens=1,3,5,6,7" %%a in (Covid.txt) do (
    if %%e equ %country% (
        if %%b geq 5 (
            if %%b leq 8 (
                set /a days=days+1
                if %result% equ 1 (
                    echo %%a %%e %%c
                    set /a sum=sum+%%c
                ) else (
                    echo %%a %%e %%d
                    set /a sum=sum+%%d
                )
            )
        )
    )
)

set /a average=%sum% / %days%
echo Sumarycznie: %sum%
echo Srednia arytmetyczna: %average%