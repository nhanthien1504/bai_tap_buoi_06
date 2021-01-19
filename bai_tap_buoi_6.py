'''
Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong hướng dẫn
Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Output: {'item1': 1150, 'item2': 300}
'''
#{'item1': 1150, 'item2': 300}
'''Tạo một dic gồm có key là name: item
và value: amount là số lượng +> {'name':'amount'}
'''
# dic = {}
# ls = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# for i in ls:
#     name = i['item']
#     amount = i['amount']
#     if name in dic:
#         dic[name] += amount
#     else:
#         dic[name] = amount
# print(dic)
# học kĩ lại

'''
Viết chương trình đếm số lần xuất hiện các từ đơn trong một đoạn văn bản

'''
# str = input('nhập đoạn văn bản: ')
# print(str.split(' '))
# lst = str.split(' ')
# lst_count=[]
# for w in lst:
#     coun_chart = lst.count(w)
#     lst_count.append(coun_chart)
# print(lst_count)
# print(list(zip(lst,lst_count)))  #DONE

'''
Viết hàm đếm số lần xuất hiện các ký tự trong một String
'''
# str = input('mời nhập đoạn văn bản: ')
# def coun_chart(str):
#     dict = {}
# # key: kí tự của str
# # value: số đếm kí tự   str.count(w)
#     for n in str:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] +=1
#         else:
#             dict[n] = 1
#     return dict
# print(coun_chart(str))


'''
Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Input:
    dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
    keys = ["name", "salary"]
Output:
    {'name': 'Kelly', 'salary': 8000}
https://www.geeksforgeeks.org/python-extract-specific-keys-from-dictionary/
'''
# Cách 1:
# sampleDict = {
#     "name": "Kelly",
#     "age":25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# keys = ["name", "salary"]
# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)
# # xem lại
# Cách 2:
# sampleDict = {
#     "name": "Kelly",
#     "age":25,
#     "salary": 8000,
#     "city": "New york"
# }
# keys = ['name','salary']
# a_dic = {}
# for k in keys:
#     # if k not in a_dic and k in sampleDict:
#     a_dic[k] = sampleDict[k]
# print(a_dic)

'''
Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
Input:
{
    0: 0
    1: 2,
    2: 4,
    -3: -1,
    4: 5,
    5: 3,
    -1: -3,
    -2: 2
}
Output:
{ (5, 3), (2, 4), (4, 5)}
'''
# dic = {
#     0: 0,
#     1: 2,
#     2: 4,
#     -3: -1,
#     4: 5,
#     5: 3,
#     -1: -3,
#     -2: 2
# }
# import collections
# k = collections.Counter(dic)
# print(k)
# high = k.most_common(3)
# print(high)
'''
Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict

'''
# dict1 = {
#     0: 3,
#     1: 2,
#     2: 4,
#     -3: -1,
#     4: 5,
#     5: 3,
#     -1: -3,
#     -2: 2
# }
# dict2 = {
#     0: 1,
#     3: 4,
#     4: 5,
#     5: 3,
# }
# a_dic = {}
# for items1 in dict1:
#     for items2 in dict2:
#         if items1 == items2 and dict1[items1] == dict2[items2]:
#            a_dic[items1] = dict2[items2]
# print(a_dic)
    # print(items1,end=' ') # key dic1
    # print(dict1[items1],end=' ') # valu dic1

'''
Viết chương trình tạo ra dict lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử.
Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
# '''
# dic = {'a':[1,2,3,4,5],'b':[1,2,3,4,5],'c':[1,2,3,4,5]}
#
# n = int(input('moi nhap so phan tu trong dict: '))
# a_dic = {}
# if n > 3:
#     for i in range (n):
#         keys = input(f'moi nhap key thu {i+1}: ')
#         m = int(input('moi nhap so luong trong list value: '))
#         lst = []
#         if m >=5:
#             for j in range(m):
#                 values = int(input(f'moi nhap gia tri thu {j+1} cua key {i}: '))
#                 lst.append(values)
#                 a_dic[keys] = lst
#         else:
#             print('nhap m>=5')
#     print(a_dic)
# else:
#     print('nhap n>3')
# DONE

'''
Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict

'''
# d = {}
# n = int(input(f'moi nhap so phan tu trong dict: '))
# for i in range(n):
#     key = input(f'mời nhập key {i+1}: ')
#     value = input(f'mời nhập value của {key}: ')
#     d[key] = value
#     all_value = d.values()
#     maxx = max(all_value)
#
# print(maxx)