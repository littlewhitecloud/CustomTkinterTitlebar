/*
	This is a c++ file to improve move window function
	Now finished -- v1.0.0
*/
#include <windows.h>
#pragma comment(lib, "user32.lib")
__declspec(dllexport) HWND hwndlinker() { // char* titlename
	// Just got window's hwnd, will add char* 
	return FindWindow(NULL, "CTT"); // return FindWindow(NULL, titlename);
}
__declspec(dllexport) void moving(int x, int y, int eventx, int eventy) {
	// x : windowx | y : windowy | eventx : mousex | eventy : mousey
	HWND hwnd = hwndlinker(); // Got hwnd
	eventx += x;
	eventy += y;
	SetWindowPos(hwnd, NULL, eventx, eventy, 0, 0, SWP_NOREDRAW | SWP_NOSIZE | SWP_SHOWWINDOW); // Change Window's Pos
}
/*
int main() {
	// SetWindowPos(gethwnd(), NULL, 0, 0, 0, 0, SWP_NOSIZE); // Init window pos
	return 0;
}
*/
