import tkinter as tk
from tkinter import ttk
from spellchecker import SpellChecker

# ==================================
# APP CONFIGURATION
# ==================================

APP_TITLE = "Smart Technical Writing Assistant"

spell = SpellChecker()

# ==================================
# TECHNICAL DICTIONARIES
# ==================================

TECHNICAL_WORDS = {

    "Programming": {
        "python", "java", "javascript", "react",
        "nodejs", "github", "vscode",
        "numpy", "pandas", "opencv",
        "mongodb", "mysql"
    },

    "AI / ML": {
        "tensorflow", "pytorch", "scikit",
        "transformer", "llm", "cnn",
        "rnn", "gan", "openai"
    },

    "Business": {
        "startup", "entrepreneurship",
        "marketing", "revenue",
        "fintech", "b2b", "b2c"
    },

    "Academic": {
        "research", "methodology",
        "hypothesis", "bibliography",
        "ieee", "citation"
    }
}

# ==================================
# MAIN WINDOW
# ==================================

root = tk.Tk()

root.title(APP_TITLE)

root.geometry("1300x850")

root.configure(bg="#edf4ff")

# ==================================
# HEADER
# ==================================

header_frame = tk.Frame(
    root,
    bg="#2563eb",
    height=90
)

header_frame.pack(
    fill="x"
)

title_label = tk.Label(
    header_frame,
    text="Smart Technical Writing Assistant",
    font=("Helvetica", 26, "bold"),
    fg="white",
    bg="#2563eb"
)

title_label.pack(
    pady=20
)

# ==================================
# TOP CONTROLS
# ==================================

control_frame = tk.Frame(
    root,
    bg="#edf4ff"
)

control_frame.pack(
    fill="x",
    pady=15
)

tk.Label(
    control_frame,
    text="Mode:",
    font=("Arial", 13, "bold"),
    bg="#edf4ff"
).pack(
    side="left",
    padx=10
)

mode_var = tk.StringVar()

mode_dropdown = ttk.Combobox(
    control_frame,
    textvariable=mode_var,
    state="readonly",
    width=20
)

mode_dropdown["values"] = (
    "General",
    "Programming",
    "AI / ML",
    "Business",
    "Academic"
)

mode_dropdown.current(0)

mode_dropdown.pack(
    side="left"
)

# ==================================
# MAIN DASHBOARD
# ==================================

dashboard = tk.Frame(
    root,
    bg="#edf4ff"
)

dashboard.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

# ==================================
# LEFT PANEL
# ==================================

left_panel = tk.Frame(
    dashboard,
    bg="white",
    width=800
)

left_panel.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0,10)
)

input_title = tk.Label(
    left_panel,
    text="📝 Writing Workspace",
    font=("Helvetica",18,"bold"),
    bg="white"
)

input_title.pack(
    anchor="w",
    padx=15,
    pady=10
)

input_text = tk.Text(
    left_panel,
    wrap="word",
    font=("Arial",14),
    height=20
)

input_text.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

# ==================================
# RIGHT PANEL
# ==================================

right_panel = tk.Frame(
    dashboard,
    bg="white",
    width=320
)

right_panel.pack(
    side="right",
    fill="y"
)

analytics_title = tk.Label(
    right_panel,
    text="📊 Writing Analytics",
    font=("Helvetica",18,"bold"),
    bg="white"
)

analytics_title.pack(
    pady=15
)

word_label = tk.Label(
    right_panel,
    text="Words: 0",
    font=("Arial",13),
    bg="white"
)

word_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

character_label = tk.Label(
    right_panel,
    text="Characters: 0",
    font=("Arial",13),
    bg="white"
)

character_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

sentence_label = tk.Label(
    right_panel,
    text="Sentences: 0",
    font=("Arial",13),
    bg="white"
)

sentence_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

reading_label = tk.Label(
    right_panel,
    text="Reading Time: 0 min",
    font=("Arial",13),
    bg="white"
)

reading_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

misspelled_label = tk.Label(
    right_panel,
    text="Misspelled Words: 0",
    font=("Arial",13),
    bg="white"
)

misspelled_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

vocabulary_label = tk.Label(
    right_panel,
    text="Vocabulary: Beginner",
    font=("Arial",13),
    bg="white"
)

vocabulary_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

score_label = tk.Label(
    right_panel,
    text="Writing Score: 100",
    font=("Arial",13,"bold"),
    fg="green",
    bg="white"
)

score_label.pack(
    anchor="w",
    padx=20,
    pady=10
)

# ==================================
# OUTPUT SECTION
# ==================================

output_frame = tk.Frame(
    root,
    bg="white"
)

output_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

output_title = tk.Label(
    output_frame,
    text="✅ Corrected Output",
    font=("Helvetica",18,"bold"),
    bg="white"
)

output_title.pack(
    anchor="w",
    padx=15,
    pady=10
)

output_text = tk.Text(
    output_frame,
    height=8,
    font=("Arial",14)
)

output_text.pack(
    fill="x",
    padx=15,
    pady=10
)

# ==================================
# START APP
# ==================================

root.mainloop()