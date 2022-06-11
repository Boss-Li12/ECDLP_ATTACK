from main.cipolla import cipolla


def compress(P):
    '''
    :param P: 【x，y】 其中x和y都是int
    :return:  【x，y】 其中x是字符串型的十六进制，y是0或1的int
    '''
    x, y = hex(P[0]), hex(P[1])
    y = 1 if y[-1] in ['1','3','5','7','9','b','d','f'] else 0
    return [x, y]


def decompress(P, a, b, p):
    '''

    :param P: 【x，y】 其中x是字符串型的十六进制，y是0或1的int
    :param a:
    :param b:
    :param p:
    :return:  【x，y】 其中x和y都是int
    '''
    x = eval(P[0])
    fake_y = P[1]
    n = (x ** 3 + a * x + b) % p
    choose_p_y = cipolla(n, p)
    # 获得real_y
    if len(choose_p_y) == 0:
        print('y ** 2 = x ** 3 + a * x + b 的 y 无解！！')
    else:
        if fake_y == 0:
            if choose_p_y[0] % 2 == 0:
                real_y = choose_p_y[0]
            else:
                real_y = choose_p_y[1]
        else:
            if choose_p_y[0] % 2 == 1:
                real_y = choose_p_y[0]
            else:
                real_y = choose_p_y[1]
    return [x, real_y]