import gradio as gr
from diffusers import StableDiffusionPipeline, StableDiffusionInpaintPipeline
import torch
from PIL import Image

# Load both pipelines
txt2img_pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to("cpu")
inpaint_pipe = StableDiffusionInpaintPipeline.from_pretrained("stabilityai/stable-diffusion-2-inpainting").to("cpu")

# Function for text-to-image generation
def generate_image(prompt):
    image = txt2img_pipe(prompt).images[0]
    return image

# Function for inpainting
def inpaint_image(prompt, image, mask):
    if image is None or mask is None:
        return None
    return inpaint_pipe(prompt=prompt, image=image, mask_image=mask).images[0]

# Tabs UI
with gr.Blocks() as demo:
    gr.Markdown("## 🏠 Interior Design Generator & Editor")

    with gr.Tab("🖼️ Generate from Prompt"):
        prompt_input = gr.Textbox(label="Describe the Room (Prompt)", placeholder="e.g., Cozy Scandinavian living room")
        generate_button = gr.Button("Generate")
        gen_output = gr.Image(label="Generated Image")

        generate_button.click(fn=generate_image, inputs=prompt_input, outputs=gen_output)

    with gr.Tab("🎨 Edit Existing Image"):
        inpaint_prompt = gr.Textbox(label="Describe what to change (Prompt)")
        original_image = gr.Image(label="Original Image", tool="editor", type="pil")
        mask_image = gr.Image(label="Mask Image (white = change)", type="pil")
        inpaint_button = gr.Button("Apply Changes")
        inpaint_output = gr.Image(label="Edited Image")

        inpaint_button.click(fn=inpaint_image, inputs=[inpaint_prompt, original_image, mask_image], outputs=inpaint_output)

demo.launch()
