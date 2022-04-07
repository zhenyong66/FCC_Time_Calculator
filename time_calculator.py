def add_time(start, duration, start_day = None):
    
# start = "9:15 AM"
# duration = "24:46"
# start_day = "Monday"
    
    days = {"monday" : 1,
            "tuesday" : 2,
            "wednesday" : 3,
            "thursday" : 4,
            "friday" : 5,
            "saturday" : 6,
            "sunday" : 0}
    
    new_days = {1 : "Monday",
                2 : "Tuesday",
                3 : "Wednesday",
                4 : "Thursday",
                5 : "Friday",
                6 : "Saturday",
                0 : "Sunday"}
    
    start = start.split()
    start_time = start[0].split(":")
    start_hr = int(start_time[0])
    start_min = int(start_time[1])
    am_pm = start[1]
    
    duration = duration.split(":")
    duration_hr = int(duration[0])
    duration_min = int(duration[1])
    
    new_hr = 0
    new_min = 0
    nday = 0
    nhour = 0
    
    # count minutes
    tol_min = start_min + duration_min
    if tol_min >= 60:
        nhour = int(tol_min / 60)
        new_min = tol_min % 60
    else:
        new_min = tol_min
        
    if new_min < 10:
        temp = ""
        temp = temp + str(0) + str(new_min)
        new_min = temp
    
    if am_pm == "AM":
        # count hours
        tol_hr = (start_hr % 12) + duration_hr + nhour
        new_hr = tol_hr % 12
        if new_hr == 0:
            new_hr = 12
        
        # find am/pm
        if int(tol_hr / 12) % 2 != 0:
            am_pm = "PM"
            
        # count number of days
        if tol_hr >= 24 and tol_hr < 48:
            nday += 1
            day_passed = "next day"
        elif tol_hr >= 48:
            nday = int(tol_hr / 24)
            day_passed = str(int(nday)) + " days later"
            
        # find new day (optional)
        if start_day != None:
            start_day = start_day.lower()
            if nday < 1:
                new_day = new_days[(days[start_day])]
            elif nday >= 1:
                new_day = new_days[(days[start_day] + nday) % 7]
    
    elif am_pm == "PM":
        tol_hr = (start_hr + 12) + duration_hr + nhour
        new_hr = tol_hr % 12
        if new_hr == 0:
            new_hr = 12
            
        # find am/pm
        if int(tol_hr / 12) % 2 == 0:
            am_pm = "AM"
            
        # count number of days
        if tol_hr >= 24 and tol_hr < 48:
            nday += 1
            day_passed = "next day"
        elif tol_hr >= 48:
            nday = int(tol_hr / 24)
            day_passed = str(int(nday)) + " days later"
            
        # find new day (optional)
        if start_day != None:
            start_day = start_day.lower()
            if nday < 1:
                new_day = new_days[(days[start_day])]
            elif nday >= 1:
                new_day = new_days[(days[start_day] + nday) % 7]
    
    # results
    new_time = ""
    new_time += str(new_hr) + ":" + str(new_min) + " " + str(am_pm)
    if start_day != None:
        new_time += ", " + str(new_day)    
    if tol_hr >= 24:
        new_time += " (" + str(day_passed) + ")"

# print(new_time)

    return new_time 