
import sys

def main():
    my_function()

def my_function_for_opening_files():

    header = "*Here are the contents of my file*\n"

    with(open("files/myfile.txt", "r")) as opened_file:
        content =  opened_file.read()
    content = header + content
    print(content)

    
if __name__ == "__main__":  
    main()

