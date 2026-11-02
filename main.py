import os
import threading
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import yt_dlp


class VideoDownloaderApp(App):

  def build(self):
    self.title = "Descargador de Videos"
    self.download_folder = App.get_running_app().user_data_dir

    # Layout principal
    layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

    # Título
    self.label_title = Label(
        text="📥 Descargador YouTube / TikTok / Reels",
        font_size=18,
        size_hint_y=None,
        height=50,
    )
    layout.add_widget(self.label_title)

    # Campo de texto para el enlace
    self.url_input = TextInput(
        hint_text="Pega aquí el enlace del video...",
        size_hint_y=None,
        height=50,
        multiline=False,
    )
    layout.add_widget(self.url_input)

    # Botón de descarga
    self.download_btn = Button(
        text="Descargar Video",
        size_hint_y=None,
        height=55,
        background_color=(0.06, 0.72, 0.5, 1),
    )
    self.download_btn.bind(on_press=self.start_download)
    layout.add_widget(self.download_btn)

    # Etiqueta de estado
    self.status_label = Label(
        text="", font_size=14, size_hint_y=None, height=40
    )
    layout.add_widget(self.status_label)

    return layout

  def start_download(self, instance):
    url = self.url_input.text.strip()
    if not url:
      self.status_label.text = "⚠️ Por favor pega una URL válida."
      return

    self.download_btn.disabled = True
    self.status_label.text = "⏳ Descargando video..."

    # Ejecutar en segundo plano para no congelar la app móvil
    threading.Thread(
        target=self.download_video_task, args=(url,), daemon=True
    ).start()

  def download_video_task(self, url):
    ydl_opts = {
        "format": "best",
        "outtmpl": os.path.join(self.download_folder, "%(title)s.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
    }

    try:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

      Clock.schedule_once(
          lambda dt: self.update_ui_success("✅ ¡Video descargado con éxito!")
      )
    except Exception as e:
      error_text = f"❌ Error: {str(e)[:40]}"
      Clock.schedule_once(lambda dt: self.update_ui_error(error_text))

  def update_ui_success(self, message):
    self.status_label.text = message
    self.url_input.text = ""
    self.download_btn.disabled = False

  def update_ui_error(self, message):
    self.status_label.text = message
    self.download_btn.disabled = False


if __name__ == "__main__":
  VideoDownloaderApp().run()