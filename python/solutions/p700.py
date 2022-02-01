# eulercoins


A = 1504170715041707
B = 4503599627370517

candidate = A
eulercoins = [A]

while True:
    candidate += A
    candidate %= B
    if candidate < eulercoins[-1]:
        eulercoins.append(candidate)
        print("sum eulercoins = {}\t smallest eulercoin = {}".format(sum(eulercoins),eulercoins[-1]))

        while eulercoins[-2] - eulercoins[-1] <= eulercoins[-1]:
            candidate -= eulercoins[-2] - eulercoins[-1]
            eulercoins.append(candidate)
            print("sum eulercoins = {}\t smallest eulercoin = {}".format(sum(eulercoins),eulercoins[-1]))



# m = B - A
# candidate = B 
# eulercoins = [A]
# 
# while True:
#     if candidate > (eulercoins[-1] + m:
#         candidate -= m * ((candidate - eulercoins[-1]) // m)
#     else:
#         candidate -= m
#         candidate %= B
#     if candidate < eulercoins[-1]:
#         eulercoins.append(candidate) 
#         if len(eulercoins) > 1:
#             m = eulercoins[-2] - eulercoins[-1]
#         print("sum eulercoins = {}\t smallest eulercoins = {}".format(sum(eulercoins),eulercoins[-1]))
