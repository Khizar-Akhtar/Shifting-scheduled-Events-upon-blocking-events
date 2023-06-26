
import pandas as pd
import numpy as np

event = pd.DataFrame([
   [20230403,8 ,9],
   [20230403,10 ,18],
   [20230403,18,19],
   ],
columns=['Date',  'start_time',   'end_time'])

#print(event)
blocker=[20230403 ,10 ,12]
deltaB=blocker[2]-blocker[1]

for i in range(3):
      
 if blocker[0]== event.iat[i, 0] :
    
    
    interval1= pd.Interval(blocker[1], blocker[2])
    interval2 = pd.Interval(event.iat[i, 1] , event.iat[i, 2] )
    result = interval1.overlaps(interval2)
    if result:
     x=blocker[2]-event.iat[i, 1]
     new_event=event.add([0,x,x],axis= 'index')
     if new_event.iat[i,2]>19:
       print("yes")
       
     else:
       print("no")
       
       


      
       
       
     
      
     #new_event=event.iat[i, 2]+x
     #new_event=event([])+x

     #y=event.loc[i ,'end_time']+x

    # print(new_event)


     print(new_event)
     #shifting event downwards by deltaB duration
     #new_event=event [['Date','start_time' +str(deltaB), 'end_time'+str(deltaB)]]
     #new_event=event.iat[[i ,]]
     
    #  newest_event=new_event(
     #print(new_event)
    else:
      print("false")     
 i=i+1



