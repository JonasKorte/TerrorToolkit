import core.terror as terror

def main():
    terror.scanModules()
    terror.executeModule('TerrorTest')

if __name__ == '__main__':
    main()