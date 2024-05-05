import flet as ft
import json
import os

def load_video_data():
    with open("proyectoHack/assets/videos.json", "r") as f:
        return json.load(f)

data = load_video_data()

def create_sample_media(data):
    video_paths = [ft.VideoMedia(value["path"]) for key, value in data["sample_media"].items()]
    return video_paths

sample_media = create_sample_media(data)

current_video_index = 0  # Track the current video index globally
btn_yes = None
btn_no = None

def handle_vote(vote, page):
    global current_video_index, data, btn_yes, btn_no
    video_name = list(data["sample_media"].keys())[current_video_index]
    data["sample_media"][video_name][f"number_of_{vote}"] += 1
    with open("proyectoHack/assets/videos.json", "w") as f:
        json.dump(data, f, indent=4)
    
    current_video_index += 1
    if current_video_index >= len(sample_media):
        # Disable buttons and clear the video player
        btn_yes.enabled = False
        btn_no.enabled = False
        page.update()
        print("All videos have been viewed and voted on.")
    else:
        video_player.next()  # Move to the next video

def main(page: ft.Page):
    global video_player, sample_media, current_video_index, btn_yes, btn_no
    page.update()

    video_player = ft.Video(
        expand=True,
        playlist=sample_media,
        playlist_mode=ft.PlaylistMode.SINGLE,  # Loop the current video indefinitely
        volume=100,
        autoplay=True,
        show_controls=False
    )

    page.add(video_player)

    # Voting buttons
    btn_yes = ft.FilledButton(text="YES", on_click=lambda e: handle_vote("yes", page))
    btn_no = ft.FilledButton(text="NO", on_click=lambda e: handle_vote("no", page))

    page.add(ft.Row(controls=[btn_yes, btn_no]))

ft.app(target=main)
