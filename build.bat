echo off
cls

python -m pip install --upgrade pip --user
pip install pillow --user
pip install darkdetect --user
pip install blurwindow --user
cl /Ox /Ot /favor:blend /EHsc /GA /nologo /LD /DEF: plugin.def plugin.c /w /errorReport:none /std:c17 /D "_WINDOWS"
