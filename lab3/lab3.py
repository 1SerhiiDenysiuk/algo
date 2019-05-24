def dfs(list_pairs, one_tribe, i):
    j = 0
    while j < len(list_pairs):
        if (list_pairs[j][0] == i):
            person = list_pairs[j][1]
            devide_sex(one_tribe, person)
            list_pairs.pop(j)
            dfs(list_pairs, one_tribe, person)
            j = 0
        else:
            j += 1
    return one_tribe

def split_pairs_on_tribe(list_pairs):
    tribe_peoples = []
    while (len(list_pairs) > 0):
        one_tribe = [[], []]
        if (list_pairs[0][0] % 2 == 0):
            one_tribe[0].append(list_pairs[0][0])
        else:
            one_tribe[1].append(list_pairs[0][0])
        one_tribe = dfs(list_pairs, one_tribe, list_pairs[0][0])
        tribe_peoples.append(one_tribe)
    return tribe_peoples

def devide_sex(one_tribe, person):
    if (person % 2 == 0):
        one_tribe[0].append(person)
    else:
        one_tribe[1].append(person)

def calculate_pairs(list_of_tribe):
    pairs_count = []
    for tribe in list_of_tribe:
        for men in tribe[0]:
            for other_tribe in list_of_tribe:
                if tribe != other_tribe:
                    for women in other_tribe[1]:
                        pairs_count.append([women, men])
    return pairs_count

def input_pairs():
    number_of_pairs = input()
    list_pairs = []
    for i in range(0, int(number_of_pairs)):
        var = input().split()
        list_pairs.append([int(var[0]), int(var[1])])
    return list_pairs


if __name__ == "__main__":
    list_pairs = input_pairs()
    list_of_tribe = split_pairs_on_tribe(list_pairs)
    pairs_count = calculate_pairs(list_of_tribe)
    print("Number of pairs: " + str(len(pairs_count)))
    print("All possible pairs: " + str(pairs_count))