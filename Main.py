car_height = int(input())
car_length = int(input())
man_height = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

human_list = ["XXXXX","X   X","X   X","XXXXX","  X  ","XXXXX"," X X ","X   X"]
for i in range(man_height):
    human_list.insert(6, "  X  ")
human_list2 = human_list.copy()
human_list3 = human_list.copy()

car_list = []
for i in range(car_height):
    if i == 0 or i == car_height -1:
        car_list.append("X" * car_length)
    else:
        car_list.append("X" + " " * (car_length -2) + "X")
car_list2 = car_list.copy()

x_max = 17 + car_length -1
y_max = 8 + man_height
car_drawing_start = y_max - car_height - 3
car_drawing_stop = y_max - 3

for x in range(x_max):

    for y in range(y_max):

        if y < car_drawing_start:
            print(human_list[y])

        elif car_drawing_start <= y < car_drawing_stop:
            if  x <= 10:
                print(human_list[y] + " " * (10 - x) + car_list[y - car_drawing_start])
            else:
                if len(human_list2[y] + car_list2[ y - car_drawing_start]) > 5:
                    if human_list2[y]:
                        human_list2[y] = human_list[y][:15-x]
                        print(human_list2[y] + car_list[y - car_drawing_start])
                    else:
                        car_list2[y - car_drawing_start] = car_list2[y - car_drawing_start][1:]
                        human_list3[y] = human_list[y][len(human_list2[y] + car_list2[ y - car_drawing_start]): ]
                        print(car_list2[y - car_drawing_start] + human_list3[y])
                else:
                    if human_list2[y]:
                        human_list2[y] = human_list[y][:15-x]
                        human_list3[y] = human_list[y][len(human_list2[y] + car_list2[ y - car_drawing_start] ) : ]
                        print(human_list2[y] + car_list[y - car_drawing_start] + human_list3[y])
                    else:
                        car_list2[y - car_drawing_start] = car_list2[y - car_drawing_start][1:]
                        human_list3[y] = human_list[y][len(car_list2[ y - car_drawing_start]) : ]
                        print(car_list2[y - car_drawing_start] + human_list3[y])
        else:
            print(human_list[y])
    print()
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
