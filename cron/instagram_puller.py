import requests  # to GET from Instagram API
import json     # to gather local data
import re       # to extract links
from PIL import Image
from resizeimage import resizeimage


class InstagramPuller:
    def __init__(self, access_token, data_path, temp_path, image_path):
        self.access_token = access_token
        self.data_path = data_path
        self.temp_path = temp_path
        self.image_path = image_path

        # automatically cache the data
        self.set_remote_data()
        self.set_local_data()
        self.set_new_data()

    # add caption to the JSON data
    def add_caption(self, data):
        for x in data:
            x.update(category=",".join(
                map(str, re.findall(r"(https?://[^\s]+)", x["caption"]))))
        return data

    # collect data from remote
    def set_remote_data(self):
        request_url = f"https://graph.instagram.com/me/media?fields=id,media_url,caption,timestamp&access_token={self.access_token}"
        response = requests.get(request_url)
        if response.ok:
            response_data = response.json()["data"]
            self.remote_data = self.add_caption(response_data)
        else:
            raise Exception(
                f"When trying to access Instagram API, received response code {response.status_code}: {response.reason}")

    # collect data from local storage
    def set_local_data(self):
        with open(f"{self.data_path}/resumeData.json",) as local_file:
            self.local_json = json.load(local_file)
            self.local_data = self.local_json["portfolio"]["posts"]

    # extract new data (requires remote and local set)
    def set_new_data(self):
        self.new_data = [
            x for x in self.remote_data if x not in self.local_data]

    # process any new images
    def process_images(self):
        # get the images
        image_tuples = [(x["id"], x["media_url"]) for x in self.new_data]
        for (image_id, image) in image_tuples:
            with open(f"{self.temp_path}/{image_id}.png", "wb") as handle:
                im_response = requests.get(image, stream=True)
                for block in im_response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            with Image.open(f"{self.temp_path}/{image_id}.png") as img:
                width, height = img.size
                dim = max(width, height)
                img = resizeimage.resize_contain(img, [dim, dim])
                img.save(f"{self.image_path}/{image_id}.png")

    # process the JSON data
    def process_json(self):
        with open(f"{self.data_path}/resumeData.json", "w") as write_file:
            new_data = dict(self.local_json)
            new_data["portfolio"] = {"posts" : self.remote_data}
            json.dump(new_data, write_file)

    # set the data that has been pulled
    def set_data(self):
        self.process_images()
        self.process_json()

 
