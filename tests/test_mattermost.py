from unittest import TestCase
from nose.tools import eq_
from mattermost_client import mattermost_cl

mmc = mattermost_cl.MatterMostClient("http://10.125.75.11:8065/hooks/qs4uzy4b1py98qjpiut93sewzw")


class MMCTestCase(TestCase):

    def test_send_message_only(self):
        resp = mmc.send_message("test")
        eq_(resp.text, 'ok')
