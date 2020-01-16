from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "numpy", "skimage", "matplotlib"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "AutostereogramGenerator",
    options = options,
    version = "0.8",
    description = 'Sample_desc',
    executables = executables
)
