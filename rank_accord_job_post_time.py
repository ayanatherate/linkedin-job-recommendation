
def matchtime(x):
    
    """
    ranks (assigns a number) to jobs
    according to time (of job posting) for final sorting

    """
    x=x.split(' ')
    
    rank=0
    if 'hour'in x:
        rank+=int(x[0])+100
    elif 'hours' in x:
        rank+=int(x[0])+100
        
    elif 'week' in x:
        rank+=int(x[0])+1000
    elif 'weeks' in x:
        rank+=int(x[0])+1000
        
    elif 'day' in x:
        rank+=int(x[0])+10000
    elif 'days' in x:
        rank+=int(x[0])+10000
        
    elif 'month' in x:
        rank+=int(x[0])+100000
    elif 'months' in x:
        rank+=int(x[0])+100000
        
    elif 'year' in x:
        rank+=int(x[0])+1000000
    elif 'years' in x:
        rank+=int(x[0])+1000000
    else:
        rank+=1000000
    return rank

if '__name__'=='__main__':
    matchtime(x='')