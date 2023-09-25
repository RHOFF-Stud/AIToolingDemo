import gradio as gr
print("Test")

def example_method():
    pass

my_interface = gr.Interface(fn=example_method, inputs="", outputs="")
#my_interface.launch()