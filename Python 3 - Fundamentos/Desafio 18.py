import math
a = float(input ('\033[36mDigite um ângulo:'))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))

print ('\033[1;37;46mO cosseno do ângulo {} graus,\n vale:{:.2f} radianos,\nseu seno vale:{:.2f} radianos\n e sua tangente vale: {:.2}\033[m'.format(a, c, s, t))