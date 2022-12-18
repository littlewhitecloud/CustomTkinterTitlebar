import platform
import ctypes

if platform.system() == 'Windows':
    from ctypes.wintypes import  DWORD, BOOL, HRGN, HWND
    user32 = ctypes.windll.user32
    dwm = ctypes.windll.dwmapi


    class ACCENTPOLICY(ctypes.Structure):
        _fields_ = [
            ("AccentState", ctypes.c_uint),
            ("AccentFlags", ctypes.c_uint),
            ("GradientColor", ctypes.c_uint),
            ("AnimationId", ctypes.c_uint)
        ]


    class WINDOWCOMPOSITIONATTRIBDATA(ctypes.Structure):
        _fields_ = [
            ("Attribute", ctypes.c_int),
            ("Data", ctypes.POINTER(ctypes.c_int)),
            ("SizeOfData", ctypes.c_size_t)
        ]


    class DWM_BLURBEHIND(ctypes.Structure):
        _fields_ = [
            ('dwFlags', DWORD), 
            ('fEnable', BOOL),  
            ('hRgnBlur', HRGN), 
            ('fTransitionOnMaximized', BOOL) 
        ]


    class MARGINS(ctypes.Structure):
        _fields_ = [("cxLeftWidth", ctypes.c_int),
                    ("cxRightWidth", ctypes.c_int),
                    ("cyTopHeight", ctypes.c_int),
                    ("cyBottomHeight", ctypes.c_int)
                    ]


    SetWindowCompositionAttribute = user32.SetWindowCompositionAttribute
    SetWindowCompositionAttribute.argtypes = (HWND, WINDOWCOMPOSITIONATTRIBDATA)
    SetWindowCompositionAttribute.restype = ctypes.c_int

def HEXtoRGBAint(HEX):
    alpha = HEX[7:]
    blue = HEX[5:7]
    green = HEX[3:5]
    red = HEX[1:3]

    gradientColor = alpha + blue + green + red
    return int(gradientColor, base=16)

def blur(hwnd, hexColor=False, Acrylic=False, Dark=False, AccentState = 3):
    accent = ACCENTPOLICY()
    accent.AccentState = 3 #Default window Blur #ACCENT_ENABLE_BLURBEHIND

    gradientColor = 0
    
    if hexColor != False:
        gradientColor = HEXtoRGBAint(hexColor)
        accent.AccentFlags = 2 #Window Blur With Accent Color #ACCENT_ENABLE_TRANSPARENTGRADIENT
    
    if Acrylic:
        #accent.AccentState = 4 #UWP but LAG #ACCENT_ENABLE_ACRYLICBLURBEHIND
        accent.AccentState = AccentState # Default window blur, UWP LAG
        if hexColor == False: #UWP without color is translucent
            accent.AccentFlags = 2
            gradientColor = HEXtoRGBAint('#91203801') #placeholder color
	
		
    accent.GradientColor = gradientColor
    
    data = WINDOWCOMPOSITIONATTRIBDATA()
    data.Attribute = 19 #WCA_ACCENT_POLICY
    data.SizeOfData = ctypes.sizeof(accent)
    data.Data = ctypes.cast(ctypes.pointer(accent), ctypes.POINTER(ctypes.c_int))
    
    SetWindowCompositionAttribute(int(hwnd), data)
    
    if Dark: 
        data.Attribute = 26 #WCA_USEDARKMODECOLORS
        SetWindowCompositionAttribute(int(hwnd), data)
