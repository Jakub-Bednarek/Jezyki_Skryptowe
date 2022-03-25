set country=%1

(for /F "skip=1 tokens=1,6,7" %%a in (Covid.txt) do (
   if %%c equ %country% (
     echo %%a %%b %%c >> test.txt
   )
)) | sort /o test.txt