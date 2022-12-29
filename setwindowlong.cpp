/*
	This is a file about add thickframe change the window.
	We use function : "SetWindowLong" to change window's attribute.
	
	Functions : setwindowlong, main
	void setwindowlong() {
		<To change the window's attribute>
		no args
	}
	int main() {
		<Main function call>
		no args
	}
*/
#include <Windows.h>
#include <iostream> 
using namespace std;

void setwindowlong() {
	// Find the hwnd of the window
	HWND hwnd = FindWindow(NULL, "CTT");
	// Set Window long
	SetWindowLong(hwnd, GWL_EXSTYLE, WS_EX_TOOLWINDOW | WS_EX_APPWINDOW); // What I improved in 1.0.5.6
	// SetWindowLong(hwnd, GWL_STYLE, WS_BORDER); // What I improvoed in 1.0.5.5
}

int main() {
	// Call the setwindow long to change the window's attribute
	setwindowlong();
	return 0;
}
