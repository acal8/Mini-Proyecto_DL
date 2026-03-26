import torch
from diffusers import DiffusionPipeline

model_id = "stabilityai/stable-diffusion-xl-base-1.0"

pipe = DiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    use_safetensors=True, 
    variant="fp16"
)
pipe.to("cuda")

prompt = "Children's book illustration of Berta the giant blue whale in the ocean, watercolor style."

image = pipe(prompt=prompt).images[0]
image.save("berta_sdxl.png")