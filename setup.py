from cx_Freeze import setup, Executable

executables = [Executable("nome_arquivo.py")]

options = {
    "build_exe": {
        "packages": ["idna"],
    }
}

setup(
    name="Nome do seu programa",
    options=options,
    version="1.0",
    description="Descrição do seu programa",
    executables=executables
)
