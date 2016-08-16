import requests
import json
import exceptions


class MatterMostClient(object):
    """
    Send message to Mattermost using incomming web hook
    """

    def __init__(self, url):
        self.__mattermosturl = url

    def send_message(self, message, username='PythonClient',
                     icon_url=None, icon_emoji=None):
        """
        :param message: message which you want to send.
        :param username: username shown on chat.(default: PythonClient)
        :param icon_url: icon shown on chat. you specify
                            url for image.(default: None)
        :param icon_emoji: icon shown on chat.
                            specify :emoji: (default: None)

         Usage::

            >>> mmc = MatterMostClient(MATTERMOSTURL)
            >>> mmc.send_message("This is test")

        """
        header = {'Content-Type': 'application/json'}
        payload = {
                "text": message,
                "username": username,
                }
        if icon_url is not None:
            payload['icon_url'] = icon_url
        if icon_emoji is not None:
            payload['icon_emoji'] = icon_emoji

        resp = requests.post(self.__mattermosturl,
                             headers=header, data=json.dumps(payload))

        if resp.status_code >= 400:

            if resp.text:
                try:
                    body = json.load(resp.text)
                except (ValueError, AttributeError):
                    pass
                    body = None
            else:
                body = None

            raise exceptions.from_response(resp, body)

        return resp
