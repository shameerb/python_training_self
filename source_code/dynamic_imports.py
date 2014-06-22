lst_modules=['sys', 'os', 're','untangle','asdf']
print lst_modules
modules=map(__import__,lst_modules)
