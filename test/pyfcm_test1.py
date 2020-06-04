# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAl7NnNWQ:APA91bFAgIWcesU6lSac6lxazKtt-TPAtH_2mnonEhtQ9TOyO3S6u3ZvSxZN2hQj_vJQzTE4h10j9-GKGMiFlQHDDcSoFD2h1sR5zQ6azKssvh4zjNAGLgSOMPfmthW5RPqQ8gKmszpt")

# OR initialize with proxies

# proxy_dict = {
#           "http"  : "http://127.0.0.1",
#           "https" : "http://127.0.0.1",
#         }
# push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

# registration_id = "cS5nVkZX_B8:APA91bEl5r-C6_CCbEmogaDT4fduJTmex5qMou6_AE5q_kXwo9LmI9vPfL_mc3rq7YE6LtO0VnfCH3iH9rTU0hJX27u-5mgCEArQa7pDzT6mkToi0sBuwGu-MgMAmpYKmFbvZKvgGEb0"
#@ fcmtest3용 토큰
registration_id = "etm6cyIuqfc:APA91bFzX8V-MaeIH9D6bMaZQAjwExeksmUGbD87QGKFaGguFrjIICEpkRMfE3jvyGlhpHtAuiRRb3rja3slAiJHBrm2AoN8TXd7bF3g74aJfrogadBstvsfdU5j_JpCB_v60uJtz-AX"

        # push_service = FCMNotification(api_key="AAAAl7NnNWQ:APA91bFAgIWcesU6lSac6lxazKtt-TPAtH_2mnonEhtQ9TOyO3S6u3ZvSxZN2hQj_vJQzTE4h10j9-GKGMiFlQHDDcSoFD2h1sR5zQ6azKssvh4zjNAGLgSOMPfmthW5RPqQ8gKmszpt")
        # registration_id = "etm6cyIuqfc:APA91bFzX8V-MaeIH9D6bMaZQAjwExeksmUGbD87QGKFaGguFrjIICEpkRMfE3jvyGlhpHtAuiRRb3rja3slAiJHBrm2AoN8TXd7bF3g74aJfrogadBstvsfdU5j_JpCB_v60uJtz-AX"
#@getStyle 용 토큰
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print(result)
