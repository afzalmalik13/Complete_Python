q = [
'''When the branch of a tree is shaken the ripe fruits gets detached from the branch. This is an example of
A. Newton's first law of motion
B. Newton's second law of motion
C. Newton's third law of motion
D. All the above''',
'''In rectilinear motion, the objects move along
A. Straight line
B. Ellipse
C. Parabola
D. Circle''',
'''The rate of change of momentum of an object is
A. Equal to displacement of the object
B. Directly proportional to the resultant force applied
C. Equal to its mass
D. None of the above''',
'''The path length travelled by a body in a given time interval is known as
A. Distance
B. Velocity
C. Acceleration
D. Moment''',
'''Which of the following situations is true and possible?
A. If the velocity of a body is zero, then the acceleration can be non-zero
B. A body moving at a constant velocity can have acceleration
C. The magnitude of distance and displacement are equal in a circular motion
D. All of the above''',
'''Suppose a boy is moving with a uniform velocity of 10 m/s on a merry-go-round ride. Which of the following is true of the given scenario?
A. The boy is at rest
B. The boy is moving with no acceleration
C. The boy is moving with acceleration
D. The boy is moving with uniform velocity''',
'''What does the slope of the distance-time graph give?
A. Speed
B. Velocity
C. Acceleration
D. Displacement''',
'''The physical quantity that has both magnitude and direction is known as
A. Vectors
B. Scalars
C. Both A and B
D. Neither A or B''',
'''Which of the following is true of a free-falling body?
A. It moves with non-uniform motion
B. It has zero velocity
C. It has constant non-zero acceleration
D. It has non-uniform acceleration''',
'''What does the slope of the velocity-time graph give?
A. Speed
B. Velocity
C. Acceleration
D. Displacement'''
    ]


while 1:
    w = 0            
    print(f"1st Question on your Screen\n\n{q[0]}")
    q1 = str(input('Please select your option: '))
    if q1.upper() == 'A':
        print(f"\n\tYour answer is correct\n")
        w += 1
    if q1.upper() != 'A':
        print('\n\tIncoorect Answer')
        break
        
    print(f"2nd Question on your Screen\n\n{q[1]}")
    q2 = str(input('Please select your option: '))
    if q2.upper()+'a' == 'Aa':
        print('\n\tYour answer is correct\n')
        w += 1
    if q2.upper()+'a' != 'Aa':
        print('\n\tIncoorect Answer')
        break

    print(f"3rd Question on your Screen \n\n{q[2]}")
    q3 = str(input('Please select your option: '))
    if q3.upper() == 'B':
        print('\n\tYour answer is correct\n')
        w += 1
    if q3.upper() != 'B':
        print('\n\tIncoorect Answer')
        break

    print(f"4th Question on your Screen \n\n{q[3]}")
    q4 = str(input('Please select your option: '))
    if q4.upper()+'b' == 'Ab':
        print('\n\tYour answer is correct\n')
        w += 1
    if q4.upper()+'b' != 'Ab':
        print('\n\tIncoorect Answer')
        break

    print(f"5th Question on your Screen \n\n{q[4]}")
    q5 = str(input('Please select your option: '))
    if q5.upper()+'c' == 'Ac':
        print('\n\tYour answer is correct\n')
        w += 1
    if q5.upper()+'c' != 'Ac':
        print('\n\tIncoorect Answer')
        break

    print(f"6th Question on your Screen \n\n{q[5]}")
    q6 = str(input('Please select your option: '))
    if q6.upper() == 'C':
        print('\n\tYour answer is correct\n')
        w += 1
    if q6.upper() != 'C':
        print('\n\tIncoorect Answer')
        break

    print(f"7th Question on your Screen \n\n{q[6]}")
    q7 = str(input('Please select your option: '))
    if q7.upper()+'d' == 'Ad':
        print('\n\tYour answer is correct\n')
        w += 1
    if q7.upper()+'d' != 'Ad':
        print('\n\tIncoorect Answer')
        break

    print(f"8th Question on your Screen \n\n{q[7]}")
    q8 = str(input('Please select your option: '))
    if q8.upper()+'e' == 'Ae':
        print('\n\tYour answer is correct\n')
        w += 1
    if q8.upper()+'e' != 'Ae':
        print('\n\tIncoorect Answer')
        break

    print(f"9th Question on your Screen \n\n{q[8]}")
    q9 = str(input('Please select your option: '))
    if q9.upper()+'a' == 'Ca':
        print('\n\tYour answer is correct\n')
        w += 1
    if q9.upper()+'a' != 'Ca':
        print('\n\tIncoorect Answer')
        break

    print(f"Last Question on your Screen \n\n{q[9]}")
    q10 = str(input('Please select your option: '))
    if q10.upper()+'b' == 'Cb':
        print('\n\tYour answer is correct\n')
        w += 1
    if q10.upper()+'b' != 'Cb':
        print('\n\tIncoorect Answer')
        break
    print("Congratulation, You win the competition")
    if w == 10:
        break
