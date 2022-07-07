import numpy as np
def mine_swepeer(bombs,num_rows,num_col):
    table=np.zeros((num_rows,num_col))

    for bombLokation in bombs:
        (bomb_row,bomb_col)=bombLokation
        table[bomb_row,bomb_col]=-1
        if bomb_col+1<num_col and table[bomb_row,bomb_col+1]+1!=0 :
            table[bomb_row,bomb_col+1]+=1
        if bomb_col-1>=0 and table[bomb_row, bomb_col - 1]+1!=0:
            table[bomb_row, bomb_col - 1] += 1
        if bomb_row+1<num_rows and table[bomb_row+1,bomb_col]+1!=0:
            table[bomb_row+1,bomb_col]+=1
        if bomb_row-1>=0 and table[bomb_row-1,bomb_col]+1!=0:
            table[bomb_row-1,bomb_col]+=1
        if bomb_row-1>=0 and bomb_col-1>=0 and table[bomb_row-1,bomb_col-1]+1!=0:
            table[bomb_row-1,bomb_col-1]+=1
        if bomb_row-1>=0 and bomb_col+1<num_col and table[bomb_row-1,bomb_col+1]+1!=0:
            table[bomb_row-1,bomb_col+1]+=1
        if bomb_row+1<num_rows and bomb_col+1<num_col and table[bomb_row+1,bomb_col+1]+1!=0:
            table[bomb_row+1,bomb_col+1]+=1
        if bomb_row+1<num_rows and bomb_col-1>=0 and table[bomb_row+1,bomb_col-1]+1!=0:
            table[bomb_row+1,bomb_col-1]+=1

    print(table)
def mine_swepeer2(bombs,num_rows,num_col):
    table = np.zeros((num_rows, num_col))

    for bombLokation in bombs:
        (bomb_row, bomb_col) = bombLokation
        table[bomb_row, bomb_col] = -1

        row_Range=range(bomb_row-1,bomb_row+2)
        col_Range=range(bomb_col-1,bomb_col+2)
        for i in row_Range:
            for j in col_Range:
                if 0<= i <num_rows and 0<= j < num_col and table[i,j]!=-1:
                    table[i,j]+=1
    print(table)



mine_swepeer(([0,0],[2,2],[2,0],[2,3],[0,1]),3,4)
mine_swepeer2(([0,0],[2,2],[2,0],[2,3],[0,1]),3,4)