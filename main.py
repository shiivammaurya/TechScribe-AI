import customtkinter as ctk

from analytics import calculate_analytics
from spell_engine import correct_text

from technical_dictionary import (
    PROGRAMMING_WORDS,
    AI_WORDS,
    BUSINESS_WORDS,
    ACADEMIC_WORDS
)

# ==========================================
# APP SETTINGS
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_TITLE = "Smart Technical Writing Assistant"

# ==========================================
# MAIN WINDOW
# ==========================================

root = ctk.CTk()

root.title(APP_TITLE)

root.geometry("1400x850")

# ==========================================
# TECHNICAL DICTIONARY HELPER
# ==========================================

def get_dictionary():

    mode = mode_var.get()

    if mode == "Programming":
        return PROGRAMMING_WORDS

    elif mode == "AI / ML":
        return AI_WORDS

    elif mode == "Business":
        return BUSINESS_WORDS

    elif mode == "Academic":
        return ACADEMIC_WORDS

    return set()

# ==========================================
# WRITING SCORE
# ==========================================

def calculate_score(word_count, misspelled):

    score = 100

    score -= misspelled * 5

    if word_count < 10:
        score -= 10

    if score < 0:
        score = 0

    return score

# ==========================================
# ANALYTICS UPDATE
# ==========================================

def update_analytics(event=None):

    text = input_box.get(
        "1.0",
        "end-1c"
    )

    result = calculate_analytics(
        text
    )

    technical_words = get_dictionary()

    corrected_text, misspelled = correct_text(
        text,
        technical_words
    )

    score = calculate_score(
        result["words"],
        misspelled
    )

    word_label.configure(
        text=f"Words: {result['words']}"
    )

    char_label.configure(
        text=f"Characters: {result['characters']}"
    )

    sentence_label.configure(
        text=f"Sentences: {result['sentences']}"
    )

    reading_label.configure(
        text=f"Reading Time: {result['reading_time']} min"
    )

    misspelled_label.configure(
        text=f"Misspelled Words: {misspelled}"
    )

    vocabulary_label.configure(
        text=f"Vocabulary: {result['vocabulary']}"
    )

    score_label.configure(
        text=f"Writing Score: {score}/100"
    )

# ==========================================
# CORRECT BUTTON
# ==========================================

def perform_correction():

    text = input_box.get(
        "1.0",
        "end-1c"
    )

    technical_words = get_dictionary()

    corrected_text, misspelled = correct_text(
        text,
        technical_words
    )

    output_box.delete(
        "1.0",
        "end"
    )

    output_box.insert(
        "1.0",
        corrected_text
    )

    update_analytics()

# ==========================================
# HEADER
# ==========================================

title_label = ctk.CTkLabel(
    root,
    text="🚀 Smart Technical Writing Assistant",
    font=("Helvetica", 32, "bold")
)

title_label.pack(
    pady=20
)

# ==========================================
# TOP BAR
# ==========================================

top_frame = ctk.CTkFrame(
    root
)

top_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

mode_label = ctk.CTkLabel(
    top_frame,
    text="Mode:"
)

mode_label.pack(
    side="left",
    padx=10
)

mode_var = ctk.StringVar(
    value="General"
)

mode_dropdown = ctk.CTkComboBox(
    top_frame,
    values=[
        "General",
        "Programming",
        "AI / ML",
        "Business",
        "Academic"
    ],
    variable=mode_var,
    width=200
)

mode_dropdown.pack(
    side="left",
    padx=10
)

# ==========================================
# MAIN SECTION
# ==========================================

main_frame = ctk.CTkFrame(
    root
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

# ==========================================
# LEFT PANEL
# ==========================================

left_panel = ctk.CTkFrame(
    main_frame
)

left_panel.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

input_title = ctk.CTkLabel(
    left_panel,
    text="📝 Writing Workspace",
    font=("Helvetica", 20, "bold")
)

input_title.pack(
    pady=10
)

input_box = ctk.CTkTextbox(
    left_panel,
    width=800,
    height=350
)

input_box.pack(
    padx=15,
    pady=10,
    fill="both",
    expand=True
)

# ==========================================
# RIGHT PANEL
# ==========================================

right_panel = ctk.CTkFrame(
    main_frame,
    width=300
)

right_panel.pack(
    side="right",
    fill="y",
    padx=10,
    pady=10
)

analytics_title = ctk.CTkLabel(
    right_panel,
    text="📊 Writing Analytics",
    font=("Helvetica", 20, "bold")
)

analytics_title.pack(
    pady=20
)

word_label = ctk.CTkLabel(
    right_panel,
    text="Words: 0"
)

word_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

char_label = ctk.CTkLabel(
    right_panel,
    text="Characters: 0"
)

char_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

sentence_label = ctk.CTkLabel(
    right_panel,
    text="Sentences: 0"
)

sentence_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

reading_label = ctk.CTkLabel(
    right_panel,
    text="Reading Time: 0 min"
)

reading_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

misspelled_label = ctk.CTkLabel(
    right_panel,
    text="Misspelled Words: 0"
)

misspelled_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

vocabulary_label = ctk.CTkLabel(
    right_panel,
    text="Vocabulary: Beginner"
)

vocabulary_label.pack(
    anchor="w",
    padx=20,
    pady=5
)

score_label = ctk.CTkLabel(
    right_panel,
    text="Writing Score: 100/100",
    font=("Helvetica", 16, "bold")
)

score_label.pack(
    anchor="w",
    padx=20,
    pady=15
)

# ==========================================
# CORRECT BUTTON
# ==========================================

correct_button = ctk.CTkButton(
    root,
    text="⚡ Correct Writing",
    height=45,
    command=perform_correction
)

correct_button.pack(
    pady=10
)

# ==========================================
# OUTPUT SECTION
# ==========================================

output_frame = ctk.CTkFrame(
    root
)

output_frame.pack(
    fill="both",
    padx=20,
    pady=10
)

output_title = ctk.CTkLabel(
    output_frame,
    text="✅ Corrected Output",
    font=("Helvetica", 20, "bold")
)

output_title.pack(
    pady=10
)

output_box = ctk.CTkTextbox(
    output_frame,
    height=180
)

output_box.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

# ==========================================
# LIVE ANALYTICS
# ==========================================

input_box.bind(
    "<KeyRelease>",
    update_analytics
)

# ==========================================
# START APP
# ==========================================

root.mainloop()