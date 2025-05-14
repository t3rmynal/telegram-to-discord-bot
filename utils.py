import requests

user_data = {}

def send_discord_message(webhook_url, content, embed=False, color="#000000", username=None, avatar_url=None):
    data = {}

    if embed:
        data["embeds"] = [{
            "description": content,
            "color": int(color.replace("#", ""), 16)
        }]
    else:
        data["content"] = content

    if username:
        data["username"] = username
    if avatar_url:
        data["avatar_url"] = avatar_url

    response = requests.post(webhook_url, json=data)
    return response.status_code == 204