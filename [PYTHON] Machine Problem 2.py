import math

x1 = int(input('Enter value for X1:  '));
y1 = int(input('For Y1:  '));
x2 = int(input('For X2:  '));
y2 = int(input('For Y2:  '));
x3 = int(input('For X3:  '));
y3 = int(input('And for Y3:  '));
print('Points: ( %d , %d ), ( %d , %d ) and ( %d , %d ).'  %(x1,y1,x2,y2,x3,y3))

A = x1*(y2-y3) - y1*(x2-x3) + x2*y3 - x3*y2;
D = (x1**2 + y1**2)*(y3-y2) + (x2**2 + y2**2)*(y1-y3) + (x3**2 + y3**2)*(y2-y1);
E = (x1**2 + y1**2)*(x2-x3) + (x2**2 + y2**2)*(x3-x1) + (x3**2 + y3**2)*(x1-x2);
F = (x1**2 + y1**2)*(x3*y2 - x2*y3) + (x2**2 + y2**2)*(x1*y3 - x3*y1) + (x3**2 + y3**2)*(x2*y1 - x1*y2);

h = -(D/(2*A));
k = -(E/(2*A));
r = math.sqrt((D**2 + E**2 -4*A*F)/(4*A**2));
print('Given 3 points, the circle formed has its at center (%d,%d) with radius of %d units. \n' %(h,k,r))
print('The vector would be: V[%d,%d,%d].\n' %(D/A,E/A,F/A))