import sys

delta_version = "0.2a"

a = []

lambda_rl = 0.95
t_st      = [12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.2, 2.2, 2.2, 2.2, 2.1]

print(' ')
print('delta v ', delta_version, ' -      error calculation utility')
print('-------------------------------------------------')
print('n         - number of measurements, 1 < n < 16')
print('l         - scale interval value')
print('a[i]      - one of the measured values')
print('lambda_rl - reliability ratio, is 0.95 by default')
print('t_st      - Student"s ratio value')
print('a_a       - average value of measurements')
print('delta_a   - final absolute error value') 
print('-------------------------------------------------')

n = int(input('n    = '))

if (n < 2) or (n > 15):
      print('-------------------------------------------------')
      sys.exit('Incorrect number of measurements!')

l = float(input('l    = '))

summ_a = 0
    
for i in range(n):
      a.append(input('a[' + str(i + 1) + '] = '))
      a[i] = float(a[i])
      summ_a = summ_a + a[i]

a_a = summ_a / float(n)

summ_a_q = 0

for i in range(n):
    summ_a_q = summ_a_q + (a[i] - a_a)**2

sigma_a_q = summ_a_q / float( n * (n - 1) )

delta_a = ( (t_st[n - 2] * t_st[n - 2] * sigma_a_q) + (lambda_rl * lambda_rl * (l / 2.0) * (l / 2.0)) ) ** (0.5)

print('-------------------------------------------------')
print('lambda_rl = ', lambda_rl)
print('t_st      = ', t_st[n - 2])
print('-------------------------------------------------')
print('summ_a    = ', summ_a)
print('a_a       = ', a_a)
print('summ_a_q  = ', summ_a_q)
print('sigma_a_q = ', sigma_a_q)
print('-------------------------------------------------')
print('a_a       = ', a_a)
print('delta_a   = ', delta_a)

foo = input()

