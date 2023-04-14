#浅拷贝
import copy

will = ["Will", 28, ["Python", "C#", "JavaScript"]]
wilber = copy.copy(will)

print(id(will))
print(will)
print([id(ele) for ele in will])
print("浅拷贝后的id",id(wilber))
print("浅拷贝后的元素",wilber)
print("浅拷贝后的元素id",[id(ele) for ele in wilber])
will[0] = "Wilber"
will[2].append("CSS")
print("修改后的id",id(will))
print("修改后的元素",will)
print("修改后的元素ID",[id(ele) for ele in will])
print("浅拷贝后的id",id(wilber))
print("浅拷贝后的元素",wilber)
print("浅拷贝后的元素id",[id(ele) for ele in wilber])

# 总结：
# 当对will列表进行浅拷贝，计算机会为wilber列表开辟一块新的内存地址，但是wilber列表中的元素内存地址和will对列表的元素对应的是一个内存地址如果对will
# 列表的第一个值进行修改，那么will的变量id值不会变，而是列表中第一个元素会发生变化，因为will列表的第一个元素为字符串不可变类型，如果发生改变计算机会
# 重新分配给该元素一片新的内存地址。对will列表的第三个元素进行了一个append的操作，但是该元素的id值并没有发生改变，原因是因为该元素是列表可变类型
# 由于wilber列表是由初始化will浅拷贝而来，所以wilber的元素的内存id不会发生改变
# 浅拷贝，修改不可变类型会开辟新的内存地址空间，当元素为可变类型不会开辟新的内存空间

print("##################################################")
#深拷贝
will = ["Will", 28, ["Python", "C#", "JavaScript"]]
wilber = copy.deepcopy(will)
print(id(will))
print(will)
print([id(ele) for ele in will])
print("深拷贝后的id",id(wilber))
print("深拷贝后的元素",wilber)
print("深拷贝后的元素id",[id(ele) for ele in wilber])
will[0] = "Wilber"
will[2].append("CSS")
print("修改后的id",id(will))
print("修改后的元素",will)
print("修改后的元素id",[id(ele) for ele in will])
print("深拷贝后的id",id(wilber))
print("深拷贝后的元素",wilber)
print("深拷贝后的元素id",[id(ele) for ele in wilber])

# 总结：
# 首先对列表will进行了深拷贝得到了wilber列表，计算机会为wilber开辟新的内存空间，和浅拷贝不同的是，wilber中的第三个元素因为是可变类型，当使用深拷贝时
# 计算机会为列表中元素为可变类型的元素划分新的内存地址空间，对will列表中第一个元素进行修改，因为是字符串不可变类型，如果修改后对应的内存地址就会发生变化
# ，这里和浅拷贝是一样的可以发现对will列表中的第三个元素进行了append后，该元素的内存地址并没有发生变化，这里也和浅拷贝是一样的原理，因为列表是可变
# 类型进行修改或者删除都不会改变内存地址
# 深拷贝 当元素为可变类型 计算机会对新产生的深拷贝列表中的可变类型划分一个新的内存空间
