import requests  # to GET from Instagram API
import json     # to gather local data
import re       # to extract links
import logging  # to log information


class InstagramPuller:
    def __init__(self, access_token, data_path, log_path):
        self.access_token = access_token
        self.data_path = data_path
        self.log_path = log_path

        # automatically cache the data
        self.set_remote_data()
        self.set_local_data()
        self.set_new_data()

    # add caption to the JSON data
    def add_caption(self, data):
        for x in data:
            x.update(links=",".join(
                map(str, re.findall(r"(https?://[^\s]+)", x["caption"]))))
        return data

    # collect data from remote
    def set_remote_data(self):
        request_url = f"https://graph.instagram.com/me/media?fields=id,media_url,caption,timestamp&access_token={self.access_token}"
        response = requests.get(request_url)
        response_data = response.json()["data"]
        self.remote_data = self.add_caption(response_data)

    # collect data from local storage
    def set_local_data(self):
        with open(f"{self.data_path}/post_data.json",) as local_file:
            self.local_data = json.load(local_file)

    # extract new data (requires remote and local set)
    def set_new_data(self):
        self.new_data = [
            x for x in self.remote_data if x not in self.local_data]

    # process any new images
    def process_images(self):
        # get the images
        image_tuples = [(x["id"], x["media_url"]) for x in self.new_data]
        for (image_id, image) in image_tuples:
            with open(f"{self.data_path}/images/{image_id}.png", "wb") as handle:
                im_response = requests.get(image, stream=True)
                for block in im_response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)

    # process the JSON data
    def process_json(self):
        # prepend to the existing json data
        total_data = self.new_data + self.local_data

        with open(f"{self.data_path}/post_data.json", "w") as write_file:
            json.dump(total_data, write_file)

    # set the data that has been pulled
    def set_data(self):
        self.process_images()
        self.process_json()
