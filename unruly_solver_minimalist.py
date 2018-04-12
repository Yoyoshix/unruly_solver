import numpy as np

H, W = 8, 8
MAP = np.zeros((H, W))
MAP[0][2] = -1
MAP[2][3] = -1
MAP[2][7] = -1
MAP[5][7] = -1
MAP[6][7] = -1
MAP[1][5] = 1
MAP[1][6] = 1
MAP[3][1] = 1
MAP[3][5] = 1
MAP[4][3] = 1
MAP[5][1] = 1
MAP[5][3] = 1
MAP[5][5] = 1
MAP[7][1] = 1
MAP[7][6] = 1

diff = []

print(MAP)
num = input('press enter')

def get_nb_element(array, value):
    total = 0
    shape = array.shape
    for i in range(len(array)):
        if (len(shape) == 2):
            for j in range(len(array[i])):
                total += (array[i][j] == value)
        elif (len(shape) == 1):
            total += (array[i] == value)
    return (total)

def replace_by(array, find, replace):
    shape = array.shape
    for i in range(len(array)):
        if (len(shape) == 2):
            for j in range(len(array[i])):
                if (array[i][j] == find):
                    array[i][j] = replace
        elif (len(shape) == 1):
            if (array[i] == find):
                array[i] = replace
    return (array)

def check_kiss(subarray):
    #print("k", subarray)
    return ((subarray[0] == subarray[2]) * -subarray[0])

def check_two_row(subarray):
    #print("r", subarray)
    return (((subarray[0] == subarray[1]) or (subarray[1] == subarray[2])) * -subarray[1])

def check_range(subarray):
    if (len(subarray) < 3):
        return (None)
    #print(subarray)
    type = 2
    following = 0
    for i in subarray:
        following = (i == type) * (following + 1)
        if (following == 2):
            return (0)
        type = i
    return (1)

def enter_if_possible(i, j):
    min_l = (i-2 >= 0) * (i-2)
    max_l = H - (i+3 <= W) * (H - (i+3))
    min_c = (j-2 >= 0) * (j-2)
    max_c = W - (j+3 <= H) * (W - (j+3))
    #print(i,j,[min_l,max_l],[min_c,max_c])

    MAP[i][j] = -1
    if (check_range(MAP[min_l:max_l, j]) == 0):
        return (1)
    elif (check_range(MAP[i, min_c:max_c]) == 0):
        return (1)

    MAP[i][j] = 1
    if (check_range(MAP[min_l:max_l, j]) == 0):
        return (-1)
    elif (check_range(MAP[i, min_c:max_c]) == 0):
        return (-1)
    return (0)

def rotate90(array):
    he, wi = array.shape
    tmp = np.zeros((wi, he))
    for i in range(len(array)):
        for j in range(len(array[i])):
            tmp[j][-i-1] = array[i][j]
    return (tmp)

def everything(subarray, black, white, pos):
    while (pos < len(subarray) and subarray[pos] != 0):
        pos += 1
    if (pos == len(subarray)):
        if (check_range(subarray) == 1):
            #print(subarray, black, white, pos)
            if (diff[0] == -2):
                for i in range(len(subarray)):
                    diff[i] = subarray[i]
            else:
                for i in range(len(subarray)):
                    if (diff[i] != subarray[i]):
                        diff[i] = 0
    else:
        if (black > 0):
            subarray[pos] = -1
            everything(subarray, black - 1, white, pos + 1)
            subarray[pos] = 0
        if (white > 0):
            subarray[pos] = 1
            everything(subarray, black, white - 1, pos + 1)
            subarray[pos] = 0
    return (diff)


el_left = get_nb_element(MAP, 0)
while (el_left > 0):
    save = el_left
    for j in [-1, 1]:
        for i in range(H):
            if (get_nb_element(MAP[i], j) == int(W/2)):
                MAP[i] = replace_by(MAP[i], 0, -j)
        for i in range(W):
            if (get_nb_element(MAP[:, i], j) == int(H/2)):
                MAP[:, i] = replace_by(MAP[:, i], 0, -j)

    for i in range(H):
        for j in range(W):
            if (MAP[i][j] == 0):
                MAP[i][j] = enter_if_possible(i, j)
            tmp = get_nb_element(MAP, 0)
            if (el_left != tmp):
                el_left = tmp

    if (save == el_left):
        for i in range(H):
            if (get_nb_element(MAP[i], 0) > 2 and save == el_left):
                diff = [-2 for j in range(W)]
                MAP[i] = everything(MAP[i], W/2 - get_nb_element(MAP[i], -1), W/2 - get_nb_element(MAP[i], 1), 0)
                el_left = get_nb_element(MAP, 0)
        for i in range(W):
            if (get_nb_element(MAP[:, i], 0) > 2 and save == el_left):
                diff = [-2 for j in range(H)]
                MAP[:, i] = everything(MAP[:, i], H/2 - get_nb_element(MAP[:, i], -1), H/2 - get_nb_element(MAP[:, i], 1), 0)
                el_left = get_nb_element(MAP, 0)
    else:
        print("Empty squares :", el_left)
print(MAP)
