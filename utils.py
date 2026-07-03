#Function untuk mengecek apakah text ada di list
#Diambil (dan dimodif) dari https://flexiple.com/python/python-list-contains
def contain_checker(text,li):
    setconverted = set(li)
    exist = text in setconverted
    return exist
