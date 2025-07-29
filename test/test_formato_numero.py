
def formato_numero(_valor):
    return '${:,.0f}-'.format(_valor).replace(",", "@").replace(".", ",").replace("@", ".")





print(formato_numero(9999999))
#El area es: 1.973,92


