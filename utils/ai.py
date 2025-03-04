from openai import OpenAI
import base64
from natsort import natsorted
import os
import time
import dotenv
dotenv.load_dotenv()

# API_KEY = os.getenv("OPENAI_API_KEY")

def process_images(API_KEY):
    client = OpenAI(api_key = API_KEY)
    folder_name = "screenshots"
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def get_image_batches(folder_name, batch_size=2):
        image_files = natsorted(
            [os.path.join(folder_name, f) for f in os.listdir(folder_name) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        )
        # print([image_files[i:i+batch_size] for i in range(0, len(image_files), batch_size)])
        return [image_files[i:i+batch_size] for i in range(0, len(image_files), batch_size)]



    os.makedirs("English", exist_ok=True)
    image_batches = get_image_batches(folder_name)

    for i,batch in enumerate(image_batches):

        image_numbers = []
        for image in batch:
            image_numbers.append(image.split(".")[0].split("_")[-1])
        print(i, image_numbers)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that translates German notes "
                    "into clear, structured English explanations. Format your "
                    "answers in Markdown, and present any formulas in LaTeX. "
                    "Provide detailed, step-by-step explanations suitable for a "
                    "student studying Electrodynamics."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Please translate the following German Electrodynamics "
                            "notes into English. Include all relevant formulas and "
                            "explanations in a sequential, easy-to-follow manner. "
                            "Use headings, bullet points, and LaTeX for equations. "
                            "Provide a final summary at the end to highlight key points."
                        )
                    }
                ]
                + [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encode_image(image)}",
                            "detail": "high"
                        }
                    }
                    for image in batch
                ]
            }
        ]

        completion = client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=messages
        )

        text = completion.choices[0].message.content
        markdown_filename = f"markdown_{i}.md"
        with open(os.path.join("English", markdown_filename), "w", encoding="utf-8") as md_file:
            md_file.write(text)
        print(f"Saved {markdown_filename}")
        time.sleep(1)