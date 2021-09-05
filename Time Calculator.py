def add_time(start, duration, day = None):
    time,midday=start.split()
    start_hr,start_min = time.split(":")
    duration_hr,duration_min = duration.split(":")
    
    # Total Hour and Minute Calculation
    total_min = (int(start_min) + int(duration_min)) % 60
    add_hr = (int(start_min) + int(duration_min)) // 60
    if len(str(total_min)) == 1:
        total_min = "0"+str(total_min)

    # 24 hour clock Format    
    total_hr =int()
    if midday == "PM":
        start_hr = int(start_hr)+ 12
    total_hr = int(start_hr) + int(duration_hr) + add_hr 
    
    # 12 hour clock Format
    twelve_hr = (total_hr % 24) % 12
    if twelve_hr == 0:
        twelve_hr = 12
    
    # Mid Day Calculation.
    if (total_hr % 24) <= 11:
        midday = "AM"
    else:
        midday = "PM"

    # print(twelve_hr,total_min,midday)
    num_of_days = total_hr // 24
    future_days =""
    if num_of_days == 0:
        future_days =""
    elif num_of_days == 1 :
        future_days = "(next day)"
    else:
        future_days = f"({num_of_days} days later)"
    
    total_days = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
    reverse_total_days = {"SUNDAY":1 ,"MONDAY":2,"TUESDAY":3,"WEDNESDAY":4,"THURSDAY":5,"FRIDAY":6,"SATURDAY":7}
    reverse_total_days 
    new_time =""

    if day != None:
        new_time = (str(twelve_hr) +":"+str(total_min)+" "+ midday +", "+total_days[(num_of_days+reverse_total_days[str(day).upper()])%7]+" "+str(future_days)).strip()
    elif num_of_days == 0:
        new_time = str(twelve_hr) +":"+str(total_min)+" "+midday
    else:
        new_time = str(twelve_hr) +":"+str(total_min)+" "+midday+" "+ str(future_days)
    return new_time


print(
add_time("3:00 PM", "3:10"),
# Returns: 6:10 PM 
add_time("11:30 AM", "2:32", "Monday"),
# Returns: 2:02 PM, Monday
add_time("11:43 AM", "00:20"),
# Returns: 12:03 PM
 add_time("10:10 PM", "3:30"),
# Returns: 1:40 AM (next day)
add_time("11:43 PM", "24:20", "tueSday"),
# Returns: 12:03 AM, Thursday (2 days later)
add_time("2:59 AM", "24:00", "saturDay"))
# Returns: 7:42 AM (9 days later))