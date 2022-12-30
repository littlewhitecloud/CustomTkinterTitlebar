/*
	This is a file about add some long value to change the window.
	Use function : "SetWindowLong" to change window's attribute.

	Function in sw.h
	Include : windows.h
	HWND gethwnd() {
		<Get target window's hwnd and return it>
		no args
		hwnd : HWND
		return hwnd
	}
	void setwindowlong() {
		<To change the window's attribute>
		no args
		return none
	}
	Function in sw.cpp
	Include : sw.h
	int main() {
		<Main function call>
		no args
		return 0
	}
*/
#include "sw.h"
int main() {
	setwindow();
	return 0;
}
