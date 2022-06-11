a = 1
b = 0
p = 3009944491747103173592552029257669572283120430367
order = 3009944491747103173592552029257669572283120430368
gx = 2900641855339024752663919275085178630626065454884
gy = 1803317565451817334919844936679231131166218238368

F = GF(p)
k = 2 # min_k E.order() | (p^k-1)
Fy = GF(p^k,'y')

E = EllipticCurve(F,[a,b])
Ee = EllipticCurve(Fy,[a,b])

P = E((gx,gy))
xP = E((0x1ddc663e98edb9e848b66dd961bb555396fa680, 0xdedc439c092188a093b2b887dcbee2abe302934c))

Pe = Ee(P)
xPe = Ee(xP)

R = Ee.random_point()
m = R.order()
d = gcd(m, P.order())
Q = (m//d)*R

assert P.order()/Q.order() in ZZ
assert P.order() == Q.order()

n = P.order()
print('computing pairings')
alpha = Pe.weil_pairing(Q,n)
beta = xPe.weil_pairing(Q,n)

print('computing log')
dd = beta.log(alpha)
print(dd)
