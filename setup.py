from cx_Freeze import setup, Executable

base = None


executables = [Executable("tratar_contatos.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Tratar Contatos",
    options = options,
    version = "1.0",
    description = 'Tratar Contatos',
    executables = executables
)
