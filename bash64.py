import base64
import tkinter as tk
from tkinter import scrolledtext, messagebox

class HackerBase64:
    def __init__(self, root):
        self.root = root
        self.root.title("CyberBase64")
        self.root.geometry("500x400")
        self.setup_ui()
        
    def setup_ui(self):
        # Hacker theme (dark with green accents)
        self.root.configure(bg='black')
        widget_style = {'bg': 'black', 'fg': '#00ff00', 'font': ('Courier', 10)}
        entry_style = {**widget_style, 'insertbackground': '#00ff00', 'selectbackground': '#003300'}
        
        # Main frame
        self.tab = tk.Frame(self.root, bg='black')
        self.tab.pack(fill=tk.BOTH, expand=True)
        
        # Input
        tk.Label(self.tab, text="Input:", **widget_style).pack(anchor='w')
        self.input_text = scrolledtext.ScrolledText(self.tab, **entry_style, height=8)
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        btn_frame = tk.Frame(self.tab, bg='black')
        btn_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(btn_frame, text="Encode", command=self.encode, 
                bg='black', fg='#00ff00', relief='groove').pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Decode", command=self.decode,
                bg='black', fg='#00ff00', relief='groove').pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Clear", command=self.clear,
                bg='black', fg='#ff0000', relief='groove').pack(side=tk.RIGHT)
        
        # Output
        tk.Label(self.tab, text="Output:", **widget_style).pack(anchor='w')
        self.output_text = scrolledtext.ScrolledText(self.tab, **entry_style, height=8)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
    def encode(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Alert", "Input required!")
            return
        
        try:
            encoded = base64.b64encode(text.encode()).decode()
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, encoded)
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed: {str(e)}")
    
    def decode(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Alert", "Input required!")
            return
        
        try:
            decoded = base64.b64decode(text.encode()).decode()
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, decoded)
        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed: {str(e)}")
    
    def clear(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = HackerBase64(root)
    root.mainloop()
