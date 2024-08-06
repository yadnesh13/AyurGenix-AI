# AyurAI - Ayurvedic Medicine Data Extraction and Analysis

AyurGenix AI: Intelligent Ayurvedic Formulation Advisor

Project Overview

AyurGenix AI is an AI-powered software designed to bridge the gap between traditional Ayurvedic medicine and modern healthcare. By leveraging the vast knowledge contained within classical Ayurvedic texts, the project aims to develop a system that can suggest appropriate Ayurvedic drugs and formulations for various diseases and pharmacological properties.

Problem Statement

Modern healthcare systems often overlook the potential of traditional medicine, particularly Ayurveda. Despite its efficacy and historical significance, Ayurveda's integration into contemporary medicine remains limited due to the vast and complex nature of its texts. This project seeks to address this challenge by creating an AI-based solution.

Project Goals

    Develop a robust AI model capable of understanding and processing Ayurvedic text data.
    Extract relevant information about herbs, diseases, and formulations.
    Create a knowledge base of Ayurvedic concepts and relationships.
    Build a user-friendly interface for interacting with the system.

Expected Outcomes

    A functional AI-powered software capable of suggesting Ayurvedic treatments based on user input.
    A valuable tool for healthcare professionals and individuals interested in Ayurveda.
    Increased accessibility and utilization of Ayurvedic knowledge.

Key Challenges

    Extracting accurate and relevant information from complex Ayurvedic texts.
    Developing an AI model capable of understanding the nuances of Ayurvedic concepts.
    Ensuring the reliability and efficacy of the suggested formulations.

Next Steps

    Data collection and preprocessing.
    Model development and training.
    User interface design and development.
    System testing and evaluation.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Entity Extraction](#entity-extraction)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Structure
```
AyurAI/
│
├── data/
│   ├── ayurveda_books/
│   │   ├── book1.txt
│   │   ├── book2.txt
│   │   └── ...
│   └── combined_preprocessed_text.txt
│
├── preprocessing/
│   ├── extract_text.py
│   ├── preprocessing1_to_csv.py
│   └── combined_preprocessed_text.txt
│
├── environment.yml
├── README.md
└── ayurvedic_medicine_data.csv
```

## Setup and Installation

### Prerequisites
- Anaconda/Miniconda
- Python 3.8 or above

### Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/AyurAI.git
   cd AyurAI
   ```

2. **Create a new conda environment and install dependencies**
   ```sh
   conda env create -f environment.yml
   conda activate ayurai_env
   ```

3. **Install NLTK data**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   ```



## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can copy and paste this content into a `README.md` file in your project directory. Make sure to update the repository URL and any other project-specific details as necessary.
