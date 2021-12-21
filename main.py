import uuid
from slack import SlackAPI


def test_slack():
    token = 'xoxb-2873001082209-2860360577010-5TO5dyOLkO6jC2owSqeSXzAC'
    request_id = str(uuid.uuid4())
    channel_name = "랜덤"
    channel_id = SlackAPI(token).get_channel_id(channel_name)
    message = SlackClient().get_requested_ts(channel_id, request_id)
    print(message)