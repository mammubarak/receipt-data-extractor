# Receipt-Data-Extractor

## Description
This CLI application processes receipt images, detects text areas, extracts text (items, prices, and totals), and compares multiple receipts by visualizing the totals in a chart.

## Features
- Image preprocessing (resizing, orientation correction, deskewing)
- Text area detection
- Optical Character Recognition (OCR) using Tesseract
- Summarization of receipt data (item name, quantity, price, subtotal, cash, change)
- Comparison of multiple receipts with a visual bar chart

## Prerequisites

1. **Install Tesseract**
   - **Windows**: Download and install Tesseract [here](https://github.com/UB-Mannheim/tesseract/wiki)
   - Uncomment line 7 in ocr_recognition.py file. (Give the correct installed path of tesseract OCR engine)
   - **Linux**: Install via terminal:
     ```bash
     sudo apt install tesseract-ocr
     ```
   - **macOS**: Install via Homebrew:
     ```bash
     brew install tesseract
     ```

2. **Install Python Dependencies**
   Run the following command to install dependencies:
   ```bash
   pip install -r requirements.txt

## Running the Application

### Process a single receipt
```bash
python main.py path/to/receipt_image.jpg
```
- example:
```bash
python main.py images/input/r1.png
```

### Compare multiple receipts
```bash
python main.py --compare
```