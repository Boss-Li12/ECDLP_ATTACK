from main.cipolla import cipolla
from main.ecc import calculate_np, calculate_p_q
from main.compress import compress


def messageEncrypt(m, index, Q_a, P, k, a, b, p):
    '''

    :param m: 明文（长度为16的str）
    :param index: 明文所在的段落
    :param Q_a: 公钥
    :param P: 基点
    :param k: 随机数
    :param a:
    :param b:
    :param p:
    :return: [C1,C2]其中C1，C2均为压缩形式
    '''


    res = ''

    # 16个字符转成32位16进制
    for c in m:
        res += hex(ord(c))[2:].zfill(2)

    # 补上编号index
    res += hex(ord('0') + index)[2:].zfill(2)

    # 还有24bits，也就是补6个0
    res += '000000'
    res = '0x' + res

    # 得到M3的int形式
    M3 = eval(res)

    # 从M3开始往后找找到合适的xm = M3 + i
    i = 0

    # 循环直到M3 + i 有解
    while len(cipolla((M3 + i) ** 3 + a * (M3 + i) + b, p)) == 0:
        i += 1

    # 得到xm
    xm = M3 + i

    # 可能的ym
    choose_ym = cipolla(xm ** 3 + a * xm + b, p)

    # 要ym < p / 2
    if choose_ym[0] < p / 2:
        ym = choose_ym[0]
    else:
        ym = choose_ym[1]

    # 得到M
    M = [xm, ym]

    # 得到C1
    C1 = calculate_np(k, P[0], P[1], a, b, p)

    # 计算C2
    k_Q_a = calculate_np(k, Q_a[0], Q_a[1], a, b, p)
    C2 = calculate_p_q(M[0], M[1], k_Q_a[0], k_Q_a[1], a, b, p)

    return [compress(C1), compress(C2)]


def messageDecrypt(C1, C2, n_a, a, b, p):
    '''

    :param C1:
    :param C2:
    :param n_a: 私钥
    :param a:
    :param b:
    :param p:
    :return: [原文长度为16的str, index]
    '''

    # cal M
    # M = C2 - n_a * C1
    n_a_C1 = calculate_np(n_a, C1[0], C1[1], a, b, p)
    transform_n_a_C1 = [n_a_C1[0], -n_a_C1[1] % p]
    M = calculate_p_q(C2[0], C2[1], transform_n_a_C1[0], transform_n_a_C1[1], a, b, p)
    xm = hex(M[0])

    # decode M
    ans = ''
    message, index = xm[2:34], xm[34: 36]

    # get message (ans)
    for i in range(16):
        c = message[2 * i: 2 * i + 2]
        c = '0x' + c
        ascii1 = eval(c)
        ans += chr(ascii1)

    # get index
    index = '0x' + index
    index = chr(eval(index))

    return [ans, index]