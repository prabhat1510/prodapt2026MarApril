try:
    #file =open("d://prodapt2026MarApril//pythonfundamentals//abc.txt","r")
    #with open("d://prodapt2026MarApril//pythonfundamentals//abc.txt", "w") as file:
    with open("d://prodapt2026MarApril//pythonfundamentals//abc.txt", "r") as file:
        file.seek(0)
        print(file.read())
        print("**********************")
        file.seek(15)
        print("**********************")
        print(file.tell())           
        print(file.read())
except FileNotFoundError as e:
    print(e)


######################################
with open("d://prodapt2026MarApril//pythonfundamentals//abc.txt", "r+") as file:
    print(file.read())
    file.write("Lunch Time")
    file.seek(0)
    print("****************")
    print(file.read())