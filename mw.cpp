/*
	This is a c++ file to improve move window function
*/
#include <Windows.h>

extern "C" {
	HWND gethwnd() {
		return FindWindow(NULL, "CTT");
	}
	
	void Dragging(int eventx, int eventy) {
		HWND hwnd = gethwnd();
		SetWindowPos(hwnd, NULL, 0, 0, eventx, eventy, SWP_NOSIZE);
	}
	int main() {
		SetWindowPos(gethwnd(), NULL, 0, 0, 0, 0, SWP_NOSIZE); // Init window pos
		Dragging(114, 514);
		return 0;
	}
}
