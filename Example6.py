def great(magj):
    for m in range(0,len(magj)):
        magj[m]="The Great "+magj[m].title()
    return magj
def printo_m(magjistaret):
    for m in magjistaret:
        print(m)
magicians=['ardit','james','robin','harden']
magicians_new=great(magicians[:])
printo_m(magicians)
printo_m(magicians_new)