import customtkinter
from customtkinter import CTkFont

mainwindow = customtkinter.CTk()
mainwindow.geometry("1350x825")
mainwindow.title("Eduu's Media Utility")
mainwindow.resizable(False, False)

label_font = customtkinter.CTkFont(size=50)
description_font = customtkinter.CTkFont(size=25)
url_font = customtkinter.CTkFont(size=20)

#LEFT FRAME
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
    text="Download youtube videos or\nspotify musics & playlists here!",
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
url_label.pack(pady=10,padx=10)

url_entry = customtkinter.CTkEntry(
    left_frame,
    placeholder_text="Youtube/Spotify Link Here!",
    font=description_font,
    width=700,
    height=70,
    corner_radius=15,
)
url_entry.pack(pady=1, padx=20,anchor="w")

download_area_button = customtkinter.CTkButton(
    left_frame,
    text="Download",
    text_color="white",
    font=label_font,
    corner_radius=15,
    fg_color="#f17634",
    hover_color="#ff8a37",
)
download_area_button.pack(side="bottom", anchor="w", pady=(0,20), padx=20)

#RIGHT FRAME
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

download_area_label = customtkinter.CTkLabel(
    label_wrapper_right,
    text="Convert area",
    text_color="white",
    font=label_font,
    fg_color="transparent",
)
download_area_label.pack(padx=20, pady=1)

download_description_label = customtkinter.CTkLabel(
    right_frame,
    text="Convert all sorts of files here,\nfrom images to files & documents!",
    text_color="white",
    font=description_font,
    anchor="w",
    justify="left",
)
download_description_label.pack(pady=20, padx=25, anchor="w")

mainwindow.mainloop()