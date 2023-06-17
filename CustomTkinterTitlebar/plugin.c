/*
	Include : windows.h Compile : plugin.def
	__declspec(dllexport) void move(HWND hwnd, int x, int y, int eventx, int eventy) {
		"x : windowx | y : windowy | eventx : mousex | eventy : mousey"
		< Move window's funcition >
	}
	__declspec(dllexport) void setwindowlong(HWND hwnd) {
		< To change the window's attribute >
	}
*/

#include <windows.h>
#pragma comment(lib, "user32.lib")
__declspec(dllexport) inline void move(HWND hwnd, int x, int y, int eventx, int eventy) { SetWindowPos(hwnd, NULL, eventx + x, eventy + y, 0, 0, SWP_NOREDRAW | SWP_NOSIZE | SWP_SHOWWINDOW); } // x : windowx | y : windowy | eventx : mousex | eventy : mousey
__declspec(dllexport) void setwindow(HWND hwnd) {
	SetWindowLong(hwnd, GWL_EXSTYLE, WS_EX_APPWINDOW);
	SetWindowLong(hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME);
}
