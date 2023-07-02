import datetime
def processView(views):
    if views == None:
        return 0
    if views >= 1000000:
        processed_views = str(views//1000000) + 'M'
    elif views >= 1000:
        processed_views = str(views//1000) + 'K'
    else:
        processed_views = views
    return processed_views

def time_difference(date):
    current_time = datetime.now().replace(microsecond=0)
    try:
        seconds = (current_time-date.replace(microsecond=0)).total_seconds()
    except:
        return 'unreleased'
    minutes = int(seconds / 60)
    hours = int(minutes / 60)
    days = int(hours / 24)
    if seconds < 60 and seconds > 0:
        return str(int(seconds))+' seconds ago'
    elif seconds < 0:
        return 'unreleased'
    elif minutes < 60:
        if minutes == 1:
            return str(minutes)+' minute ago'
        else:
            return str(minutes)+' minutes ago'
    elif hours < 24:
        if hours == 1:
            return str(hours)+' hour ago'
        else:
            return str(hours)+' hours ago'
        
    elif days < 7:
        if days == 1:
            return str(days)+' day ago'
        else:
            return str(days)+' days ago'
    else:
        return date.date().strftime("%d %B, %Y")

