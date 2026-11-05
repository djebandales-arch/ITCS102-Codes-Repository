from getpass import getpass

usern = "Djenelle"
pword = "IAMDJE_123"

isLogin = False
print("--------------------------------")
while isLogin == False:
    user = input("Username --> ")
    password = getpass("Password --> ")
    print("--------------------------------")
    if usern == user and pword == password:
        print("======LOGIN SUCCESS HAHAHAHA=====")
        isLogin = True
    else:
        print("======LOGIN FAILED HAHAHAAAHA======")
        isLogin = False
