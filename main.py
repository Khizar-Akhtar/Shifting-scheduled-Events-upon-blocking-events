import pandas as pd
import numpy as np 
#from shift import *

event = pd.DataFrame([
    [20230403,8 ,9],
    [20230403,9 ,11],
    [20230403,13 ,14],
    [20230403,14 ,19],
    [20230404,7 ,9],
    ],
    columns=['Date',  'start_time',   'end_time'])

blocker=[20230404 ,8,11]
overlap_results = []

for i in range(len(event)):
   #This part is checking overlapping in date and time   
  if blocker[0]== event.iat[i, 0] :
    interval1= pd.Interval(blocker[1], blocker[2]) 
    interval2 = pd.Interval(event.iat[i, 1] , event.iat[i, 2] )                                                    # event interval
    result = interval1.overlaps(interval2)   
    if result:
      shift_amount = interval1.right - interval2.left
      event.at[i, 'start_time'] += shift_amount
      event.at[i, 'end_time'] += shift_amount
      for j in range(i+1,len(event)):
       
       #print(i,j)
       if event.at[j-1, 'end_time'] > event.at[j, 'start_time'] :
         time_shift = event.at[j-1, 'end_time']-event.at[j, 'start_time']
         print(time_shift)
         #event.at[j, 'start_time'] = event.at[j-1, 'end_time']
         event.at[j, 'start_time'] +=time_shift
         event.at[j, 'end_time'] +=time_shift
         if event.at[j, 'end_time']>19:
           duration=event.at[j, 'end_time']-event.at[j, 'start_time']
           event.at[j ,'Date'] +=1
           event.at[j, 'start_time'] =7
           event.at[j, 'end_time'] =duration+7

         #event.at[j, 'start_time'] = event.at[j-1, 'end_time']
         print("hi")
      else :
          print("na du") 
         
    else: 
      print("do nothing")
  else:
      print("collision date do not match")

print(event)



#for j in range(i+1,len(event)):
# if event.at[j-1, 'end_time'] > event.at[j, 'start_time'] :
#    print("hi")
# else :
#    print("na du")   
#print(event)     
    