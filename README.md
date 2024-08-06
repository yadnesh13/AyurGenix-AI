# AyurAI - Ayurvedic Medicine Data Extraction and Analysis

AyurAI is a project designed to extract and analyze relevant information from Ayurvedic text data. The primary goal is to identify diseases, their Ayurvedic treatments, cures, and side effects from a collection of Ayurvedic texts, and store this information in a structured format such as a CSV file.

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

## Usage

### Step 1: Preprocess Text Data
Run the `extract_text.py` script to read and preprocess the Ayurvedic text files.

```sh
python preprocessing/extract_text.py
```

### Step 2: Extract and Analyze Data
Run the `preprocessing1_to_csv.py` script to extract relevant entities and store them in a CSV file.

```sh
python preprocessing/preprocessing1_to_csv.py
```

### Data Preprocessing
The `extract_text.py` script reads all `.txt` files from the specified directory, removes unnecessary whitespace, and combines the texts into a single file (`combined_preprocessed_text.txt`).

### Entity Extraction
The `preprocessing1_to_csv.py` script uses a pre-trained NLP model to identify and extract diseases, treatments, and side effects from the preprocessed text. This data is then stored in `ayurvedic_medicine_data.csv`.

## Results
The final output is a CSV file (`ayurvedic_medicine_data.csv`) containing structured data extracted from the Ayurvedic texts.

### CSV File Columns
- `Disease`
- `Treatments`
- `Side Effects`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can copy and paste this content into a `README.md` file in your project directory. Make sure to update the repository URL and any other project-specific details as necessary.
