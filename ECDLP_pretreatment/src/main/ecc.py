# ECC在Fp域上加法、倍乘运算

# 求value在Fp域的逆——用于分数求逆
# 可用扩展欧几里得优化
'''
def get_inverse(value, p):
    for i in range(1, p):
        if (i * value) % p == 1:
            return i
    return -1
'''

'''
Attention：所有坐标(x,y)都是以list表示[x,y]
'''

def get_inverse(a, b):  # b表示需要输取模的质数
    old_s, s = 1, 0
    old_r, r = a, b
    if b == 0:
        print('MOD不可为0！')
        return
    else:
        while (r != 0):
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
    return old_s % b


# 求最大公约数——用于约分化简
def get_gcd(x, y):
    if y == 0:
        return x
    else:
        return get_gcd(y, x % y)


# 计算P+Q函数
def calculate_p_q(x1, y1, x2, y2, a, b, p):
    if x1 == 0 and y1 == 0:
        return [x2 % p, y2 % p]

    if x2 == 0 and y2 == 0:
        return [x1 % p, y2 % p]

    # (x1, y1) + (x1, -y1) = (0, 0)
    if y1 % p + y2 % p == p:
        return [0, 0]

    flag = 1  # 控制符号位

    # 若P = Q，则k=[(3x1^2+a)/2y1]mod p
    if x1 == x2 and y1 == y2:
        member = 3 * (x1 ** 2) + a  # 计算分子
        denominator = 2 * y1  # 计算分母

    # 若P≠Q，则k=(y2-y1)/(x2-x1) mod p
    else:
        member = y2 - y1
        denominator = x2 - x1
        if member * denominator < 0:
            flag = 0
            member = abs(member)
            denominator = abs(denominator)

    # 将分子和分母化为最简
    gcd_value = get_gcd(member, denominator)
    member = member // gcd_value
    denominator = denominator // gcd_value

    # 求分母的逆元
    inverse_value = get_inverse(denominator, p)
    k = (member * inverse_value)
    if flag == 0:
        k = -k
    k = k % p

    # 计算x3,y3
    """
        x3≡k^2-x1-x2(mod p)
        y3≡k(x1-x3)-y1(mod p)
    """
    x3 = (k ** 2 - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    return [x3, y3]


# 计算2P函数
def calculate_2p(p_x, p_y, a, b, p):
    tem_x = p_x
    tem_y = p_y
    p_value = calculate_p_q(tem_x, tem_y, p_x, p_y, a, b, p)
    tem_x = p_value[0]
    tem_y = p_value[1]
    return p_value


# 计算nP函数
def calculate_np(n, p_x, p_y, a, b, p):
    # 快速幂
    # 先把n转换为二进制
    binString = bin(n)[2:]
    # print(binString)
    n = len(binString)
    # 记录结果
    ans = [0, 0]
    now_x, now_y = p_x, p_y
    # 倒叙看二进制
    for i in range(n):
        if i == 0:  # 第一个不用翻倍
            pass
        else:
            now_x, now_y = calculate_2p(now_x, now_y, a, b, p)

        if binString[n - 1 - i] == '1':
            ans = calculate_p_q(ans[0], ans[1], now_x, now_y, a, b, p)

    return ans