import os
import urllib.request
import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, StringVar

# Apply dark mode theme
dark_bg = "#2e2e2e"  # Dark background
dark_fg = "#ffffff"  # Light foreground
button_bg = "#3e3e3e"  # Button background
button_fg = "#ffffff"  # Button foreground

# Function to fetch images
def fetch_images():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    save_folder = folder_path.get()
    if not save_folder:
        messagebox.showerror("Error", "Please select a folder to save images.")
        return

    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        images = soup.find_all('img')
        if not images:
            messagebox.showinfo("Info", "No images found on the page.")
            return

        for img in images:
            img_url = img.get('src') or img.get('data-src') or img.get('srcset')
            if img_url:
                if not img_url.startswith(('http:', 'https:')):
                    img_url = requests.compat.urljoin(url, img_url)

                print(f"Downloading image: {img_url}")  # Debugging
                try:
                    file_name = os.path.basename(img_url)
                    save_path = os.path.join(save_folder, file_name)
                    urllib.request.urlretrieve(img_url, save_path)
                except Exception as e:
                    print(f"Failed to download {img_url}: {e}")

        messagebox.showinfo("Success", "All images have been downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to select folder
def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# Create GUI
app = Tk()
app.title("Image Fetcher")
app.geometry("500x200")
app.configure(bg=dark_bg)  # Set the app's background color

folder_path = StringVar()

Label(app, text="Enter Website URL:", bg=dark_bg, fg=dark_fg).pack(pady=5)
url_entry = Entry(app, width=50, bg=dark_bg, fg=dark_fg, insertbackground=dark_fg)
url_entry.pack(pady=5)

Label(app, text="Select Save Folder:", bg=dark_bg, fg=dark_fg).pack(pady=5)
Button(app, text="Choose Folder", command=select_folder, bg=button_bg, fg=button_fg).pack(pady=5)
Label(app, textvariable=folder_path, bg=dark_bg, fg=dark_fg).pack(pady=5)

Button(app, text="Start Download", command=fetch_images, bg=button_bg, fg=button_fg).pack(pady=10)

app.mainloop()
