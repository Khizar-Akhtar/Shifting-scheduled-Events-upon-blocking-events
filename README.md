# Shifting-scheduled-Events-upon-blocking-events

This Project aims to help logistic or Production department in moving planned events forward in available free slots if there
is any clash between planned event and some blocker event.A blocker event can be interruption because of any issues or disturbances.
We can give our planned events in following format at start of code [YYYYMMDD ,start_time, end_time]
''
event = pd.DataFrame([
    [20230403,8 ,9],
    [20230403,9 ,11],
    [20230403,13 ,14],
    [20230403,14 ,19],
    [20230404,7 ,10]
    ],
    columns=['Date',  'start_time',   'end_time'])
''
and after that we can add blocker event in following format

''
blocker=[20230405 ,8,11]
''
If the blocker will collide with planned events then program will shift event forward . The working hours of office are from 7 - 19
if the event effected is going outside that time zone (19:00 ) then it will shift that event to next date 
