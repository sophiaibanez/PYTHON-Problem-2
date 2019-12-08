import math

x1 = float(input('Enter value for X1:  '));
y1 = float(input('For Y1:  '));
x2 = float(input('For X2:  '));
y2 = float(input('For Y2:  '));
x3 = float(input('For X3:  '));
y3 = float(input('And for Y3:  '));
print('Points: ( %.4f , %.4f ), ( %.4f , %.4f ) and ( %.4f , %.4f ).'  %(x1,y1,x2,y2,x3,y3))

A = x1*(y2-y3) - y1*(x2-x3) + x2*y3 - x3*y2;
D = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1);
E = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2);
F = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2);

h = -(D/(2*A));
k = -(E/(2*A));
r = math.sqrt((D**2 + E**2 -4*A*F)/(4*A**2));
print('Given 3 points, the circle formed has its at center ( %.4f , %.4f ) with radius of %.4f units. \n' %(h,k,r))
print('The vector would be: V[ %.4f , %.4f , %.4f]. \n' %(D/A,E/A,F/A))
