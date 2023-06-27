# 赋值运算符
# 执行顺序:从右到左
# 支持链式复制:a = b = c = 0;
# 支持参数赋值:+= -= *= /= //= %= ;
# 支持系列解包赋值:a,b,c = 10,20,30 ;


a  = 10 + 5
print(a)

# 链式赋值
# 此时,链式赋值的变量对应的都是同一个内存中的地址

b = c = d = 30
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))


# 参数赋值
e = 20
e += 30
print(e,type(e))

e *= 30
print(e,type(e))

e -= 20
print(e,type(e))

e /= 19
print(e,type(e))

e //= 3
print(e,type(e))


# 解包赋值
f,g,h =20,30,40    # 左右变量的个数要与值的数量一致
print(f,g,h)

# 交换两个变量的值
# 交换之前
j,k = 50,90
print('交换之前:',j,k)


# 交换之后
j,k = k,j
print('交换之后:',j,k)




