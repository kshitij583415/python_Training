# Floyd’s Triangle
# Print Floyd’s triangle for N rows:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

count=1
for i in range(4):
    for j in range(i+1):
        print(count, end=" ")
        count+=1

    print()
    
# output
# 1
# 2 3
# 4 5 6
# 7 8 9 10