import requests # to GET from Instagram API
import json     # to gather local data
import re       # to extract links

class InstagramPuller:
    def __init__(self, access_token, data_path, log_path):
        self.access_token = access_token
        self.data_path = data_path
        self.log_path = log_path
        self.remote_data = self.get_remote()
        self.local_data = self.get_local()

    def get_remote(self):
        request_url = f"https://graph.instagram.com/me/media?fields=id,media_url,caption,timestamp&access_token={self.access_token}"
        response = requests.get(request_url)
        response_data = response.json()["data"]
        return response_data

    def get_local(self):
        with open(f"{self.data_path}/post_data.json",) as local_file:
            post_data = json.load(local_file)
        return post_data

    # ask the Instagram API for the image IDs
    def get_remote_ids(self):
        return [x["id"] for x in self.remote_data]

    # retrieve the current IDs
    def get_current_ids(self):
        return [x["id"] for x in self.local_data]

    # if there are new IDs, retrieve this information
    def pull(self):
        remote_ids = self.get_remote_ids()
        current_ids = self.get_current_ids()
        new_ids = [x for x in remote_ids if x not in current_ids]
        filtered_data = [x for x in self.remote_data if x["id"] in new_ids]

        # get the images
        image_tuples = [(x["id"], x["media_url"]) for x in self.remote_data]
        for (image_id, image) in image_tuples:
            with open(f"{self.data_path}/images/{image_id}.png", "wb") as handle:
                im_response = requests.get(image, stream=True)
                for block in im_response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)

        # add the links to the remote_ids
        
        for x in filtered_data:
            x.update(links=",".join(map(str, re.findall(r"(https?://[^\s]+)", x["caption"]))))

        # prepend to the existing json data
        new_data = filtered_data + self.local_data
            
        with open(f"{self.data_path}/post_data.json", "w") as write_file:
            json.dump(new_data, write_file)
