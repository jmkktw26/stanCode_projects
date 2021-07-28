"""
File: boggle.py
Name: 李柏諠
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_txt = {}
boggle_list = []
all_ans = []


def main():
    read_dictionary()
    for i in range(1, 5):
        input_w = input(f"{i} row of letters:")
        input_w_list = input_w.lower().split(" ")
        for letter in input_w_list:
            if len(letter) != 1:
                print('Illegal input')
                return None
        boggle_list.append(input_w_list)
    for i in range(len(boggle_list)):
        for j in range(len(boggle_list[0])):
            start_alpha = boggle_list[i][j]
            # find the index
            find_boggle(start_alpha, [i, j], [(i, j)])
    print(f"There are {len(all_ans)} words in total")


def find_boggle(alpha, current, seen_alpha):
    # if len > 4  and find in dict
    if len(alpha) >= 4 and alpha in dict_txt[alpha[0]]:
        if alpha not in all_ans:
            print("Found:" + alpha)
            all_ans.append(alpha)
    # find the neighbor
    for i in range(-1, 2):
        if current[0] + i < 0 or current[0] + i >= len(boggle_list):
            continue
        # find the next neighbor
        for j in range(-1, 2):
            new_idx1 = current[0] + i
            new_idx2 = current[1] + j
            # filter
            if new_idx2 < 0 or new_idx2 >= len(boggle_list[0]) or (new_idx1, new_idx2) in seen_alpha or (
                    i == 0 and j == 0):
                continue
            ans = alpha + boggle_list[new_idx1][new_idx2]
            if has_prefix(ans):
                current = [new_idx1, new_idx2]
                seen_alpha.append((new_idx1, new_idx2))
                find_boggle(ans, current, seen_alpha)
                current = [current[0] - i, current[1] - j]
                # pop
                seen_alpha.pop()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for vocabulary in f:
            if vocabulary[0].strip() not in dict_txt:
                dict_txt[vocabulary[0].strip()] = [vocabulary.strip()]
            else:
                dict_txt[vocabulary[0].strip()].append(vocabulary.strip())


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for vocabulary in dict_txt[sub_s[0]]:
        if vocabulary.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
