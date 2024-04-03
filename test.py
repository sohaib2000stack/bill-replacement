import fitz

def remove_all_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b["type"] == 0:  # Text block
                for l in b["lines"]:
                    for s in l["spans"]:
                        rect = fitz.Rect(s["bbox"])
                        page.add_redact_annot(rect)
        page.apply_redactions()
    pdf_document.save("modified_output.pdf")
    pdf_document.close()



# # # Example usage

pdf_path = "0400005231734_480016102591.pdf"
remove_all_text_from_pdf(pdf_path)
print("All text removed. Modified PDF saved as 'modified_output.pdf'.")

















import re
import PyPDF2

def extract_data_from_pdf(pdf_path):
    extracted_data = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Assume that the relevant information is in the first page
        first_page = reader.pages[0]
        text = first_page.extract_text()
        # Convert the extracted text into a list
        lines = text.split('\n')
        # Display the keys and values
        for i, line in enumerate(lines):
            extracted_data.append({'index': i, 'text': line.strip()})
    
    return extracted_data

# Example usage
# pdf_path = '0400005231734_480016102591.pdf'
# extracted_data = extract_data_from_pdf(pdf_path)
# for data in extracted_data:
#     print(f"Index: {data['index']}, Text: {data['text']}")


































