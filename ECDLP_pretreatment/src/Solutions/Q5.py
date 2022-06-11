from main.compress import decompress, compress
from main.ecc import calculate_np
from main.message import messageDecrypt


p =  0x8c72d321e48aa1419b22f914cb43c112b76d7ae5
a =  0x8c72d321e48aa1419b22f914cb43c112b76d7ae2
b =  0x299ce219b7b01348fc2b5007b6ab1ee1005676f7


compress_Q_a = ['0x386619183dbbf88c748b8d4d65619f59e1967afc' , 0]
Q_a = decompress(compress_Q_a, a, b, p)

compress_P = ['0x3ae61b66adfe7b3c8f06f9d5bbd70a743404a86a' , 0]
P = decompress(compress_P, a, b, p)

print('Q_a: ' + str(Q_a))

print('compress_Q_a: ' + str(compress(Q_a)))


print('P: ' + str(P))
# [652884557691898814847358937071207013703943476307, 88459790570409444739528863763799759742520872878]
print('compress_P: ' + str(compress(P)))