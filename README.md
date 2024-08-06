# AyurVeda AI - Intelligent Ayurvedic Formulation Advisor

AyurVeda AI is a project aimed at bridging the gap between traditional Ayurvedic medicine and modern healthcare. The software leverages AI to suggest Ayurvedic drugs and formulations based on classical Ayurvedic texts. The goal is to enhance the integration of Ayurveda into contemporary medicine by providing actionable insights from ancient wisdom.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
```
AyurVeda_AI/
│
├── data/
│   ├── ayurvedic_texts/
│   │   ├── text1.txt
│   │   ├── text2.txt
│   │   └── ...
│   └── ayurvedic_formulations.csv
│
├── preprocessing/
│   ├── text_processing.py
│   ├── nlp_analysis.py
│   └── combined_preprocessed_text.txt
│
├── recommendation/
│   ├── formulation_engine.py
│   └── recommendation_results.csv
│
├── environment.yml
├── README.md
└── ayurvedic_formulations.csv
```

## Setup and Installation

### Prerequisites
- Anaconda/Miniconda
- Python 3.8 or above

### Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/AyurVeda_AI.git
   cd AyurVeda_AI
   ```

2. **Create a new conda environment and install dependencies**
   ```sh
   conda env create -f environment.yml
   conda activate ayurveda_env
   ```

3. **Install NLTK data**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   ```

## Usage

### Step 1: Preprocess Text Data
Run the `text_processing.py` script to preprocess the Ayurvedic text files.

```sh
python preprocessing/text_processing.py
```

### Step 2: Analyze Text Data
Run the `nlp_analysis.py` script to perform NLP analysis and extract relevant information from the preprocessed text.

```sh
python preprocessing/nlp_analysis.py
```

### Step 3: Generate Recommendations
Run the `formulation_engine.py` script to generate Ayurvedic drug and formulation recommendations based on input symptoms or pharmacological properties.

```sh
python recommendation/formulation_engine.py
```

## Features

- **Disease and Symptom Input Interface:** User-friendly input for specifying diseases or symptoms.
- **Pharmacological Property Search:** Search by properties like anti-inflammatory or analgesic.
- **Database of Ayurvedic Texts:** Collection of classical Ayurvedic texts.
- **NLP Module:** Extracts relevant information from text using NLP techniques.
- **Formulation Recommendation Engine:** AI-based suggestions for Ayurvedic treatments.
- **Dosage and Administration Guidelines:** Provides traditional dosage and administration instructions.
- **Cross-Reference with Modern Medicine:** Compares Ayurvedic recommendations with modern treatments.
- **Personalized Recommendations:** Tailors suggestions based on user profiles.
- **Educational Resources:** Provides information about Ayurvedic principles.

## Results
The final output includes:
- **`ayurvedic_formulations.csv`**: Contains suggested Ayurvedic formulations and their details.

### CSV File Columns
- `Disease`
- `Formulation`
- `Pharmacological Property`
- `Dosage`
- `Administration Guidelines`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to adjust the details according to your specific implementation and needs.
