import re

def extract_edu_qualf(x:str):
    
    """
     function to extract educational qualifications using string/pattern matching
     """
    
    find=['Bachelor of Engineering','Master of Engineering','bachelor of technology','master of technology','BTech','MTech','Bsc','Msc'
          'Bachelor of Business Administration','Master of Business Administration','bba','mba'
         'bachelor of computer applications','master of computer applications','bca','mca','bcom'
          'mcom','phd']
    
    for i in find:
        pattern=i.lower()
        x=x.replace('.','')
        truth=re.findall(pattern,x.lower())
        if truth:
            if pattern=='bachelor of Engineering':
                return 'btech'
            elif pattern=='master of Engineering':
                return 'mtech'
            elif pattern=='bachelor of technology':
                return 'btech'
            elif pattern=='master of technology':
                return 'mtech'
            elif pattern=='Bachelor of Business Administration':
                return 'bba'
            elif pattern=='Master of Business Administration':
                return 'mba'
            elif pattern=='bachelor of computer applications':
                return 'bca'
            elif pattern=='master of computer applications':
                return 'mca'
            else:
                return pattern
            
if '__name__'=='__main__':
    extract_edu_qualf(x='')

