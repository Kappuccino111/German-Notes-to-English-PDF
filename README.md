# German Handwritten Lecture Notes to English PDF

## Project Overview
This project is a PDF translation tool specifically designed for converting German Electrodynamics lecture notes into structured English content. The system processes PDF content through a pipeline of image extraction, AI-powered translation, and formatting to produce well-structured Markdown and PDF documents.

## Key Features
- **PDF to Image Conversion**: Converts PDF pages into high-resolution images.
- **AI-Powered Translation**: Translates German content to English using OpenAI's API.
- **LaTeX Formula Preservation**: Maintains mathematical formulas with proper LaTeX notation.
- **Markdown Correction**: Automatically fixes LaTeX notation in Markdown files.
- **File Combination**: Merges individual translated files into a comprehensive document.
- **PDF Generation**: Creates a professional-looking PDF from the combined Markdown.
- **Web Interface**: Provides a user-friendly Streamlit interface for the entire process.

## Project Structure
```
.
├── app.py                         # Main Streamlit application
├── utils/
│   ├── ai.py                     # OpenAI API integration for translation
│   ├── convert.py                 # PDF to image conversion
│   ├── combine.py                 # Markdown file combiner
│   ├── markdown_corrector.py      # LaTeX notation fixer
├── corrected/                      # Storage for corrected Markdown files
├── English/                        # Raw AI-translated Markdown files
├── screenshots/                    # Extracted PDF page images
├── temp/                           # Temporary storage for uploaded PDFs
├── requirements.txt                # Project dependencies
├── combined_Electrodynamics_final.md  # Final combined Markdown output
└── output.pdf                      # Final PDF output
```

## How It Works
1. **Upload PDF**: User uploads a German Electrodynamics PDF through the Streamlit interface.
2. **Image Extraction**: PDF pages are converted to high-resolution images.
3. **AI Translation**: Images are processed in batches by OpenAI's API to translate content.
4. **Markdown Generation**: Translated content is saved as Markdown files with LaTeX formulas.
5. **Notation Correction**: LaTeX notation is standardized (`\[...\]` → `$$...$$`, etc.).
6. **File Combination**: Individual Markdown files are combined into a single document.
7. **PDF Generation**: The combined Markdown is converted to a well-formatted PDF.

## Installation
### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenAI API key

### Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pdf-translator.git
    cd pdf-translator
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a `.env` file with your OpenAI API key:
    ```sh
    OPENAI_API_KEY=your-api-key-here
    ```

## Usage
1. Start the Streamlit application:
    ```sh
    streamlit run app.py
    ```
2. Open the displayed URL in your browser (typically http://localhost:8501).
3. Enter your OpenAI API key in the provided field.
4. Upload a PDF file containing German Electrodynamics notes.
5. Wait for the processing to complete.
6. Download the translated PDF.

## Implementation Details
### PDF to Image Conversion
The `convert.py` script uses the `pdf2image` library to extract high-resolution images from the PDF, with configurable DPI settings for optimal clarity of mathematical formulas.

### AI Translation
The `ai.py` module interfaces with OpenAI's API to process the images in batches. It uses a specialized system prompt that instructs the model to focus on properly translating and formatting physics content.

### Markdown Correction
The `markdown_corrector.py` script standardizes LaTeX notation in Markdown files, replacing patterns like `\(...\)` with `$...$` and `\[...\]` with `$$...$$` using regular expressions.

### File Combination
The `combine.py` module organizes the individual Markdown files into sections and combines them into a single comprehensive document with proper headings and separators.

### PDF Generation
The final PDF is generated using Pandoc with the `xelatex` engine, ensuring high-quality mathematical rendering.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Acknowledgments
- The project was created to assist students in studying Electrodynamics lecture notes originally written in German.
- OpenAI API powers the core translation functionality.
- Streamlit provides the web interface framework.

**Note**: This application is optimized for Electrodynamics content but can be adapted for other technical subjects with appropriate modifications to the prompts and processing pipeline.
