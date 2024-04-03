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
                    x0, y0, x1, y1 = text_instance[:4]
                    center_x = (x0 + x1) / 2
                    center_y = (y0 + y1) / 2
                    page.insert_text((center_x, center_y), replacement_text, fontsize=10, align=0)
                    # Get the coordinates as a tuple
                    # coordinates = (text_instance.x0, text_instance,0)

                    # # Insert the replacement text as a text box
                    # page.insert_textbox(coordinates, replacement_text, align=0)

        # Save the modified PDF
        pdf_document.save(pdf_path, incremental=False)

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
