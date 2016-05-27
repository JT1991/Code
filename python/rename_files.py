import os

def rename_files():
    #GET
    file_list = os.listdir(r"C:\Users\Josh\Downloads\prank\prank")
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\Josh\Downloads\prank\prank")
    #SET
    
    for file_name in file_list:
        print ("Old name - " + file_name)
        print ("New name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    print saved_path
rename_files()
    
    

    
