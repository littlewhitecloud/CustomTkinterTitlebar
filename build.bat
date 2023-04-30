echo off
cls
echo You can use this file to build the project
echo Require VS 2022 (C/C++ Install) & Python 3.11.1 (Or lower(Not recommended))

echo Tip
echo If you set the cl.exe in system path, you can use this file to build dll in normal console
echo If not, you can do this:
echo Use x64 Native Tools Command Prompt for VS 2022 to build 64 bit dll
echo Use x86 Native Tools Command Prompt for VS 2022 to build 32 bit dll
echo You can exit and use the command prompt or press any key to continue...
pause

echo Start install the inneed package
python -m pip install --upgrade pip --user
pip install pillow --user
pip install darkdetect --user
pip install blurwindow --user

echo Start building the plugin.dll ...
echo You can open the Developer PowerShell for VS 2022 and use "cd" to this path do ".\build.bat"
echo And the "cl.exe" will build the dll automatic...
cl /Ox /Ot /favor:blend /EHsc /GA /nologo /LD /DEF: plugin.def plugin.c /w /errorReport:none /std:c17 /D "_WINDOWS"
