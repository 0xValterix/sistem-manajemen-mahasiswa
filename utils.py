#Function untuk mengecek apakah text ada di list
#Diambil (dan dimodif) dari https://flexiple.com/python/python-list-contains
def contain_checker(text,li):
    setconverted = set(li)
    exist = text in setconverted
    return exist

#Function untuk mengecek apakah input adalah sebuah angka
#Diambil (dan dimodif) dari https://stackabuse.com/python-check-if-variable-is-a-number/
def is_number(num):
    try:
        tmp = int(num)
        return True
    except:
        return False
