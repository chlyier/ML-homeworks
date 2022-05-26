# Gibbs采样


# 参数设置
B = {True: 0.001, False: 0.999}
E = {True: 0.002, False: 0.998}
A = {(True, True): {True: 0.95, False: 0.05}, 
     (True, False): {True: 0.94, False: 0.06}, 
     (False, True): {True: 0.29, False: 0.71}, 
     (False, False): {True: 0.001, False: 0.999}}
J = {True: {True: 0.90, False: 0.10}, False: {True: 0.05, False: 0.95}}
M = {True: {True: 0.70, False: 0.30}, False: {True: 0.01, False: 0.99}}


# 初始状态序列
S = {'B': True, 'E': False, 'A': True, 'J': True, 'M': False}
print(f"初始状态: {S}")


# 采样
d = 1000
n = 100
gap = 100
for i in range(d + n * gap):
    # B
    P_BT = A[(True, S['E'])][S['A']] * B[True]
    P_BF = A[(False, S['E'])][S['A']] * B[False]
    if P_BT > P_BF:
        S['B'] = True
    else:
        S['B'] = False
    # print(P_BT, P_BF, S['B'])

    # E
    P_ET = A[(S['B'], True)][S['A']] * E[True]
    P_EF = A[(S['B'], False)][S['A']] * E[False]
    if P_ET > P_EF:
        S['E'] = True
    else:
        S['E'] = False
    # print(P_ET, P_EF, S['E'])

    # A
    P_AT = B[S['B']] * \
           E[S['E']] * \
           A[(S['B'], S['E'])][True] * \
           J[True][S['J']] * \
           M[True][S['M']]
    P_AF = B[S['B']] * \
           E[S['E']] * \
           A[(S['B'], S['E'])][False] * \
           J[False][S['J']] * \
           M[False][S['M']]
    if P_AT > P_AF:
        S['A'] = True
    else:
        S['A'] = False
    # print(P_AT, P_AF, S['A'])

    # J
    if S['A']:
        S['J'] = True
    else:
        S['J'] = False
    # print(S['J'])

    # M
    if S['A']:
        S['M'] = True
    else:
        S['M'] = False
    # print(S['M'])

    if i > d - 1 and i % 100 == 0:
        print(f"第{(i-1000) // 100 + 1}次采样: {S}")

    # exit()
