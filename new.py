def is_palin(sinp):
    return sinp == sinp[::-1]

if __name__=="__main__":
    sinp = input("Введите строку: ")
    print(is_palin(sinp))