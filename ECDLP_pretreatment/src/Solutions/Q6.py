from main.compress import decompress, compress
from main.ecc import calculate_np
from main.message import messageDecrypt


p =  0xb77902abd8db9627f5d7ceca5c17ef6c5e3b0969
a =  0x9021748e5db7962e1b208e3949d42ad0388a18c
b =  0x744f47974caabdd8b8192e99da51c87f91cc453e


compress_Q_a = ['0x352ad1b63b37373cb04bf5c7309c1b6c401f7bdb' , 1]
Q_a = decompress(compress_Q_a, a, b, p)

compress_P = ['0x609e413d6e302e1c79664f785bf869d467dd6858' , 1]
P = decompress(compress_P, a, b, p)

print('Q_a: ' + str(Q_a))
# [242592654818096921574850598594616993156682296768, 511009546065983018949123123082211609567208145765]
print('compress_Q_a: ' + str(compress(Q_a)))


print('P: ' + str(P))
# [652884557691898814847358937071207013703943476307, 88459790570409444739528863763799759742520872878]
print('compress_P: ' + str(compress(P)))