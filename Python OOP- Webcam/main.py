from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
# pip install filestack-python
from filestack import Client
from kivy.core.clipboard import Clipboard
import time
import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop The Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start The Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        # the files Directory, you will need to create it yourself:
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        # The Screen that the User is currently looking at:
        # This is for the self.manager: When we actually set
        # it to the filename, it mean to say that the screen capture
        # will capture that particular instance of the image:
        self.manager.current_screen.ids.img.source = self.filepath


class FileSharer:
    # Need to create the FileSharer Account in dev.filestack.com to
    # get the API Key:
    def __init__(self, filepath, api_key='AsDrF9tmiQxDcifnPLdHhz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url


class ImageScreen(Screen):
    link_message = "Create a Link First"
    def create_link(self):
        """Access the photo filepath, upload to the web
           and insert the link into the Label Widget Application"""
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath=filepath)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """Copy the Links to the Clipboard for Pasting Purpose"""
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """Open the Link with the Default Browser"""
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()

# Note:
# If the code does not run properly
# turn off your Window Firewall and also
# download the following Python Libraries:
# pip install pygobject
# pip install opencv-python
# pip install picamera
