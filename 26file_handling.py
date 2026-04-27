# # Write to a File
# f=open("26file.txt",'+w')
# f.write("_mr._.jaga")
# f.close()

# # Read from a File
# f=open("26file.txt",'r')
# print(f.read())
# f.close()

# # Read Only First 5 Characters
# f=open("26file.txt",'r')
# print(f.read(3))
# f.close()

# # Read One Line
# f=open("26file.txt",'r')
# print(f.readline())
# f.close()

# # Read File Line by Line using Loop
# f=open("26file.txt",'r')
# for i in f:
#     print(i)
# f.close()

# # Append to a File
# f=open("26file.txt",'a')
# f.write("\nthis is append text")
# f.close()

# # Delete a File
# import os
# if os.path.exists("26file.txt"):
#     os.remove("26file.txt")

# # Real Life Example: Logging Errors
# try:
#     a=10/0
#     print(a)
# except Exception as e:
#     f=open("26error_log.txt",'a')
#     f.write(f'\n{str(e)}')
#     f.close()

# # task
# enter=str(input("enter the mode: "))
# def read():
#     f=open("26file.txt",'r')
#     print(f.read())
#     f.close()
# def write():
#     text=str(input("enter content:"))
#     f=open("26file.txt",'w')
#     f.write(f'\n{text}')
#     f.close()
# def append():
#     text=str(input("enter content:"))
#     f=open("26file.txt",'a')
#     f.write(f'\n{text}')
#     f.close()
# def invalid():
#     print(f"invalid input '{enter}'")

# if enter.lower()=='r':
#     read()
# elif enter.lower()=='w':
#     write()
# elif enter.lower()=='a':
#     append()
# else:
#     invalid()

# task 2
enter_file=str(input("enter the file: "))
# import os
# if os.path.exists(enter_file):
#     print(f"file '{enter_file}' exists and do you want to open it?")
#     choice = input("Enter 'y' to open: ")
#     if choice.lower() == 'y':
#         f=open(enter_file,'r')
#         print(f.read())
#         f.close()
#     else:
#         print("invalid choice")
# else:
#     print(f"file '{enter_file}' does not exist and do you want to create it?")
#     choice = input("Enter 'y' to create: ")
#     if choice.lower() == 'y':
#         f=open(enter_file,'w')
#         content=str(input("enter the content: "))
#         f.write(content)
#         f.close()
#         print(f"file '{enter_file}' do you want to read it?")
#         choice1 = input("Enter 'y' to read: ")
#         if choice1.lower()=='y':
#             f=open(enter_file,'r')
#             print(f.read())
#             f.close()

print(f"file '{enter_file}' do you want to count it?")
choice2=input("Enter 'y' to count: ")

def count_the_file():
    vowel='aeiouAEIOU'
    v_count=0
    c_count=0
    s_count=0
    n_count=0
    f=open(enter_file,'r')
    f1=f.read()
    for i in f1:
        if i in vowel:
            v_count=v_count+1
        elif i.isalpha():
            c_count=c_count+1
        elif i.isspace():
            s_count=s_count+1
        elif i.isdigit():
            n_count=n_count+1
    print(f"Vowels: {v_count}")
    print(f"Consonants: {c_count}")
    print(f"Spaces: {s_count}")
    print(f"Digits: {n_count}")
    f.close()
    
if choice2.lower()=='y':
    count_the_file()
else:
    pass
