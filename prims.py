import sys
def prim_mst(graph,v):
    selected=[False]*v 
    selected[0]=True
    total_cost=0
    print("Edge\tWeight")
    
    for _ in range(v-1):
        minimum= sys.maxsize
        x=0
        y=0
        
        for i in range(v):
            if selected[i]:
                for j in range(v):
                    if (not selected[j]) and graph[i][j]:
                        if minimum >graph[i][j]:
                            minimum=graph[i][j]
                            x=i
                            y=j
        print(f"{x}-{y}\t{graph[x][y]}")
        total_cost+=graph[x][y]
        selected[y]=True
        print("\n totalcost",total_cost)
graph =[
    [0,2,0,6,0],
    [2,0,3,8,5],
    [0,3,0,0,7],
    [6,8,0,0,7],
    [0,5,7,9,0]
]
v=5
prim_mst(graph,v)

                    