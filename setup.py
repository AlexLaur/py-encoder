from cx_Freeze import setup, Executable

with open('README.md', 'r') as f:
    long_description = f.read()


options = {'packages': ['qtawesome', 'PySide2', 'shiboken2']}

setup(
    name = 'PyEncoder',
    version = '1.0.0.0',
    options= {'build_exe': options},
    description = long_description,
    executables = [Executable('launcher.py')],
)