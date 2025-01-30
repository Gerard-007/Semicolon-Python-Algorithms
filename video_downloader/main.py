from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import mainthread
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.button import MDRoundFlatIconButton
import os
import threading
from yt_dlp import YoutubeDL

KV = '''
MDScreen:
    md_bg_color: app.theme_cls.bg_normal
    padding: dp(20)

    ScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            adaptive_height: True
            padding: dp(10)

            MDCard:
                orientation: 'vertical'
                padding: dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height
                elevation: 2
                radius: dp(15)

                MDIconButton:
                    icon: "link"
                    pos_hint: {'center_x': 0.5}
                    theme_text_color: "Secondary"

                MDTextField:
                    id: url_input
                    hint_text: "YouTube URL"
                    mode: "fill"
                    fill_color: app.theme_cls.bg_normal
                    icon_left: "web"
                    radius: dp(10)

                MDRoundFlatIconButton:
                    text: "Choose Directory"
                    icon: "folder-outline"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    line_color: app.theme_cls.primary_color
                    on_release: app.open_file_chooser()
                    pos_hint: {'center_x': 0.5}

                MDLabel:
                    text: app.save_directory if app.save_directory else "No directory selected"
                    halign: "center"
                    font_style: "Caption"
                    theme_text_color: "Secondary"

            MDCard:
                orientation: 'vertical'
                padding: dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height
                elevation: 2
                radius: dp(15)

                MDIconButton:
                    icon: "quality-high"
                    pos_hint: {'center_x': 0.5}
                    theme_text_color: "Secondary"

                MDTextField:
                    id: filename
                    hint_text: "Custom filename (optional)"
                    mode: "fill"
                    fill_color: app.theme_cls.bg_normal
                    icon_left: "text-box-outline"
                    radius: dp(10)

                MDRoundFlatIconButton:
                    text: "Select Quality"
                    icon: "video-quality"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    line_color: app.theme_cls.primary_color
                    on_release: app.open_quality_menu()
                    pos_hint: {'center_x': 0.5}

                MDLabel:
                    text: f"Selected Quality: {app.selected_quality}"
                    halign: "center"
                    font_style: "Body2"
                    theme_text_color: "Primary"

            MDCard:
                id: progress_card
                orientation: 'vertical'
                padding: dp(20)
                spacing: dp(15)
                size_hint_y: None
                height: self.minimum_height
                elevation: 2
                radius: dp(15)
                md_bg_color: app.theme_cls.secondaryContainerColor

                MDProgressBar:
                    id: progress_bar
                    value: app.progress
                    color: app.theme_cls.primary_color

                MDLabel:
                    text: app.status_message
                    halign: "center"
                    font_style: "Caption"
                    theme_text_color: "Secondary"

                MDRoundFlatIconButton:
                    id: download_btn
                    text: "Download" if not app.downloading else "Downloading..."
                    icon: "download-outline" if not app.downloading else "progress-download"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    line_color: app.theme_cls.primary_color
                    on_release: app.start_download()
                    pos_hint: {'center_x': 0.5}
                    disabled: app.downloading
'''

class YouTubeDownloader(MDApp):
    save_directory = StringProperty("")
    selected_quality = StringProperty("best")
    progress = NumericProperty(0)
    status_message = StringProperty("Ready to download")
    downloading = BooleanProperty(False)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def open_file_chooser(self):
        from plyer import filechooser
        try:
            paths = filechooser.choose_dir()
            if paths:
                self.save_directory = paths[0]
                Snackbar(
                    text=f"Directory set to: {self.save_directory}",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_x=(Window.width - (dp(10) * 2)) / Window.width
                ).open()
        except Exception as e:
            self.show_error(str(e))

    def open_quality_menu(self):
        qualities = [
            {"text": "Best Quality", "on_release": lambda x="best": self.set_quality(x)},
            {"text": "Audio Only", "on_release": lambda x="audio": self.set_quality(x)},
            {"text": "720p", "on_release": lambda x="720p": self.set_quality(x)},
            {"text": "1080p", "on_release": lambda x="1080p": self.set_quality(x)},
        ]
        self.quality_menu = MDDropdownMenu(
            caller=self.root.ids.url_input,
            items=qualities,
            width_mult=4,
            max_height=dp(200),
        )
        self.quality_menu.open()

    def set_quality(self, quality):
        self.selected_quality = quality
        self.quality_menu.dismiss()
        self.status_message = f"Quality set to: {quality}"

    def start_download(self):
        if not self.root.ids.url_input.text.strip():
            self.show_error("Please enter a YouTube URL")
            return
        if not self.save_directory:
            self.show_error("Please select a save directory")
            return

        self.downloading = True
        url = self.root.ids.url_input.text.strip()
        filename = self.root.ids.filename.text.strip()
        threading.Thread(target=self.download_media, args=(url, filename), daemon=True).start()

    def download_media(self, url, filename):
        try:
            self.update_status("Starting download...", 0)
            options = {
                "outtmpl": os.path.join(self.save_directory, f"{filename if filename else '%(title)s'}.%(ext)s"),
                "format": self.selected_quality,
                "progress_hooks": [self.progress_hook],
            }
            with YoutubeDL(options) as ydl:
                ydl.download([url])
            self.update_status("Download complete!", 100)
        except Exception as e:
            self.show_error(str(e))
        finally:
            self.downloading = False
            self.progress = 0

    @mainthread
    def progress_hook(self, d):
        if d["status"] == "downloading":
            downloaded = d.get("downloaded_bytes", 0)
            total = d.get("total_bytes", 1)
            progress = int((downloaded / total) * 100)
            self.update_status(f"Downloading... {progress}%", progress)
        elif d["status"] == "finished":
            self.update_status("Finalizing download...", 100)

    @mainthread
    def update_status(self, message, progress):
        self.status_message = message
        self.progress = progress

    @mainthread
    def show_error(self, message):
        Snackbar(
            text=message,
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(Window.width - (dp(10) * 2)) / Window.width,
            bg_color=(1, 0, 0, 0.8)
        ).open()

if __name__ == "__main__":
    YouTubeDownloader().run()