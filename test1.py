import fitz

def replace_text_in_pdf(pdf_path, replacements):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        # Check if the PDF is encrypted
        if pdf_document.is_encrypted:
            # Decrypt the PDF using an empty password
            pdf_document.authenticate("")

        for page_num in range(len(pdf_document)):
            # Get the page
            page = pdf_document[page_num]

            for text_to_replace, replacement_text in replacements.items():
                # Search for text to replace
                text_instances = page.search_for(text_to_replace)

                # Replace the text
                for text_instance in text_instances:
                    # Get the coordinates of the text
                    x0, y0, x1, y1 = text_instance[:4]

                    # Insert the replacement text at the same position as the original text
                    page.insert_text((x0, y0), replacement_text, fontsize=10)

        # Save the modified PDF to a new file
        new_pdf_path = "modified_" + pdf_path
        pdf_document.save(new_pdf_path)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the PDF document
        if pdf_document:
            pdf_document.close()

# Specify the path to your PDF file
pdf_file_path = "0400005231734_480016102591.pdf"

# Specify the text replacements
replacements = {
    "SARDAR BIB": "sohaib",  # Name replacement
    "8thMarch2024": "9thMarch2025",  # Due date replacement
    "2,013": "2,130"  # Amount replacement
}

# Replace the text in the PDF file
replace_text_in_pdf(pdf_file_path, replacements)
