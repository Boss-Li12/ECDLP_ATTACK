from main.compress import decompress, compress
from main.ecc import calculate_np
from main.message import messageDecrypt

p =  0xb0000000000000006c5b40000000000010ad7f77
a =  0x7cbc14e5e0a72f05864385397829cbc15a2fe1d6
b =  0xa9cbc14e5e0a72f0bc20f05397829cbc24fd94a8


compress_Q_a = ['0x2a7e3b1a3960ee48d5e74dbb59859e433ead2dc0', 1]
Q_a = decompress(compress_Q_a, a, b, p)

compress_P = ['0x725c5b2943cc60511e0ff0dc2caa3d5b718c5453', 0]
P = decompress(compress_P, a, b, p)

print('Q_a: ' + str(Q_a))
# [242592654818096921574850598594616993156682296768, 511009546065983018949123123082211609567208145765]
print('compress_Q_a: ' + str(compress(Q_a)))


print('P: ' + str(P))
# [652884557691898814847358937071207013703943476307, 88459790570409444739528863763799759742520872878]
print('compress_P: ' + str(compress(P)))
# p.order:1004782375664995756298568018034189678348201721719


# check order
p_order = 1004782375664995756298568018034189678348201721719
res = calculate_np(p_order, P[0], P[1], a, b, p)
print(res)


n_a = 403367162604773449232639253154231932807107417903
cal_Q = calculate_np(n_a, P[0], P[1], a, b, p)
print('cal_Q: ' + str(cal_Q))

compress_C1 = [ '0x5962af303c964f4b538ea857524bd13b8c84c2fb' , 0]
C1 = decompress(compress_C1, a, b, p)

compress_C2 = [ '0x9ff7a0335bb9ad42c5d95d4e956f6410483001a2' , 0]
C2 = decompress(compress_C2, a, b, p)

message, index = messageDecrypt(C1, C2, n_a, a, b, p)
print(f'【{message}】')
print(index)