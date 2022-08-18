from time import sleep
from turtle import *
color('yellow')
begin_fill()
while True:
    forward(15)
    left(30)
    forward(15)
    forward(15)
    left(30)
    forward(15)
    forward(15)
    left(30)
    forward(15)
    if abs(pos()) < 1:
            break
    
end_fill()

done()
