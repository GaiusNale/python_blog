

# Directory paths for articles and drafts

# Create directories if they don't exist

# Function to list existing articles

# Function to create a new article


# Function to read an existing article


# Create the main window


# Create a listbox to display articles


# Create an article display area


# Create entry and text widgets for creating new articles


# Create buttons for actions

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
ARTICLES_DIR = "articles"
DRAFTS_DIR = "drafts"

os.makedirs(ARTICLES_DIR, exist_ok=True)
os.makedirs(DRAFTS_DIR, exist_ok=True)

def list_articles():
    articles_list.delete(0, tk.END)
    articles = os.listdir(ARTICLES_DIR)
    for article in articles:
        articles_list.insert(tk.END, article)

def create_article():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END)
    if title and content:
        file_name = os.path.join(ARTICLES_DIR, title + ".txt")
        with open(file_name, "w") as file:
            file.write(content)
        title_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Article created successfully!")
    else:
        messagebox.showerror("Error", "Title and content are required.")
def read_article():
    selected_article = articles_list.get(articles_list.curselection())
    if selected_article:
        file_name = os.path.join(ARTICLES_DIR, selected_article)
        with open(file_name, "r") as file:
            content = file.read()
            article_display.delete("1.0", tk.END)
            article_display.insert(tk.END, content)
    else:
        messagebox.showerror("Error", "Select an article to read.")
root = tk.Tk()
root.title("Personal Blog")
articles_list = tk.Listbox(root, width=30, height=10)
articles_list.grid(row=0, column=0, padx=10, pady=10)
article_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
article_display.grid(row=0, column=1, padx=10, pady=10)
title_label = tk.Label(root, text="Title:")
title_label.grid(row=1, column=0, padx=10, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1, padx=10, pady=5)
content_label = tk.Label(root, text="Content:")
content_label.grid(row=2, column=0, padx=10, pady=5)
content_text = tk.Text(root, wrap=tk.WORD, width=40, height=5)
content_text.grid(row=2, column=1, padx=10, pady=5)
list_button = tk.Button(root, text="List Articles", command=list_articles)
list_button.grid(row=3, column=0, padx=10, pady=5)
read_button = tk.Button(root, text="Read Article", command=read_article)
read_button.grid(row=3, column=1, padx=10, pady=5)
create_button = tk.Button(root, text="Create Article", command=create_article)
create_button.grid(row=4, column=1, padx=10, pady=5)

root.mainloop()