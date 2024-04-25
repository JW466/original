import Power as p

def directionAndSpeedTest():
    print("=========================================================")
    print("Testing forward direction at 25, 50, 75, and 100% speed")
    print("=========================================================")
    p.forward(25, 1)
    p.forward(50, 1)
    p.forward(75, 1)
    p.forward(100, 1)
    
    print("=========================================================")
    print("Testing reverse direction at 25, 50, 75, and 100% speed")
    print("=========================================================")
    p.reverse(25, 1)
    p.reverse(50, 1)
    p.reverse(75, 1)
    p.reverse(100, 1)
    
    print("=========================================================")
    print("Testing stop")
    print("=========================================================")