call .venv\Scripts\activate
cd package
del /Q .\dist\*.*
py -m build --sdist
py -m build --wheel
py -m twine upload dist/* 
cd ..