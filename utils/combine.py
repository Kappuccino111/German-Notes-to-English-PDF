import os
from natsort import natsorted

def combine_md_files():
    folder_path = "corrected"
    output_file = "combined_Electrodynamics_final.md"

    # Get all markdown files in the folder
    markdown_files = natsorted([f for f in os.listdir(folder_path) if f.startswith("markdown_") and f.endswith(".md")])

    # Open the output file for writing
    with open(output_file, "w", encoding="utf-8") as outfile:
        for file in markdown_files:
            part_number = file.split("_")[1].split(".")[0]  # Extract part number from filename
            outfile.write(f"# Part {part_number}\n\n")  # Write part heading

            # Read the content of the markdown file
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as infile:
                outfile.write(infile.read().strip() + "\n\n")  # Append content with a newline

            # Add an extra line break after each part
            outfile.write("\n---\n\n")


    output_file = output_file
    # Read the existing content
    with open(output_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace all occurrences of '---' with '***'
    updated_content = content.replace("---", "***")

    # Write the updated content back to the file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Updated horizontal rules in {output_file} from '---' to '***'")
