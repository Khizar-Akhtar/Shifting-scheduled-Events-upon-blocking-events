
import pandas as pd
class Event:
    def __init__(self ,date ,starttime ,endtime):
        self.date=date
        self.starttime=starttime
        self.endtime=endtime
        

class blocker:
    def __init__(self ,date ,starttime ,endtime):
        self.date=date
        self.starttime=starttime
        self.endtime=endtime

#enter blocker and event details
blocker_1=blocker(13042023 ,8 ,12)

#enter event details
event_0=Event(13042023,7,9)
event_1=Event(13042023,10,12)
event_2=Event(13042023,15,17)


# events=3
# for i in range(events):

#     print(i)
#     if blocker_1.date==event_i.date: 
#          interval1= pd.Interval(blocker_1.starttime, blocker_1.endtime)
#          interval2 = pd.Interval(event_i.starttime, event_i.endtime)
#          result = interval1.overlaps(interval2)
#          str = 'yes' if result else 'no'  
#          if str=='yes': 
#                 print("yes it overlaps")
#          else:
#                  print("no it doesnot overlap")       
# i=i+1





     
