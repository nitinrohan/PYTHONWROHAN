# A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.  

h1=int(input())
m1=int(input())
s1=int(input())
h2=int(input())
m2=int(input())
s2=int(input())
h1=h1*3600
m1=m1*60
h2=h2*3600
m2=m2*60
t1=h1+m1+s1
t2=h2+m2+s2
print(t2-t1)