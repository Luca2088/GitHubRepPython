def time_to_minutesAMPM(time):
    divided_time_list = time.split(" ")
    hours = divided_time_list[0].split(":")[0]
    minutes = divided_time_list[0].split(":")[1]
    int_minutes = int(minutes)
    int_hours = int(hours)
    if 'PM' in divided_time_list[1] and int_hours != 12:
        int_hours += 12
    if 'AM' in divided_time_list[1] and int_hours == 12:
        int_hours -= 12

    int_minutes += 60*int_hours
    return int_minutes

def time_to_minutes(time):
    hours = time.split(":")[0]
    minutes = time.split(":")[1]
    int_minutes = int(minutes)
    int_hours = int(hours)
    int_minutes += int_hours*60
    return int_minutes

def minutes_to_days(minutes,day_name):
    day_name_low = str(day_name).lower()
    days_dict = {'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
    new_days_dict = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    if day_name == -1:
        new_day = ''
    else:
        number_of_day = days_dict[day_name_low]
        days = int((minutes/60)//24)
        new_day = ", "+new_days_dict[(number_of_day + days)%7]
    days = int((minutes/60)//24)
    if days ==0:
        return f'{new_day}'
    if days == 1:
        return f'{new_day} (next day)'
    elif days >= 2:
        return f'{new_day} ({days} days later)'
    else:
        return ''
    
def add_time(start, duration,starting_day = -1):
    start_in_minutes = time_to_minutesAMPM(start)
    duration_in_minutes = time_to_minutes(duration)
    new_time_in_minutes = start_in_minutes + duration_in_minutes
    days_message = minutes_to_days(new_time_in_minutes,starting_day)
    if ((new_time_in_minutes//60)//12)%2==0:
        period = 'AM'
    else:
        period = 'PM'
    aux_op1 = "" if new_time_in_minutes%60>=10 else "0"
    hours = (new_time_in_minutes//60)
    if hours == 12:
        new_hours = (hours%24)%13
    elif hours != 12:
        new_hours = (hours%24)%12
    if hours % 24 ==0:
        new_hours = 12
    minutes = new_time_in_minutes%60
    new_time12 = f'{new_hours}:{aux_op1}{minutes} {period}{days_message}'

    return new_time12

print(add_time('9:59 PM', '53:02'))