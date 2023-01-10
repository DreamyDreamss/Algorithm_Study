def print_matrix(matrix):    
    for i in matrix:
        #for j in i:
        #print('%3d'% " ".join([str(s) for s in i]) )
        print([str(s) for s in i])

def pros_query(matrix,queries):
    answer = []

    for qry in queries:
    
        x1,y1,x2,y2 = qry[0]-1,qry[1]-1,qry[2]-1,qry[3]-1
        print(x1,y1,x2,y2)
        #print(matrix[x1][y1:y2])
        edge = matrix[x1][y1]
        print(edge)
        sq_list = [edge]
        for idx in range(x1+1,x2+1):
            sq_list.append(matrix[idx][y1])
            matrix[idx-1][y1] = matrix[idx][y1]

        
        #print(sq_list)

        for idx in range(y1+1,y2+1):
            sq_list.append(matrix[x2][idx])
            matrix[x2][idx-1] = matrix[x2][idx]
        
        #print(sq_list)
        for idx in range(x2-1,x1-1,-1):
            sq_list.append(matrix[idx][y2])
            matrix[idx+1][y2] = matrix[idx][y2]
        
        #print(sq_list)
        for idx in range(y2,y1,-1):
            sq_list.append(matrix[x1][idx])
            matrix[x1][idx] = matrix[x1][idx-1]

        matrix[x1][y1+1] = edge

        #print_matrix(matrix)

        answer.append(min(sq_list))


def solution(rows, columns, queries):
    matrix = [[y+(x*(columns)) for y in range(1,columns+1)] for x in range(0,rows)]
    answer = pros_query(matrix,queries)
    return answer
    


solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])