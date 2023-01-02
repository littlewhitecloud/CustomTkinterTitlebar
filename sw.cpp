/*
	This is a file about add some long value to change the window.
	Use function : "SetWindowLong" to change window's attribute.
	Function in sw.h
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
	Function in sw.cpp
	Include : sw.h
	int main() {
		no args
	}
*/
#include "windows.h"
extern "C" {
	HWND gethwnd() {
		// Get hwnd by FindWindow
		HWND hwnd = FindWindow(NULL, L"CTT");
		return hwnd;
	}
	void setwindow() {
		// Find the hwnd of the window
		HWND hwnd = gethwnd(); // Get hwnd
		SetWindowLong(hwnd, GWL_EXSTYLE, WS_EX_TOOLWINDOW | WS_EX_APPWINDOW); // What I improved in 1.0.5.6
		// SetWindowLong(hwnd, GWL_STYLE, WS_CLIPSIBLINGS | WS_BORDER); // What I improvoed in 1.0.5.5
	}
	int main() {
		setwindow();
	}
}
