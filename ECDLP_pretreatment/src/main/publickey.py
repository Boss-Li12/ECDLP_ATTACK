from main.compress import decompress
from main.ecc import calculate_np

def getPublicKey(P, n_a, a, b, p):
    '''
    p_x:完整坐标
    p_y:压缩形式
    P = [p_x, p_y]
    n_a:私钥
    输出Q_a为公钥，其中Q_a = n_a * P
    '''

    # 把P解压缩
    decompress_P = decompress(P, a, b, p)

    # 计算公钥Q_a
    # calculate_np(n, p_x, p_y, a, b, p)
    Q_a = calculate_np(n_a, decompress_P[0], decompress_P[1], a, b, p)

    return Q_a