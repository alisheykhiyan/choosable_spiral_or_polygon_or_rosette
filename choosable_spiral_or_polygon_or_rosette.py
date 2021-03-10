# ChoosableSpiralOrPolygonOrRosette.py

answer = input("DO you want to see a shape?(yes/no)")
if answer == 'yes':
    being_colorful = input("DO you want your shape to be colorful or not?(y/n)")
    if being_colorful == 'y':
       
        
        colors =["red","orange","yellow","green","blue","purple","pink","gray","white"]
        shape = input("Which shape do you want:(Enter'p'for polygon ,'r'for rosette and's'forspiral)") 
        sides = eval(input("How many side do you want your shape to be?")) 
        if shape == 'p':
            import turtle
            t=turtle.Pen ()
            t.speed(0)
            for x in range (sides):
                t.forward (50)
                t.left (360/sides)
                t.pencolor (colors[x % 9])
        if shape == 's':
            import turtle
            t=turtle.Pen ()
            t.speed(0)
            for x in range (100):
                t.forward (x)
                t.left ((360/sides)+1)  
                t.pencolor (colors[x % 9])
            
        if shape =='r':
            import turtle
            t=turtle.Pen ()
            t.speed(0)
            for x in range (sides):
                t.circle (100)
                t.left ((360/sides))  
                t.pencolor (colors[x % 9])
    print ("thank you for running this programm ;)")
    if being_colorful == 'n':
        shape = input("Which shape do you want:(Enter'p'for polygon ,'r'for rosette and's'forspiral)")
        sides = eval(input("How many side do you want your shape to be?")) 
        if shape == 'p':
            import turtle
            t=turtle.Pen ()
            t.speed(0)
            for x in range (sides):
                t.forward (50)
                t.left (360/sides)
        if shape == 's':
            import turtle
            t=turtle.Pen ()
            t.speed(0)
            for x in range (100):
                t.forward (x)
                t.left ((360/sides)+1)  
            
        if shape =='r':
            import turtle
            t=turtle.Pen ()
            t.speed(0)
            for x in range (sides):
                t.circle (100)
                t.left ((360/sides))  
    print ("thank you for running this programm ;)")
if answer != 'yes':
    print ("Ok,see you soon!;)")
