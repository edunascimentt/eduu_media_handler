import customtkinter
import requests
from pytubefix import YouTube
from PIL import Image, ImageTk
from io import BytesIO

mainwindow = customtkinter.CTk()
mainwindow.geometry("1350x825")
mainwindow.title("Eduu's Media Utility")
mainwindow.resizable(False, False)

label_font = customtkinter.CTkFont(size=50)
description_font = customtkinter.CTkFont(size=25)
url_font = customtkinter.CTkFont(size=20)

# LEFT FRAME
left_frame = customtkinter.CTkFrame(
    mainwindow,
    fg_color="#202325",
    width=675,
    height=825,
    corner_radius=30,
)
left_frame.pack(side="left", fill="both", expand=True)
left_frame.pack_propagate(False)

label_wrapper_left = customtkinter.CTkFrame(
    left_frame,
    fg_color="#f17634",
    corner_radius=15,
)
label_wrapper_left.pack(pady=(20, 0), padx=20, anchor="w")

download_area_label = customtkinter.CTkLabel(
    label_wrapper_left,
    text="Download area",
    text_color="white",
    font=label_font,
    fg_color="transparent",
)
download_area_label.pack(padx=20, pady=1)

download_description_label = customtkinter.CTkLabel(
    left_frame,
    text="Download youtube videos or\nspotify songs & playlists here!",
    text_color="white",
    font=description_font,
    anchor="w",
    justify="left",
)
download_description_label.pack(pady=20, padx=25, anchor="w")

url_wrapper = customtkinter.CTkFrame(
    left_frame,
    fg_color="#f17634",
    corner_radius=15,
)
url_wrapper.pack(pady=0, padx=20, anchor="w")

url_label = customtkinter.CTkLabel(
    url_wrapper,
    text="Enter the url:",
    text_color="white",
    font=url_font,
    fg_color="transparent",
)
url_label.pack(pady=10, padx=10)

url_entry = customtkinter.CTkEntry(
    left_frame,
    placeholder_text="Youtube/Spotify Link Here!",
    font=description_font,
    width=635,  
    height=70,
    corner_radius=15,
)
url_entry.pack(pady=1, padx=20, anchor="w")
url_entry.bind("<FocusOut>", lambda event: fetch_video_info())

video_title_label = customtkinter.CTkLabel(
    left_frame,
    text="",
    text_color="white",
    font=description_font,
    anchor="w",
    justify="left",
)
video_title_label.pack(pady=(10, 10))

thumbnail_label = customtkinter.CTkLabel(
    left_frame,
    text=" ",
    width=500,
    height=281,
    corner_radius=10,
)
thumbnail_label.pack(pady=(0, 10), padx=0)

status_label = customtkinter.CTkLabel(
    left_frame,
    text="",
    text_color="yellow",
    font=description_font,
    anchor="w",
    justify="left",
)
status_label.pack(pady=(10, 0), padx=25, anchor="w")

current_youtube_object = None
download_button = customtkinter.CTkButton(
    left_frame,
    text="Download",
    text_color="white",
    font=label_font,
    corner_radius=15,
    fg_color="#f17634",
    hover_color="#ff8a37",
    command=lambda: download_video(),
    state="disabled",
)
download_button.pack(side="bottom", anchor="w", pady=(10, 20), padx=20)

def download_video():
    global current_youtube_object
    if current_youtube_object:
        try:
            status_label.configure(text="Downloading video...")
            stream = current_youtube_object.streams.get_highest_resolution()
            if stream:
                stream.download()
                status_label.configure(text="Download complete!")
            else:
                status_label.configure(text="No suitable stream found for download.")
        except Exception as e:
            status_label.configure(text=f"Error during download: {e}")
    else:
        status_label.configure(text="No video loaded to download.")

def fetch_video_info():
    url = url_entry.get()
    if url:
        try:
            yt = YouTube(url)
            video_title_label.configure(text=f"{yt.title}")
            status_label.configure(text="Video information loaded.")
            download_button.configure(state="normal")
            global current_youtube_object
            current_youtube_object = yt

            # Get the thumbnail URL
            thumbnail_url = yt.thumbnail_url
            try:
                response = requests.get(thumbnail_url)
                response.raise_for_status()  # Raise an exception for bad status codes
                image_data = BytesIO(response.content)
                pil_image = Image.open(image_data)
                # Resize the image if it's too large
                pil_image = pil_image.resize((500, 281))  # Adjust size as needed
                tk_image = ImageTk.PhotoImage(pil_image)
                thumbnail_label.configure(image=tk_image)
                thumbnail_label.image = tk_image  # Keep a reference to avoid garbage collection
                thumbnail_label.configure(text="")  # Clear any previous text
            except requests.exceptions.RequestException as e:
                thumbnail_label.configure(text=f"Error loading thumbnail: {e}")
                thumbnail_label.image = None
            except Exception as e:
                thumbnail_label.configure(text=f"Error processing thumbnail: {e}")
                thumbnail_label.image = None

        except Exception as e:
            status_label.configure(text=f"Error fetching video info: {e}")
            video_title_label.configure(text="Title:")
            video_author_label.configure(text="Author:")
            thumbnail_label.configure(image=None, text="No Thumbnail")
            download_button.configure(state="disabled")
    else:
        status_label.configure(text="Please enter a YouTube URL.")
        video_title_label.configure(text="Title:")
        video_author_label.configure(text="Author:")
        thumbnail_label.configure(image=None, text="No Thumbnail")
        download_button.configure(state="disabled")

download_area_button = customtkinter.CTkButton(
    left_frame,
    text="Get Info",  # Changed button text to reflect its action
    text_color="white",
    font=label_font,
    corner_radius=15,
    fg_color="#f17634",
    hover_color="#ff8a37",
    command=fetch_video_info,
)
download_area_button.pack(side="bottom", anchor="w", pady=(0, 10), padx=20) # Adjusted padding

# RIGHT FRAME
right_frame = customtkinter.CTkFrame(
    mainwindow,
    fg_color="#121212",
    width=675,
    height=825,
    corner_radius=0,
)
right_frame.pack(side="left", fill="both", expand=True)
right_frame.pack_propagate(False)

label_wrapper_right = customtkinter.CTkFrame(
    right_frame,
    fg_color="#f17634",
    corner_radius=15,
)
label_wrapper_right.pack(pady=(20, 0), padx=20, anchor="w")

convert_area_label = customtkinter.CTkLabel(  # Changed label text to match the description
    label_wrapper_right,
    text="Convert area",
    text_color="white",
    font=label_font,
    fg_color="transparent",
)
convert_area_label.pack(padx=20, pady=1)

convert_description_label = customtkinter.CTkLabel(  # Changed label text to match the description
    right_frame,
    text="Convert all sorts of files here,\nfrom images to files & documents!",
    text_color="white",
    font=description_font,
    anchor="w",
    justify="left",
)
convert_description_label.pack(pady=20, padx=25, anchor="w")

mainwindow.mainloop()