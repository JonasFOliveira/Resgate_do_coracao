import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="Resgate do coração",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['Recursos', 'Telas.py', "Sons.py", "Sprites.py", "Mapa_matriz.py", "Mapa.py"]}},

    executables = executables

)