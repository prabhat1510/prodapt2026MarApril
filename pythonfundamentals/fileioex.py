try:
    #file =open("d://prodapt2026MarApril//pythonfundamentals//abc.txt","r")
    #with open("d://prodapt2026MarApril//pythonfundamentals//abc.txt", "w") as file:
    with open("d://prodapt2026MarApril//pythonfundamentals//abc.txt", "a") as file:
        #print(file)
        file.write("Hello all focus please\n")
        file.write("Otherwise mom will scold you all !!!")
except FileNotFoundError as e:
    print(e)