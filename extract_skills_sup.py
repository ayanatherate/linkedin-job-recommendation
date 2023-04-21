
import pandas as pd
import spacy
import warnings
warnings.filterwarnings('ignore')
#nlp = spacy.load(r"https://github.com/ayanatherate/findmyjobbot/main/files/en_core_web_sm/en_core_web_sm-3.2.0")



def extract_skills(resume_text:str) -> list[str]:
    
    """
    function to extract skills from job descriptions,
    after matching with pre-loaded corpus of all possible
    skills
    """
    nlp = spacy.load(r"C:\Users\Ayan.Sardar\Downloads\findmyjobbot-main\en_core_web_sm-3.2.0") 
    nlp_text = nlp(resume_text)
    tokens = [token.text for token in nlp_text if not token.is_stop]
    data = pd.read_csv(r"https://raw.githubusercontent.com/ayanatherate/findmyjobbot/main/files/skills_corp.csv.csv") 
    skills = list(data.columns.values)
    skillset = []
    # check for one-grams
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
     # check for bi-grams and tri-grams 
    for token in nlp_text.noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)
    
    return [i.capitalize() for i in set([i.lower() for i in skillset])]


if '__name__'=='__main__':
    extract_skills(resume_text='')

