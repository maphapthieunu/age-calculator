import os
os.system('cls' if os.name == 'nt' else 'clear')

tuoi = input("nhập số tuổi của bạn: ")

if tuoi.isnumeric():
    print("bạn đã", tuoi, "tuổi rồi")
else:
    print(tuoi, "tuổi là clgv??????")