from cx_Freeze import setup, Executable

base = None


executables = [Executable("revisao.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "teste",
    options = options,
    version = "1.0",
    description = 'asd',
    executables = executables
)
