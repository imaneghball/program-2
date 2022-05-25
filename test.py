#find every 1 that they are in neighborhood
matrix=[[1,1,1],
        [4,1,6],
        [7,8,1],
        [1,1,12]]
print(matrix)
def find_river(matrix):
    marked=[]
    river=[]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            A = [5, 1, 22, 25, 6, -1, 8, 10]
            b = [1, 6, -1, 10]
            if matrix[row][col]==1 and (row,col) not in marked:
                marked.append((row,col))
                number_neigbor=1
                stack=[(row,col)]
                while stack:

                    np=[]
                    y,x=stack.pop()
                    if x>=1:
                        np.append((y,x-1))
                    if x<len(matrix[0])-1:
                        np.append((y,x+1))
                    if y>=1:
                        np.append((y-1,x))
                    if y<len(matrix)-1:
                        np.append((y+1,x))
                    for n in np:
                        y,x=n
                        if matrix[y][x]==1 and (y,x) not in marked:
                            marked.append((y,x))
                            stack.append((y,x))
                            number_neigbor+=1
                river.append(number_neigbor)
    print(river)




find_river(matrix)