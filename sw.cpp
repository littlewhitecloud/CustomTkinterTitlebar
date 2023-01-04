/*
	This is a file about add some long value to change the window.
	Use function : "SetWindowLong" to change window's attribute.
	Include : windows.h
	HWND gethwnd() {
		<Get target window's hwnd and return it>
		no args
		hwnd : HWND
	}
	void setwindowlong() {
		<To change the window's attribute>
		no args
	}
	int main() {
		no args
	}
*/
#include "windows.h"
HWND gethwnd() {
	// Get hwnd by FindWindow
	return FindWindow(NULL, "Titlebar Demo");
}
void setwindow() {
	// Find the hwnd of the window
	HWND hwnd = gethwnd(); // Get hwnd
	SetWindowLong(hwnd, GWL_EXSTYLE, WS_EX_APPWINDOW); // What I improved in 1.0.5.6
	SetWindowLong(hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME); // What I improvoed in 1.0.5.5
}
int main() {
	setwindow();
	return 0;
}
