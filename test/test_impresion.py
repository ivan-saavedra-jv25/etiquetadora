import win32ui
import win32print
import win32con



IMG = "D:/dev/Python/impreso/final_123456789123456789.png"
IMPRESORA = "BIXOLON SLP-TX420 - BPL-Z"


INCH = 1440

hDC = win32ui.CreateDC ()

hDC.CreatePrinterDC (IMPRESORA)
hDC.StartDoc ("Test doc")
hDC.StartPage ()
hDC.SetMapMode (win32con.MM_TWIPS)
hDC.DrawText ("TEST TEST TEST TEST TEST TEST TESTEST \nTEST TEST TEST TEST TEST TESTEST TEST TEST TEST TEST TEST TEST ", (0, INCH * -1, INCH * 8, INCH * -2), win32con.DT_CENTER)
hDC.EndPage ()
hDC.EndDoc ()