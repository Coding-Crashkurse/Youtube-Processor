import tkinter as tk

class AppGUI:

    def __init__(self, processor):
        self.processor = processor
        self.app = tk.Tk()
        self.app.title("YouTube Processor")
        self.build_gui()

    def build_gui(self):
        label = tk.Label(self.app, text="Enter YouTube URL:")
        label.pack(padx=20, pady=5)
        self.url_entry = tk.Entry(self.app, width=50)
        self.url_entry.pack(padx=20, pady=5)
        chunk_size_label = tk.Label(self.app, text="Chunk Size:")
        chunk_size_label.pack(padx=20, pady=5, side=tk.LEFT)
        self.chunk_size_spinbox = tk.Spinbox(self.app, from_=100, to=1000, increment=50, width=5)
        self.chunk_size_spinbox.pack(padx=10, pady=5, side=tk.LEFT)
        process_btn = tk.Button(self.app, text="Process", command=self.process_youtube_url)
        process_btn.pack(padx=20, pady=20)
        self.loading_label = tk.Label(self.app, text="")
        self.loading_label.pack(padx=20, pady=5)
        self.result_text = tk.Text(self.app, height=20, width=70)
        self.result_text.pack(padx=20, pady=5)

    def process_youtube_url(self):
        url = self.url_entry.get()
        current_chunk_size = int(self.chunk_size_spinbox.get())
        self.loading_label.config(text="Processing...")
        self.processor.process_youtube_url(url, current_chunk_size, self.finish_processing)

    def finish_processing(self, result):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.loading_label.config(text="")  # Clear loading text

    def run(self):
        self.app.mainloop()
