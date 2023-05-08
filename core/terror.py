import importlib as il
import glob, os

modules = {}

def executeModule(name, args = None):

    print("\n[*] Executing module '" + name + "'...")
    try:
        modules[name].execute(args)
    except KeyError:
        print("[!] No module named '" + name + "'!")

def scanModules():
    print('[*] Scanning modules...\n')
    os.chdir('modules')
    for mod in glob.glob("*.py"):
        mod_name = mod.split('.')[0]
        modules[mod_name] = il.import_module('modules.' + mod_name)
        print('[+] Successfully imported module: ' + mod_name + '.')
    
    print('\n[*] Scanned ' + str(len(modules)) + ' module(s).\n')
    il.invalidate_caches()

def getModuleArgList(mod_name):
    return modules[mod_name].ARGS