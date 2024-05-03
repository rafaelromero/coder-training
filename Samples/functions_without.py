
import sys



    
if __name__ == "__main__":  
    with(open("files/myfile.txt", "r")) as opened_file:
        content =  opened_file.read()
    content = "!!!! Announcement: Here is what was ready in the myfile text file!!!!1\n" + content
    print(content)