from main.compress import decompress, compress
from main.ecc import calculate_np
from main.message import messageDecrypt

p =  0x100000000000000000000000000000000000018f3
a =  0x1
b =  0x0


compress_Q_a = ['0xb69c1c1d4180cbe558799cc71bc5cd72df01d877', 1]
Q_a = decompress(compress_Q_a, a, b, p)

compress_P = ['0x77d0847d0a4b9448433de6eef45cbdf32dc82fdf', 0]
P = decompress(compress_P, a, b, p)

print('Q_a: ' + str(Q_a))
# [242592654818096921574850598594616993156682296768, 511009546065983018949123123082211609567208145765]
print('compress_Q_a: ' + str(compress(Q_a)))


print('P: ' + str(P))
# [652884557691898814847358937071207013703943476307, 88459790570409444739528863763799759742520872878]
print('compress_P: ' + str(compress(P)))