def main():
    file_name = input("File: ")

    #grouping the extenstion type with their category
    if file_name.endswith((".gif",".jpg",".jpeg")): 
        print("image/",end ="") # change the value of endline with nothing
        # split the str into two with "." as separator, then only return the last element
        print(file_name.split(".")[-1]) 
    elif file_name.endswith(("pdf","txt","zip")):
        print("application/",end ="")
        print(file_name.split(".")[-1])
    else:
        print("application/octet-stream")
    
main()