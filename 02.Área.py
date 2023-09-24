A , B , C = input().split()
A = float(A)
B = float(B)
C = float(C)

tri = A * C / 2
cic = 3.14159 * C**2
tra = (A + B) * C / 2
qua = B**2
ret = A * B

print('TRIANGULO: {:5.3f}'.format(tri))
print('CIRCULO: {:5.3f}'.format(cic))
print(f'TRAPEZIO:{tra: 5.3f}')
print(f'QUADRADO:{qua: 5.3f}')
print('RETANGULO: %5.3f' % (ret))
