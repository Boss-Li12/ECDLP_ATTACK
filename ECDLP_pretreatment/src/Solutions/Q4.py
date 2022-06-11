from main.compress import decompress, compress
from main.ecc import calculate_np
from main.message import messageDecrypt

p =  0x8049a325d5a0ed72448756f61ddf54149b7ed883
a =  0x0
b =  0x8


compress_Q_a = ['0x475f5475f46d4a694186e77390aa785fbc947dd3' , 0]
Q_a = decompress(compress_Q_a, a, b, p)

compress_P = ['0x1e3b0742ebf7d73ff1a781164c46739a153663f3' , 1]
P = decompress(compress_P, a, b, p)

print('Q_a: ' + str(Q_a))
# [242592654818096921574850598594616993156682296768, 511009546065983018949123123082211609567208145765]
print('compress_Q_a: ' + str(compress(Q_a)))


print('P: ' + str(P))
# [652884557691898814847358937071207013703943476307, 88459790570409444739528863763799759742520872878]
print('compress_P: ' + str(compress(P)))