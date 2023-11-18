import gradioInterface as gr

def input_output_interface(input_text):
    return f"{input_text}"

iface = gr.Interface(
    fn=input_output_interface,
    inputs="text",
    outputs="text",
    live=True,
)

iface.launch()