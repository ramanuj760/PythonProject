for row in range(5):
    for col in range(5):
        if (row==0 or row==3 )and(col==2or col==3 ) :
            print("*",end=" ")
        elif(col==0 or col==4)and(row!=0 ):
            print("*",end=" ")
            row=row+1

        else:
            print(end=" ")

    print()