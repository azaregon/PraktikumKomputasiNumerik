import math
import matplotlib.pyplot as plt
import numpy as np
import time

def f(x):
    # return x**3 +2*x**2 + 10*x -20
    # return x**2 + 5*x + 6
    return 0.5*x**5 +x**4 + x**3 + x**2 +x+1
    # return x**3 + 2*x**2 + 10*x -20


# def falsePos(a,b,max_iter,ketelitian):
#     iter_now = 0
#     is_iter = True


#     new_x = -1029313091329312
#     while is_iter:
#         fa = f(a)
#         fb = f(b)


        
        
#         if fa*fb < 0 :
#             new_x = (a*fb + b*fa) / (fa+fb)
              
#             if fa*f(new_x) < 0:
#                 b = new_x
#             else:
#                a = new_x

#             iter+=1

#             if iter_now > max_iter or math.abs(new_x) < ketelitian:
#                 break 

#         else:
#             is_iter = False

#             break

#         time.sleep(2)
#     return new_x
    
                



def falsePos2(aa,bb,max_iter,ketelitian):
    iter_now = 0
    is_iter = True
    a = aa
    b = bb
    # new_x = (a*f(b) - b*f(a)) / (f(a)-f(b))

    plt.ion()
    fig,ax = plt.subplots()
    ax.set_xlim(a-4,b+4)
    ax.set_ylim(min(f(a),f(b))-2 , max(f(a),f(b))+2)


    f_plot_x = np.linspace(a-20,b+20,200)
    f_plot_y = f(f_plot_x)

    plt.plot(f_plot_x,f_plot_y)


    ab_line_x = [a,b]
    ab_line_y = [0,0]
    x_zero, = ax.plot([-1000,1000],[0,0],'c-')
    y_zero, = ax.plot([0,0],[-1000,1000],'c-')
    p_a, = ax.plot([a],[0],'bo')
    p_b, = ax.plot([b],[0],'go')
    l_ab, = ax.plot(ab_line_x,ab_line_y,'y-')
    # p_midX, = ax.plot([new_x],[f(new_x)],'ro')
    p_midX, = ax.plot([0],[f(0)],'ro')



    while is_iter:
        fa = f(a)
        fb = f(b)

        if fa*fb > 0:
            print("no root between a and b")
            return 0


        if fa*fb < 0 :
            # new_x = (a * f(b) - b * f(a)) / (f(b) - f(a))
            new_x = (a * fb - b * fa) / (fb - fa)
              
            if fa*f(new_x) < 0:
                b = new_x
            else:
                a = new_x

            iter_now+=1

            print(new_x,"  ",f(new_x))
            if iter_now > max_iter or abs(f(new_x)) < ketelitian :
                is_iter = False
                break 

        else:
            is_iter = False
            break
        
        ax.set_xlim(a-4,b+4)
        p_a.set_data([a],[fa])
        p_b.set_data([b],[fb])
        l_ab.set_data([a,b],[fa,fb])
        p_midX.set_data([new_x],[f(new_x)])

        plt.draw()
        plt.pause(1)

        
    # plt.ioff()

    return new_x
    



if __name__ == '__main__':
    a = falsePos2(-2,2,100,0.001)
    print("===========")
    print(a)