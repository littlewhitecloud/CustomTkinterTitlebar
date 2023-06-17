pip install -r requirements.txt

rem build the dll file if you want, require Visual Studio 2022
rem cl /Ox /Ot /favor:blend /EHsc /GA /nologo /LD /DEF: plugin.def plugin.c /w /errorReport:none /std:c17 /D "_WINDOWS"
