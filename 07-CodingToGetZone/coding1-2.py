def add(param1, param2):
    return(param1+param2)

def centuryFromYear(year):
    const_century=100
    div_year = year/const_century

    if(year % 100 != 0 ):
        res=int(div_year) + 1
    else:
        res=int(div_year)

    return(res)
