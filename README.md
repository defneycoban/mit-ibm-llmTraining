# Falcon40B Teaching Assistant

## Overview

The Falcon40B Teaching Assistant is a powerful tool designed to assist students in AP History Subjects (AP Euro, AP World, AP US History) and AP Biology by providing helpful hints and guidance for their questions. Leveraging the IBM Falcon 40B model, this application employs a Gradio interface for easy interaction.

## Features

- **Subject Detection:** The model can accurately detect whether a given question belongs to AP History or AP Biology.

- **Guided Answers:** Once the subject is identified, the system utilizes a set of developed principles to generate insightful hints that act as a teacher assistant, aiding students in understanding and solving problems.

- **User-Friendly Interface:** Gradio provides an intuitive interface for users to input questions and receive helpful hints in a straightforward manner.

## Supported Subjects

- **AP History:** The model supports a wide range of questions related to AP History, providing targeted hints based on historical context and principles.

- **AP Biology:** For questions in AP Biology, the model offers guidance by analyzing biological concepts and principles.

## Getting Started

### Prerequisites

- Python 3.x
- Gradio
- IBM Falcon 40B Model

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/falcon40b-teaching-assistant.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download and set up the IBM Falcon 40B model. Refer to the [IBM Model Documentation](https://ibm.com/docs/falcon40b) for instructions.

4. Run the application:

   ```bash
   python app.py
   ```

   Access the Gradio interface by navigating to `http://localhost:7860` in your web browser.

## Usage

1. Open the Gradio interface in your web browser.

2. Enter your AP History or AP Biology question in the provided input field.

3. Click the "Submit" button to receive hints and guidance related to your question.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize the README based on your specific project structure and additional details. This template provides a starting point that you can build upon.
