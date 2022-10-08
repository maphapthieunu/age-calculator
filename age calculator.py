import os
os.system('cls' if os.name == 'nt' else 'clear')

tuoi = input("nhập số tuổi của bạn: ")

if tuoi.isnumeric():
    print("bạn đã", tuoi, "tuổi rồi")
elif tuoi > 125:
    print("con chào cụ, sao cụ già dữ v??????")
else:
    print(tuoi, "tuổi là clgv??????")
