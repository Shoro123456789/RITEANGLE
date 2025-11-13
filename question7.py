def clock(hour: int, minute: int, second: int) -> float:
    if hour < 12:
        angle_H= (30*hour)+(0.5*minute)+((1/120)*second)
    else:
        angle_H= (30*(hour-12))+(0.5*minute)+((1/120)*second)
    angle_M=(6*minute)+(0.1*second)
    angle_S=6*second
    alpha= abs(angle_H - angle_M)
    if alpha > 180:
        alpha= 360 - alpha
#    print(alpha)
    beta= abs(angle_M - angle_S)
    if beta > 180:
        beta= 360 - beta
#    print(beta)
    gamma= abs(angle_S - angle_H)
    if gamma > 180:
        gamma= 360 - gamma
#    print(gamma)
    return abs(alpha), abs(beta), abs(gamma),[angle_H, angle_M, angle_S], [hour, minute, second]
smallest_angle = 360
for constant in range(0,24):
    for m in range(-12,30):
        if constant+(2*m)>60 or constant+(2*m)<0 or m==0:
            continue
        else:
            a,b,c,d,e=clock(constant,constant+m,constant+(2*m))
            if abs(a+b+c)<smallest_angle:
                smallest_angle=a+b+c
                print(constant,constant+m,constant+(2*m))
                print("m:"+str(m))
                print(a)
                print(b)
                print(c)
                print("Total Angle:"+str(a+b+c))
                total_angles=a+b+c
                print(total_angles)
print(d)
print(e)
print(smallest_angle)