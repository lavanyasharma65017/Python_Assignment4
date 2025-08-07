try:
     file1=open("sample.txt", "r")
     x=file1.read()
     print(x)
     file1.close()
except FileNotFoundError:
    print("The file \'sample.txt\' was not found.")
