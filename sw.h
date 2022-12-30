#ifndef SW_H
#define SW_H

void setwindow();
#endif
void setwindow() {
	// Find the hwnd of the window
	HWND hwnd = FindWindow(NULL, "CTT");
	// Set Window long
	SetWindowLong(hwnd, GWL_EXSTYLE, WS_EX_TOOLWINDOW | WS_EX_APPWINDOW); // What I improved in 1.0.5.6
	// SetWindowLong(hwnd, GWL_STYLE, WS_CLIPSIBLINGS | WS_BORDER); // What I improvoed in 1.0.5.5
	// 1.0.5.5 Status : Failed
}
