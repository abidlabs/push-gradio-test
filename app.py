import gradio as gr

gr.Interface(lambda x:x, "textbox", "textbox", title="test").launch()
