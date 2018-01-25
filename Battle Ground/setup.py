import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\Yongyut\AppData\Local\Programs\Python\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Yongyut\AppData\Local\Programs\Python\Python35\tcl\tk8.6'

executables = [cx_Freeze.Executable("BattleGround.py")]

cx_Freeze.setup(
    name="BattleGround",
    options={"build_exe":{"packages":["pygame"], "include_files":["fire.wav","explosion.wav"]}},
    description = "BattleGround",
    version ='1',
    executables = executables
    )
