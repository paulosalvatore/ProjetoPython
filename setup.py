from cx_Freeze import setup, Executable

executables = [Executable("calculadora.py")]

options = {
    "build_exe": {
        "packages": ["idna"]
    }
}

setup(
    name="Calculadora",
    options=options,
    version="1.0",
    description="Máquina de calcular.",
    executables=executables
)
