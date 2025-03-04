import os
from pdf2image import convert_from_path, pdfinfo_from_path
from tqdm import tqdm

# Path to your PDF file
pdf_path = '/Users/akarshankapoor/Desktop/converter/Elektrodynamik1314Stoeckinger_update.pdf'

# Output folder to save images

def convert_pdf_to_images(pdf_path):
    output_folder = 'screenshots'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get PDF info to determine total pages
    info = pdfinfo_from_path(pdf_path)
    total_pages = info.get("Pages", 0)
    if total_pages == 0:
        raise Exception("Could not determine the number of pages in the PDF.")

    # Settings
    dpi = 400           # High resolution setting
    batch_size = 10     # Process 10 pages at a time

    print(f"Total pages: {total_pages}. Processing in batches of {batch_size} pages...")

    # Create a tqdm progress bar
    with tqdm(total=total_pages, desc="Converting pages") as pbar:
        # Process in batches
        for start_page in range(1, total_pages + 1, batch_size):
            end_page = min(start_page + batch_size - 1, total_pages)
            print(f"\nProcessing pages {start_page} to {end_page}...")

            # Convert pages in the current batch
            pages = convert_from_path(
                pdf_path,
                dpi=dpi,
                first_page=start_page,
                last_page=end_page
            )

            # Save each page as an image
            for i, page in enumerate(pages, start=start_page):
                image_filename = os.path.join(output_folder, f'image_{i}.png')
                page.save(image_filename, 'PNG')
                pbar.update(1)

            # Free memory for the processed batch
            del pages

    print("\nConversion complete!")
