from main.compress import decompress, compress
from main.ecc import calculate_np
from main.message import messageDecrypt

p =  0x800000000000000000000000000000000000012b
a =  -0x3
b =  0x74f


compress_Q_a = ['0x43835d772f7dd4f90399fb35645538bb487f22cd', 0]
Q_a = decompress(compress_Q_a, a, b, p)

compress_P = ['0x25e3ea3957e945a871b9ceb6ff1659e15e325167', 1]
P = decompress(compress_P, a, b, p)

print('Q_a: ' + str(Q_a))
# [242592654818096921574850598594616993156682296768, 511009546065983018949123123082211609567208145765]
print('compress_Q_a: ' + str(compress(Q_a)))


print('P: ' + str(P))
# [652884557691898814847358937071207013703943476307, 88459790570409444739528863763799759742520872878]
print('compress_P: ' + str(compress(P)))

n_a = 48904402892901392785196496554897029798167881093
cal_Q = calculate_np(n_a, P[0], P[1], a, b, p)
print('cal_Q: ' + str(cal_Q))

compress_C1 = ['0x3a7b6c5df7a1d54b871e410d8d7b4d37c60f98ad', 0]
C1 = decompress(compress_C1, a, b, p)

compress_C2 = ['0x500504db962dcf4bb68a458414ee8a44db0b2c1b', 0]
C2 = decompress(compress_C2, a, b, p)

message, index = messageDecrypt(C1, C2, n_a, a, b, p)
print(f'【{message}】')
print(index)