# Interior Design Image Generator using Generative AI

This is a beginner-level project that uses a pre-trained generative AI model to generate interior design images from text prompts.

## 💡 Project Overview
This tool allows users to enter a room description and generate a realistic interior design image using Stable Diffusion.

## 🛠 Tools Used
- Visual Studio Code
- Python 3.8+
- Hugging Face diffusers
- Gradio (for the web interface)
- IBM Generative AI Concepts (Prompt Engineering, Foundation Models)

## 🚀 How to Run
1. Clone this project or unzip the folder.
2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```
3. Install the required packages:
    ```
    pip install diffusers transformers torch gradio
    ```
4. Run the app:
    ```
    python app.py
    ```

## 🧠 IBM Concepts Applied
- Prompt engineering for precise image control
- Use of a foundation model (Stable Diffusion)
- Simple real-world generative AI application

## 📌 Notes
- The image file input is currently optional and not used by the model.
- Prompt specificity improves output quality.

## 🖼 Sample Prompts
- "A modern living room with wooden flooring and a grey couch"
- "Scandinavian-style kitchen with natural light and plants"
