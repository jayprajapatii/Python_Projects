import pandas as pd
from fpdf import FPDF

# Function to convert XLSX to PDF
def convert_xlsx_to_pdf(xlsx_file, pdf_file):
    # Read the Excel file
    df = pd.read_excel(xlsx_file)

    # Create a PDF object
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add column headers
    for col in df.columns:
        pdf.cell(40, 10, txt=str(col), border=1)
    pdf.ln(10)

    # Add rows
    for index, row in df.iterrows():
        for item in row:
            pdf.cell(40, 10, txt=str(item), border=1)
        pdf.ln(10)

    # Save the PDF
    pdf.output(pdf_file)

# Usage
xlsx_file = 'input.xlsx'  # Input XLSX file
pdf_file = 'output.pdf'   # Output PDF file

convert_xlsx_to_pdf(xlsx_file, pdf_file)
print("PDF saved successfully!")