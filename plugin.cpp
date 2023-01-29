/*
	This is a file improve move window function and add some long value to change the window.
	Include : windows.h
	Compile with : plugin.def
	__declspec(dllexport) void move(HWND hwnd, int x, int y, int eventx, int eventy) {
		<move window's funcition>
		x, y, eventx, eventy : int
		"x : windowx | y : windowy | eventx : mousex | eventy : mousey"
	}
	__declspec(dllexport) void setwindowlong(HWND hwnd) {
		<To change the window's attribute>
		hwnd : HWND
	}
*/
#include <windows.h>
#pragma comment(lib, "user32.lib")

__declspec(dllexport) inline void move(HWND hwnd, int x, int y, int eventx, int eventy) { SetWindowPos(hwnd, NULL, eventx + x, eventy + y, 0, 0, SWP_NOREDRAW | SWP_NOSIZE | SWP_SHOWWINDOW); } // x : windowx | y : windowy | eventx : mousex | eventy : mousey

__declspec(dllexport) void setwindow(HWND hwnd) {
	SetWindowLong(hwnd, GWL_EXSTYLE, WS_EX_APPWINDOW);
	SetWindowLong(hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME);
}
