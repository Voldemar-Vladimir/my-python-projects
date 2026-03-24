from colorama import Fore, Style, Back, init
print(Fore.CYAN)
def __init__():
    pass
if __name__ == "__main__":
    leg=input(": ")
    legenda=leg.split()
    legenda_up=list(map(lambda x: x.upper(),legenda))
    dictWordLen={x:len(x) for x in legenda}
    legenda_sort=list(filter(lambda w: len(w)>5, legenda))
    legenda_up=list(map(lambda x: x.upper(),legenda))
    dictWordLen={x:len(x) for x in legenda}
    legenda_sort=list(filter(lambda w: len(w)>5, legenda))
    print(legenda_up)
    print(legenda_sort)
    print(dictWordLen)
    print(g_legenda)
    print(leg_set)


def __init__():
    pass
def len_str(str):
    return len(str)
def g_str(str):
    list_g="аоуэиыеёюя"
    global g_legenda
    g_legenda=0
    for s in str:
        for g in list_g:
            if g in s:
                g_legenda+=1
    return f"гласных: {g_legenda}"



def set_str(str):
    global leg_set
    leg_set={s for s in str}
    return f"уникальных символов: {len(leg_set)}"

