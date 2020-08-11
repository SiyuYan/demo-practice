#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from collections import Counter


def sockMerchant(n, ar):
    dic = {}
    for item in ar:
        if item in dic:
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1
    new_list = [round(x / 2) for x in list(dic.values())]
    print(sum(new_list))
    return sum(new_list)


def jumpingOnClouds(c):
    result = 0
    index = 0
    while index < len(c):
        if index < len(c) - 2:
            print(c[index + 2])
            if c[index + 2] == 1:
                index = index + 1
                result = result + 1
            if c[index + 2] == 0:
                index = index + 2
                result = result + 1
        else:
            index = index + 1
            result = result + 1

    print(result - 1)
    return result - 1


def repeatedString(s, n):
    other = s[0:n % (len(s))]
    print(s.count('a') * (n // len(s)))
    print(other.count('a'))
    return s.count('a') * (n // len(s) - 1) + other.count('a')


def getSecLar(arr):
    arr.sort()
    return arr[1]


def swap(q, index):
    temp = q[index]
    q[index] = q[index + 1]
    q[index + 1] = temp


def minimumBribes(q):
    round_cnt = {}
    for item in q:
        round_cnt[item] = 0

    for num in range(len(q) - 1, 0, -1):
        for index in range(num):
            if q[index] > q[index + 1]:
                round_cnt[q[index]] = round_cnt[q[index]] + 1
                if round_cnt[q[index]] > 2:
                    print("Too chaotic")
                    return
                swap(q, index)

    total_cnt = 0
    for item in round_cnt:
        total_cnt += round_cnt[item]

    print(total_cnt)
    return total_cnt


def minimumBribesOld(q):
    round_result = 0
    index = 0
    q_chaotic = {}

    for item in q:
        q_chaotic[item] = 0

    for i, item in enumerate(q):
        index = i + 1
        while index < len(q) - 1:
            if q_chaotic[item] > 2:
                print(item, ':')
                print(q_chaotic[item])
                round_result = -1
                return
            elif item > q[index + 1]:
                q_chaotic[item] = q_chaotic[item] + 1
                temp = q[index]
                q[index] = item
                q[i] = temp
                round_result = round_result + 1
            index = index + 1
    if round_result == -1:
        print('Too chaotic')
    else:
        print(round_result)


def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


def hourglassSum(arr):
    i = 0
    j = 0
    max_result = -9 * 7
    while i < 4:
        j = 0
        while j < 4:
            sum_result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + \
                         arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                             j + 1] + arr[i + 2][j + 2]
            j = j + 1
            if sum_result > max_result:
                max_result = sum_result
        i = i + 1
    print(max_result)
    return max_result


def divide_chunks(l, n):
    arrs = []
    for i in range(0, len(l)):
        if (i + n <= len(l)):
            arrs.extend([l[i:i + n]])
    return arrs


def minimumSwap(popularity):
    n = len(popularity)
    arrpos = [*enumerate(popularity)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


def minimumSwaps(popularity):
    arr = popularity
    count = 0
    for i in range(len(arr)):
        while arr[i] != len(arr) - i:
            count = count + 1
            temp = arr[len(arr) - arr[i]]
            arr[len(arr) - arr[i]] = arr[i]
            arr[i] = temp
    return count


def scatterPalindrome(strToEvaluates):
    result = []
    for strToEvaluate in strToEvaluates:
        longest_count = 0
        list = []
        for start in range(len(strToEvaluate) + 1):
            for end in range(start + 1, len(strToEvaluate) + 1):
                list.append(strToEvaluate[start:end])
        for sub_str in list:
            dict = {}
            for word in sub_str:
                if word not in dict:
                    dict[word] = 1
                else:
                    dict[word] = dict[word] + 1
            odd_cnt = 0
            for key, value in dict.items():
                if value % 2 != 0:
                    odd_cnt = odd_cnt + 1
            if odd_cnt <= 1:
                longest_count = longest_count + 1
        result.append(longest_count)
    return result


def solution(A):
    n = len(A)

    result = 0
    for i in range(n - 1):
        if (A[i] == A[i + 1]):
            result = result + 1
    r = -1
    for i in range(n):
        count = 0
        if (i > 0):
            if (A[i - 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        if (i < n - 1):
            if (A[i + 1] != A[i]):
                count = count + 1
            else:
                count = count - 1
        r = max(r, count)
    # print(result + r)
    return result + r


def badge_record(records):
    badge_list = []
    enter_list = []
    exit_list = []
    if not records:
        print('records not array')
    if len(records) == 0:
        print('records length zero')
    else:
        for record in records:
            if record[1] == 'enter' and record[0] in badge_list:
                enter_list.append(record[0])
            if record[1] == 'enter' and record[0] not in badge_list:
                badge_list.append(record[0])
            if record[1] == 'exit' and record[0] not in badge_list:
                exit_list.append(record[0])
            if record[1] == 'exit' and record[0] in badge_list:
                badge_list.remove(record[0])

        enter_result = list(set(badge_list + enter_list))
        print(enter_result)
        print(list(set(exit_list)))


# # def get_student(student_course_pairs):
# #     students = set([])
# #     for item in student_course_pairs:
# #         students.add(item[0])
# #     return students
# #
# #
# # def get_pair_data(student_course_pairs):
# #     pair = {}
# #     student_list = list(get_student(student_course_pairs))
# #     pair_student = list(combinations(student_list, 2))
# #     for student in pair_student:
# #         for courses in student_course_pairs:
# #             if student[0] == courses[0]:
# #                 if student[0] in pair:
# #                     pair[student[0]].add(courses[1])
# #                 else:
# #                     pair[student[0]] = {courses[1]}
# #             if student[1] == courses[0]:
# #                 if student[1] in pair:
# #                     pair[student[1]].add(courses[1])
# #                 else:
# #                     pair[student[1]] = {courses[1]}
# #         print(list(student), intersection(pair[student[0]], pair[student[1]]))
#
#
# def intersection(lst1, lst2):
#     lst3 = [value for value in lst1 if value in lst2]
#     return lst3

# def java_test.test():
def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)  # combine as string


def union(a, b):
    return list(set(a + b))


def intersection(a, b):
    return list(set(a) & set(b))


def test():
    return ''


if __name__ == '__main__':
    test()

    listOfStr = ["hello", "at", "java_test.test", "this", "here", "now", "hello"]
    # obj = {}
    # for item in listOfStr:
    #     if item in obj:
    #         obj[item] = obj[item] + 1
    #     else:
    #         obj[item] = 1
    # for item in range(len(listOfStr)):
    #     print(item)
    #     if listOfStr[item] in obj:
    #         obj[item] = listOfStr[item]
    #     else:
    #         obj[item] = listOfStr[item]
    print(','.join(reversed(listOfStr)))
    # 从头到尾，步长为-1 Sequence[start:end:step] 若start和end都为空，则表示全部元素
    print(listOfStr[::-1])
    print(reverse_a_string_more_slowly(listOfStr))
    test = (2, 2)
    test2 = [2, 2]
    test3 = [2, 8]
    test4 = {'siyu': 5, 'mingxing': 6}
    test5 = {'siyu': 7, '2': 8}
    print({**test4, **test5})
    test4.update(test5)
    print(test4)

    dict = {}
    for x in set(test4).union(test5):
        arr = []
        if test4.get(x):
            arr.append(test4.get(x))

        if test5.get(x):
            arr.append(test5.get(x))

        dict[x] = arr

    print(dict)
    res = [1, 2, 3, 4, 4]
    print([{i: res.count(i)} for i in set(res)])
    print(Counter(res))
    # final_dictionary = {x: [test4.get(x), test5.get(x)] for x in set(test4).union(test5)}
    # print(final_dictionary)
    print(*test, 'b')
    print(*test2, 'b')
    print(test4.values())
    print(test4.items())
    print(test4.keys())

    print(union(test2, test3))
    print(intersection(test2, test3))
    print(test * 4)
    print(set(test))
    print(set(test2))
    print(list(test))
    print(list(test2))
    listofTuples = [("Riti", 11), ("Aadi", 12), ("Sam", 13), ("John", 22),
                    ("Lucy", 90)]
    # studentsDict = dict(listofTuples)
    # studentsDict['Riti'] = studentsDict['Riti'] + 10
    # print(listOfStr[::-1])
    # student_course_pairs_1 = [
    #     ["58", "Linear Algebra"],
    #     ["94", "Art History"],
    #     ["94", "Operating Systems"],
    #     ["17", "Software Design"],
    #     ["58", "Mechanics"],
    #     ["58", "Economics"],
    #     ["17", "Linear Algebra"],
    #     ["17", "Political Science"],
    #     ["94", "Economics"],
    #     ["25", "Economics"],
    #     ["58", "Software Design"],
    # ]
    #
    # student_course_pairs_2 = [
    #     ["42", "Software Design"],
    #     ["0", "Advanced Mechanics"],
    #     ["9", "Art History"],
    # ]
    # dict = {}
    # for course in student_course_pairs_1:
    #     if course[0] in dict:
    #         dict[course[0]].append(course[1])
    #     else:
    #         dict[course[0]] = [course[1]]
    # print(dict)
    # get_pair_data(student_course_pairs_2)

# badge_records_1 = [
#     ["Martha", "exit"],
#     ["Paul", "enter"],
#     ["Martha", "enter"],
#     ["Martha", "exit"],
#     ["Jennifer", "enter"],
#     ["Paul", "enter"],
#     ["Curtis", "exit"],
#     ["Curtis", "enter"],
#     ["Paul", "exit"],
#     ["Martha", "enter"],
#     ["Martha", "exit"],
#     ["Jennifer", "exit"],
#     ["Paul", "enter"],
#     ["Paul", "enter"],
#     ["Martha", "exit"],
# ]
# badge_records_2 = [
#     ["Paul", "enter"],
#     ["Paul", "enter"],
#     ["Paul", "exit"],
# ]
# badge_records_3 = [
#     ["Paul", "enter"],
#     ["Paul", "exit"],
#     ["Paul", "exit"],
# ]
# badge_records_4 = [
#     ["Paul", "exit"],
#     ["Paul", "enter"],
#     ["Martha", "enter"],
#     ["Martha", "exit"],
# ]
# badge_records_5 = [
#     ["Paul", "enter"],
#     ["Paul", "exit"],
# ]
# badge_record(badge_records_5)

# solution([1, 1, 0, 1, 0, 0])
# print(minimumSwaps([3, 1, 2, 4]))
# q = [1, 2, 5, 3, 4, 7, 8, 6]
#
# # q = [2, 5, 1, 3, 4]
# minimumBribes(q)
#
# q = [5, 1, 2, 3, 7, 8, 6, 4]
# minimumBribes(q)
#
# q = [1, 2, 5, 3, 7, 8, 6, 4]
# minimumBribes(q)
# print(res)
# fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
# n = int(input())

# ar = list(map(int, input().rstrip().split()))
# n = 9
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# result = sockMerchant(n, ar)
# c=[0,0,0,1,0,0]
# result = jumpingOnClouds(c)
# s='aba'
# n = 10
# result = repeatedString(s, n)
# arr = [5, 2, 3, 1, 4]
# print(getSecLar(arr))
# fptr.write(str(result) + '\n')
#
# fptr.close()
# arr = [[-9, -9, -9, 1, 1, 1],
#        [0, -9, 0, 4, 3, 2],
#        [-9, -9, -9, 1, 2, 3],
#        [0, 0, 8, 6, 6, 0],
#        [0, 0, 0, -2, 0, 0],
#        [0, 0, 1, 2, 4, 0]]
# result = hourglassSum(arr)
#
# my_list = [ 1, 2, 3, 1, 2 ]
#
# n = 2
#
# x = list(divide_chunks(my_list, n))
# result = []
# for item in x:
#     result.append(min(item))
# print(max(result))
