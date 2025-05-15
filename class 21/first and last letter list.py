def c_l(list1):
    list2 = []
    count = 0

    for i in list1:
        if len(i) > 1 and (i[0] == (i[-1])):
            count += 1

            list2.append(i)

    print('the first an the last characters in', list2)
    return count

list1 = ['anna','bike','ellie','string']

print(f'the words that have the same first and last character are {c_l(list1)}')


            
    