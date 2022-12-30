/*
	This is a file about add some long value to change the window.
	Use function : "SetWindowLong" to change window's attribute.
	Include : windows.h sw.h
	
	Function in sw.h
	void setwindowlong() {
		<To change the window's attribute>
		no args
		return none
	}
	
	Function in sw.cpp
	int main() {
		<Main function call>
		no args
		return 0
	}
*/
#include <Windows.h>
#include "sw.h"

int main() {
	setwindow(); // Easy to use~
	return 0;
}
