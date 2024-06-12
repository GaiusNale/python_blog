# This is a simple personal blog application using tkinter
# It allows users to create, list and read articles

import os
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext


# Define the directories for articles and drafts
ARTICLES_DIR = "articles"
DRAFTS_DIR = "drafts"

# Create the directories if they don't exist
os.makedirs(ARTICLES_DIR, exist_ok=True)
os.makedirs(DRAFTS_DIR, exist_ok=True)


def list_articles():
    """
    List all the articles in the articles directory
    """
    # Clear the articles list
    articles_list.delete(0, tk.END)

    # Get all the files in the articles directory
    articles = os.listdir(ARTICLES_DIR)

    # Insert each file into the articles list
    for article in articles:
        articles_list.insert(tk.END, article)


def create_article():
    """
    Create a new article
    """
    # Get the title and content from the user
    title = title_entry.get()
    content = content_text.get("1.0", tk.END)

    # Check if the title and content are not empty
    if title and content:
        # Create a file with the title and content
        file_name = os.path.join(ARTICLES_DIR, title + ".txt")
        with open(file_name, "w") as file:
            file.write(content)

        # Clear the title and content entry fields
        title_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)

        # Show a success message
        messagebox.showinfo("Success", "Article created successfully!")
    else:
        # Show an error message if title or content is empty
        messagebox.showerror("Error", "Title and content are required.")


def read_article():
    """
    Read a selected article
    """
    # Get the selected article from the list
    selected_article = articles_list.get(articles_list.curselection())

    # Check if an article is selected
    if selected_article:
        # Read the content of the selected article
        file_name = os.path.join(ARTICLES_DIR, selected_article)
        with open(file_name, "r") as file:
            content = file.read()

            # Display the content of the article
            article_display.delete("1.0", tk.END)
            article_display.insert(tk.END, content)
    else:
        # Show an error message if no article is selected
        messagebox.showerror("Error", "Select an article to read.")


# Create the tkinter window
root = tk.Tk()
root.title("Personal Blog")

# Create the articles list
articles_list = tk.Listbox(root, width=30, height=10)
articles_list.grid(row=0, column=0, padx=10, pady=10)

# Create the article display field
article_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
article_display.grid(row=0, column=1, padx=10, pady=10)

# Create the title label and entry field
title_label = tk.Label(root, text="Title:")
title_label.grid(row=1, column=0, padx=10, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1, padx=10, pady=5)

# Create the content label and text field
content_label = tk.Label(root, text="Content:")
content_label.grid(row=2, column=0, padx=10, pady=5)
content_text = tk.Text(root, wrap=tk.WORD, width=40, height=5)
content_text.grid(row=2, column=1, padx=10, pady=5)

# Create the buttons
list_button = tk.Button(root, text="List Articles", command=list_articles)
list_button.grid(row=3, column=0, padx=10, pady=5)
read_button = tk.Button(root, text="Read Article", command=read_article)
read_button.grid(row=3, column=1, padx=10, pady=5)
create_button = tk.Button(root, text="Create Article", command=create_article)
create_button.grid(row=4, column=1, padx=10, pady=5)

# Start the tkinter event loop
root.mainloop()

