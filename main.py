from typing import List

import numpy as np

matrix=[[1,9,1,7],
        [1,5,6,8],
        [1,1,1,7]]



def find_river(matrix):
        market = set()
        river=[]

        for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                        if matrix[row][col] == 1 and (row, col) not in market:
                                market.add((row, col))
                                add_neaber=1
                                stack=[(row,col)]
                                while stack:
                                        x,y=stack.pop()
                                        neabers = neaber((x,y), matrix)
                                        for n in neabers:
                                                #print(market)
                                                if matrix[n[0]][n[1]] == 1 and (n[0],n[1]) not in market:
                                                        market.add(n)
                                                        add_neaber += 1
                                                        stack.append(n)
                                river.append(add_neaber)
        print(river)
        print(market)






def neaber(pos,matrix):
        row,col=pos

        np=[]
        if col >= 1:
                np.append((row,col-1))
        if col < len(matrix[0]) - 1:
                np.append((row,col+1))
        if row >= 1:
                np.append((row-1,col))
        if row < len(matrix) - 1:
                np.append((row+1,col))
        return np

find_river(matrix)

