#Mini Project by Vidhiya S B 
print("This is a mini project by Vidhiya S B. Welcome to my Calculator")
import math
#POLYGON
def poly():
    print("Welcome to the polygonal department!")
    print("You have two options \r\n1. The sum of the interior angles\r\n2. Still Thinking")
    poly_choice = int(input("Please choose an option (Only one option 1 works for now"))
    if poly_choice == 1:
        sides = int(input("Please tell me how many side  the polygon has: "))
        step1 = sides - 2
        ans = step1 * 180
        print("The sum of all interior angles is",ans,".")
        ans2 = ans / sides
        print("The measure of each angle is", ans2,".")
#SPHERES
def spheres():
    print("Welcome to the spheres department!")
    print("You have two options\r\n1. Volume of the sphere\r\n2. Surface area")
    sphere_choice = int(input("Please choose an option: "))
    print("")
    if sphere_choice == 1:
        r = float(input("Enter the Radius of the sphere: "))
        test = 4/3
        ans = test * math.pi
        r3 = r*r*r
        ans2 = ans * r3
        print("The answer is", ans2)
    if sphere_choice == 2:
            r = float(input("Enter the Radius of the sphere: "))
            s_area = 4 * math.pi
            r2 = r*r
            surface_area = s_area * r2
            print("The answer is",surface_area)
#TRIANGLES
def triangles():
    print("Welcome to the triangular department!")
    print("")
    print("You have two options\r\n1.Pythagoras (Hypotenuse)\r\n2.Trigonometry\r\n3.Pythagoras (other sides)")
    tri_choice = int(input("Please choose an option: "))
    if tri_choice == 1:
        num1 = float(input("Enter the first side: "))
        num2 = float(input("Enter the second side: "))
        step1 = num1 * num2
        step2 = num2 * num2
        step3 = step1 + step2
        step4 = math.sqrt(step3)
        print("The Answer is",step4)
    if tri_choice == 2:
        print("Welcome to Trigonometry\r\n1.Sine\r\n2.Cosine\r\n3.Tangent\r\n4.Length using Sine\r\n5.Length using Cosine\r\n6.Length using Tangent")
        trig_choice = int(input("Please choose an option: "))
    if trig_choice == 1:
        opp = float(input("Enter the length of the side opposite to the angle: "))
        hyp = float(input("Enter the value of the hypotenuse: "))
        angle = opp / hypotenuse
        ans = math.sinh(angle)
        print("The Answer is",ans)
    if trig_choice == 2:
        adj = float(input("Enter the value of the side adjacent to the angle: ")) 
        hyp = float(input("Enter the value of the hypotenuse: "))
        angle = adj / hypotenuse
        ans = math.cosh(angle)
        print("The answer is",ans)
    if trig_choice == 3:
        adj = float(input("Enter the value of the side adjacent to the angle: "))
        opp = float(input("Enter the value of the side apposite to the angle: "))                   
        angle =  opp / adj
        ans = math.tanh(angle)
        print("The answer is",ans)
    if trig_choice == 4:
        option = float(input("Enter the value of the side available: "))
        angle = float(input("Enter the measure of the angle: "))
        opp = math.sin(angle) * option 
        hyp = option / math.sin(angle)
        print("The hypotenuse is",hyp, "\r\nAnd the opposite sideis", opp)
    if trig_choice == 5:
        option = float(input("Enter the length of the side available: ")) 
        angle = float(input("Enter the measure of the angle: "))
        adj = math.cos(angle) * option
        hyp = option / math.cos(angle)
        print("The size of the side adjacent to the angle is" , adj, "\r\nAnd the hypotenuse is",hyp)
    if trig_choice == 6:
        option = float(input("Enter the length of the available side: "))
        angle = float(input("Enter the measure of the angle: "))
        opp = math.tan(angle) * option
        adj = option / math.tan(angle)
        print("The length of the side opposite to the angle is",opp, "\r\nAnd the side adjacent is", adj)
    if tri_choice == 3:
        num1 = float(input("Enter the side that ISN'T  a hypotenuse: "))
        hyp = float(input("ENter the hypotenuse: "))
        step1 = num1 * num1
        step2 = hyp *  hyp
        step3 = step1 - step2
        step4 = math.sqrt(step3)
        print("The Answer is", step4)     
print("Select an operation to perform")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.PERCENTAGE")
print("6.POWER")
print("7.SPHERES")
print("8.POLYGON")
print("9.TRIANGLES")
print("10.QUADRATIC EQUATION")
operation = int(input())
if operation == 1:
#ADDITION
    num1 = float(input("ENTER THE FIRST NUMBER: "))
    num2 = float(input("ENTER THE SECOND NUMBER: "))
    print("THE SUM IS ",(num1 + num2)) 
#SUBTRACTION
elif operation == 2:
    num1 = float(input("ENTER THE FIRST NUMBER: "))
    num2 = float(input("ENTER THE SECOND NUMBER: "))
    print("THE DIFFERENCE IS",(num1 - num2))
   #PRODUCT
elif operation == 3:
    num1 = float(input("ENTER THE FIRST NUMBER: "))
    num2 = float(input("ENTER THE SECOND NUMBER: "))
    print("THE ANSWER IS",(num1 * num2))
    #DIVISION
elif operation == 4:
    num1 = float(input("ENTER THE FIRST NUMBER: "))
    num2 = float(input("ENTER THE SECOND NUMBER: "))
    print("THE ANSWER IS",(num1 / num2))
    #MODULO OPERATION
elif operation == 5:
    num1 = int(input("ENTER THE FIRST NUMBER: "))
    num2 = int(input("ENTER THE SECOND NUMBER: "))
    print("THE ANSWER IS",(num1 % num2))
  #EXPONENTS
elif operation == 6:
    num1 = int(input("ENTER THE FIRST NUMBER: "))
    num2 = int(input("ENTER THE SECOND NUMBER: "))
    print(num1 ** num2)
#QUADRATIC EQUATIONS
if operation == 10:
    print("WELCOME TO THE QUADRATICS DEPARTMENT!")
    print("")
    print("""When using the quadratic formula, there are three values you need to assign. They are 'a', 'b','c'. In the following equation the value of 'a' is 6, value of 'b'is 31 and the value of 'c' is 40   6x^2+31x+40""")
    print("")
    a=float(input("Enter a value for 'a': "))
    b=float(input("Enter a value for 'b': "))
    c=float(input("Enter a value for 'c': "))
    step1 = float(b**2)
    step2 = float(step1 - 4*a*c)
    step3 = math.sqrt(step2)
    step5 = float(2*a)
    pstep4 = float (-b + step3)
    pstep6 = float(pstep4 / step5)
    nstep4 = float(-b - step3)
    nstep6 = float(nstep4 / step5)
    print("The two values of x are :/r/n", pstep6, "And", nstep6)
elif operation == 7:
  spheres()
elif operation == 8:
  poly()
elif operation == 9:
  triangles()
else:
    print("INVALID INPUT")
