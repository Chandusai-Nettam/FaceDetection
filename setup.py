import cx_Freeze 
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\kurno\Admin\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\kurno\Admin\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("face_detector.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "face_detector ",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll','krishna.PNG']}},
    version = "1.0",
    description = "Face_Detector | Developed By Sahithi ",
    executables = executables
    )
