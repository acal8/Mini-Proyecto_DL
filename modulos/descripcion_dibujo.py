from transformers import Qwen3VLForConditionalGeneration, AutoProcessor
from PIL import Image
import torch

model_id = "Qwen/Qwen3-VL-2B-Instruct"
model = Qwen3VLForConditionalGeneration.from_pretrained(
    model_id, torch_dtype="auto", device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id)

imagen = Image.open("tu_garabato.png")

messages = [
    {
       "role": "user",
        "content": [
            {"type": "image", "image": imagen},
            {"type": "text", "text": """Analyze the animal in this image and answer strictly in this exact format:
Animal: [animal's name]
Description: [Describe strictly and briefly the physical appearance, shape, and colors of the animal exactly as it is depicted, without mentioning the background. Do NOT use words like "drawing", "sketch", "image", "picture". Describe its physical traits directly.]
"""}, ],
    }
]

text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=[text], images=[imagen], padding=True, return_tensors="pt")

generated_ids = model.generate(**inputs, max_new_tokens=128)
output_text = processor.batch_decode(generated_ids, skip_special_tokens=True)

print(output_text[0])