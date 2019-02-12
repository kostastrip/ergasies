pl_bomb('Dwse plh8os apo vomves ')
pl_gr('Dwse plh8os apo grammes ')
pl_st('Dwse plh8os apo sthles ')
L=[][]
for i in range(0,pl_gr):
    for i in range(0,pl_st-1):
        L[i][j]='_'
for i in range(0,pl_bomb):
    x=random.randint(0,pl_gr-1)
    y=random.randint(0,pl_st-1)
    L[x][y]='bomb'
    print [L]
