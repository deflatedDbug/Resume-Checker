import re 
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    doc = nlp(text)
    lemmatized = " ".join(token.lemma_ for token in doc if not token.is_stop)
    return lemmatized

resumeText = "Experienced Python developer with Flask and SQL background. 5 years in ML."

res = clean_text(resumeText)
print(res)