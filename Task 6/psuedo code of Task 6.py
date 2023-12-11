# psuedo code
# def EditDistance(s1, s2):
#     int matrix[i,j] = 0
#     for i in range(1,len(s1)):
#         matrix[i,0] = i
#     for j in range(1, len(s2)):
#         matrix[0,j] = j
#     for i in range(1,len(s1)):
#         for j in range(1, len(s2)):
#             matrix[i,j] = min(
#                 matrix[i-1,j] + 1,
#                 matrix[i, j-1] + 1,
#                 if s1 != s2:
#                     matrix[i-1,j-1] + 1
#                 else:
#                     matrix[i-1,j-1] + 0
#                               )