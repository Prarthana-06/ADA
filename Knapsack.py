from itertools import combinations
weights=[7,1,2,6]
values=[22,12,30,25]
capacity=10
n=len(weights)
best_value=0
best_subset=None
print("subset\t\t\t total weight\t total value")
print("-"*45)

for r in range(n+1):
    for subset in combinations(range(n),r):
        total_weight=sum(weights[i]for i in subset)
        total_value=sum(values[i] for i in subset)
        subset_display="{"+",".join(str(i+1)for i in subset)+"}"
        if total_weight<= capacity:
            print(f"{subset_display:<15}{total_weight:<15}${total_value}")
            if total_value>best_value:
                best_value=total_value
                best_subset=subset
            else:
                print(f"{subset_display:<15}{total_weight:<15}not feasible")
print("\noptimal solution:")
print("item selected:",{i+1 for i in best_subset})
print("maximum value:$",best_value)