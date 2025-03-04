import os
import re
from natsort import natsorted

def final_corrector():
    # Directory containing Markdown files
    input_directory = "English"
    output_directory = "corrected"

    # Create 'corrected' directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    # Get all markdown files that match the pattern
    markdown_files = [f for f in os.listdir(input_directory)
                    if f.startswith("markdown_") and f.endswith(".md")]
    markdown_files = natsorted(markdown_files)  # Sort files naturally

    def correct_markdown(content: str) -> str:
        # Replace \( ... \) with $...$ (no extra space between $ and content)
        corrected = re.sub(
            r'\\\(\s*(.*?)\s*\\\)',
            r'$\1$',
            content,
            flags=re.DOTALL
        )

        # Replace \[ ... \] with $$...$$ (no extra space between $$ and content)
        corrected = re.sub(
            r'\\\[\s*(.*?)\s*\\\]',
            r'$$\1$$',
            corrected,
            flags=re.DOTALL
        )

        return corrected

    # Process each Markdown file

    for markdown_file in markdown_files:
        input_path = os.path.join(input_directory, markdown_file)
        output_path = os.path.join(output_directory, markdown_file)

        # Read Markdown content
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Correct the markdown content
        final_corrected_text = correct_markdown(content)

        # Write the corrected Markdown into the "corrected" directory
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_corrected_text)

        print(f"Processed: {markdown_file} → saved in 'corrected/'")

    print("All Markdown files have been corrected and saved in the 'corrected/' folder.")
