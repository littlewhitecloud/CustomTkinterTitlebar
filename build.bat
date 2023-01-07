echo off
echo You can build dll with this file
echo Require VS 2022
echo If you set the cl.exe in system path, you can use this file to build dll in normal console. 
echo Use x64 Native Tools Command Prompt for VS 2022 to build 64 bit dll
echo Use x86 Native Tools Command Prompt for VS 2022 to build 32 bit dll
echo You can open the command prompt can use "cd" to this path and do ".\build.bat"
echo And the "cl.exe" will build the dll...
cl /LD /DEF: mw.def mw.cpp /std:c++20
pause
