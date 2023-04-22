import os

def _user_info():
    data = dict()

    count = input("How many Cases should be generated? ")
    try: data['count'] = int(count)
    except: raise TypeError
    
    defaultvalue = input("What should be the default value? ")
    if str(defaultvalue) == "": defaultvalue = 2
    else:
        try: data["defaultval"] = int(defaultvalue)
        except: raise TypeError
    
    return data

def _write_init(): return "def iseven(zahl:int) -> str:\n"

def _write_statement(count:int):
    evenoddstr = "even" if count % 2 == 0 else "odd"
    if count == 1: statement = f"  if zahl == {count}:\n    return '{str(evenoddstr)}'\n"
    else: statement = f"  elif zahl == {count}:\n    return '{str(evenoddstr)}'\n"

    return statement

def _write_closing(default:int): return f"""\n\ndef main():\n  zahl = {default}\n  print(f"{{zahl}} is {{iseven(zahl)}}")\n\nif __name__ == '__main__': main()\n"""

def _write_script_to_disk(script:str, name:str='example', folder:str='tmp') -> None:
    if not os.path.exists(folder): os.makedirs(folder)   
    with open(f'{folder}/{name}.py', 'w') as file: file.write(script)

def main():
    data = _user_info()
    
    script = ""
    script += _write_init()
    for count in range(1, data["count"]+1):
        script += _write_statement(count)
    script += _write_closing(data["defaultval"])

    _write_script_to_disk(script, 'myscript', 'tmp')

if __name__ == '__main__': main()
