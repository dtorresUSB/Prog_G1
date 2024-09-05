a=[[0, 2, 9], [19, 18, 18], [15, 1, 13], [5, 17, 14]]

# for i in a:
#     for j in i:
#         print(j)

for idx_1,val_1 in enumerate(a):
    for idx_2, val_2 in enumerate(val_1):
        print(f'el elemento en la posicion {idx_1}{idx_2} es: {val_2}')

    