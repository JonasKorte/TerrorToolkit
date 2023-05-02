import importlib as il
import glob, os

modules = {}

def executeModule(name, args = None):
    try:
        modules[name].execute(args)
    except KeyError:
        print("[!] No module named '" + name + "'!")

def scanModules():
    print('[*] Scanning modules...\n')
    os.chdir('modules')
    for mod in glob.glob("*.py"):
        mod_name = mod.split('.')[0]
        imported_mod = il.import_module('modules.' + mod_name)
        modules[imported_mod.NAME] = imported_mod
        print('[+] Successfully imported module: ' + mod_name + '.')
    
    print('\n[*] Scanned ' + str(len(modules)) + ' module(s).\n')
    il.invalidate_caches()