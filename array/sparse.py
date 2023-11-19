def Sparce(List,n,m):
    counter=0
    for i in range (n):
        for j in range (m):
            if List[i][j]!=0:
                counter+=1 
    Matrix=[[0 for i in range(3)] for j in range(counter+1)] 
    Matrix[0]=[n,m,counter]
    z=1
    for i in range (n):
        for j in range (m):
            if List[i][j]!=0:
                Matrix[z][0]=i
                Matrix[z][1]=j
                Matrix[z][2]=List[i][j]
                z+=1
                
    return Matrix
