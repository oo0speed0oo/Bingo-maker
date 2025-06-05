import os

class ImageLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.images = {}

    def load_images(self):
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(".jpg") or filename.lower().endswith(".png"):
                path = os.path.join(self.folder_path, filename)
                # Store path instead of loading the image now
                self.images[filename] = path

    def get_images(self):
        return self.images