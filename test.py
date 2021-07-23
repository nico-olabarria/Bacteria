column_titles = []
colonies = []

for i in range(0, n):
    column_title = 'n_bac_col_' + str(i)
    column_titles.append(column_title)
    colony_size = []
    Pop = int(input('Introduzca la población inicial de la colonia: '))
    rate = int(input('Introduzca el ritmo de crecimiento de la bacteria en la colonia: '))
    for j in range(0, len(time_list)):
        colony_size.append(bacteria_growth_formula(Pop, time_list[j], rate / 100))
    colonies.append(colony_size) 


size = pd.DataFrame(columns = column_titles)
for i in range(0, len(column_titles)):
    size[column_titles[i]] = colonies[i]
print(size)