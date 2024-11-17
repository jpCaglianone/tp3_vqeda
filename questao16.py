def inverter_string(string, indice=None):
    if indice is None:
        indice = len(string) - 1
    if indice < 0:
        return ""
    return string[indice] + inverter_string(string, indice - 1)

print(inverter_string("recursao"))
