@echo off
setlocal EnableDelayedExpansion
set LF=^


for /r %%F in (*.txt) do (
    for /f "tokens=8,9 delims=\" %%P in ("%%~pF") do (
        if "%%Q" NEQ "" (
            if "%%~nF" EQU "�������਩" (
                echo %%P\%%Q\%%~nxF
                ren "%%~fF" �������਩_%%Q_%%P.txt
            )
        )
    )
)
