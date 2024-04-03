import fitz

def insert_text_in_blank_spaces(pdf_path, text_to_insert):
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text = page.get_text()
        if not text.strip():  # Check if the page is blank
            page_width = page.rect.width
            page_height = page.rect.height
            # Insert the new text in the center of the page
            insert_x = page_width / 2
            insert_y = page_height / 2
            # Create a new PDF page object
            new_page = pdf_document.new_page(width=page_width, height=page_height)
            # Draw the new text on the new page
            new_page.insert_text((insert_x, insert_y), text_to_insert)
            # Replace the original page with the new page
            pdf_document.replace_page(page_num, new_page)

    # Save the modified PDF
    pdf_document.save("modified_output.pdf")
    pdf_document.close()

# Specify the path to your PDF file
pdf_file_path = "modified_output.pdf"

# Specify the text to insert
text_to_insert = "This"

# Insert the text in the blank spaces of the PDF file
insert_text_in_blank_spaces(pdf_file_path, text_to_insert)
