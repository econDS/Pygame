import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\DELL\Anaconda3\tcltcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\DELL\Anaconda3\tcltk8.6'

executables = [cx_Freeze.Executable("Krobra King.py")]

cx_Freeze.setup(
    name="Krobra King",
    options={"build_exe":{"packages":["pygame"], "include_files":["apple.png","snakehead.png"]}},
    description = "Krobra King",
    version ='0.1',
    executables = executables
    )
