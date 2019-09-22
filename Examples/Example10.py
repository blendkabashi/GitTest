
def numeroFjalet(string):
    fjala_max = 0
    fjala = ''
    vargu = []
    vargu = string.split()
    for vlere in vargu:
        vargu.count(vlere)
        if(fjala_max == 0 or fjala_max < vargu.count(vlere)):
            fjala_max = vargu.count(vlere)
            fjala = vlere
    print(fjala+" ma e shpeshta me "+str(fjala_max)+" here.")


filepath = 'C:\\Users\\Fitore Muqaj\\Desktop\\book.txt'

with open(filepath, encoding='utf8') as fileObject:
    string = fileObject.read()
numeroFjalet(string)
