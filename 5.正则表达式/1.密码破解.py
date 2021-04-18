#__author:  Administrator
#date:  2020/3/15
#从N个不同元素中取出m（m≤n）个元素，按照一定的顺序排成一列，
#叫做从N个元素中取出m个元素的一个排列（Arrangement），特别的，当M=N时，这个排列被称作全排列（Permutation）

import itertools
#排列
mylist = list(itertools.permutations([1,2,3,4],3))
print(mylist)
print(len(mylist))

#组合（combination）是一个数学名词。一般地，从n个不同的元素中，任取m（m≤n）个元素为一组，叫作从n个不同元素中取出m个元素的一个组合。我们把有关求组合的个数的问题叫作组合问题
mylist1 = list(itertools.combinations([1,2,3,4],3))
print(mylist1)
print(len(mylist1))

#排列+组合
mylist2 = list(itertools.product((0,1,2,3,4,5,),repeat=4))
print(mylist2)
print(len(mylist2))