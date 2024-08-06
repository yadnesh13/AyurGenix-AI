import re
import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Load a pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForTokenClassification.from_pretrained("deepset/roberta-base-squad2")
ner_pipeline = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

def extract_entities(text):
    ner_results = ner_pipeline(text)
    diseases = []
    treatments = []
    side_effects = []
    symptoms = []
    research_findings = []

    # Define additional patterns for post-processing
    symptoms_pattern = re.compile(r'symptom|sign', re.IGNORECASE)
    research_pattern = re.compile(r'research|study|findings', re.IGNORECASE)
    
    for entity in ner_results:
        if entity['entity_group'] == 'DISEASE':
            diseases.append(entity['word'])
        elif entity['entity_group'] == 'TREATMENT':
            treatments.append(entity['word'])
        elif entity['entity_group'] == 'SIDE_EFFECT':
            side_effects.append(entity['word'])
        elif symptoms_pattern.search(entity['word']):
            symptoms.append(entity['word'])
        elif research_pattern.search(entity['word']):
            research_findings.append(entity['word'])

    return diseases, treatments, side_effects, symptoms, research_findings

def process_text(text):
    # Split text into sentences or smaller chunks
    sentences = re.split(r'\.\s+', text)
    all_diseases = []
    all_treatments = []
    all_side_effects = []
    all_symptoms = []
    all_research_findings = []

    for sentence in sentences:
        diseases, treatments, side_effects, symptoms, research_findings = extract_entities(sentence)
        all_diseases.extend(diseases)
        all_treatments.extend(treatments)
        all_side_effects.extend(side_effects)
        all_symptoms.extend(symptoms)
        all_research_findings.extend(research_findings)

    return all_diseases, all_treatments, all_side_effects, all_symptoms, all_research_findings

# Read the combined preprocessed text
with open('combined_preprocessed_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Process the text
diseases, treatments, side_effects, symptoms, research_findings = process_text(text)

# Check if any entities were found
if not (diseases or treatments or side_effects or symptoms or research_findings):
    print("No relevant entities were found in the text.")
else:
    # Create a structured data dictionary
    structured_data = {
        "disease": ' '.join(diseases),
        "treatments": ' '.join(treatments),
        "side_effects": ' '.join(side_effects),
        "symptoms": ' '.join(symptoms),
        "research_findings": ' '.join(research_findings)
    }

    # Convert the structured data into a DataFrame and save it as a CSV file
    df = pd.DataFrame([structured_data])
    df.to_csv('ayurvedic_medicine_data.csv', index=False)

# Optional: Print the data to verify
try:
    print(df)
except NameError:
    print("DataFrame not created due to no relevant entities found.")
