# for i in range(3,-1,-1):
#     print(i)
R=2
C=2
    
diffusion_arr = [[[] for _ in range(C)]  for _ in range(R)]
diffusion_arr[0][0].append(2)
print(sum(diffusion_arr[1][0]))
    