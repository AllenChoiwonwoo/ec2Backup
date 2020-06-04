
from txfcm import TXFCMNotification
from twisted.internet import reactor
# import baseapi

push_service = TXFCMNotification(api_key="AAAAl7NnNWQ:APA91bFAgIWcesU6lSac6lxazKtt-TPAtH_2mnonEhtQ9TOyO3S6u3ZvSxZN2hQj_vJQzTE4h10j9-GKGMiFlQHDDcSoFD2h1sR5zQ6azKssvh4zjNAGLgSOMPfmthW5RPqQ8gKmszpt")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
# Send to multiple devices by passing a list of ids.
registration_ids = ["651549947236"]
message_title = "Uber update"
message_body = "Hope you're having fun this weekend, don't forget to check today's news"
df = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
#
# registration_id = "1:651549947236:android:aff4805df7090991"
# message_title = "Uber update"
# message_body = "Hi john, your customized news for today is ready"
# result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


def got_result(result):
    print(result)

df.addBoth(got_result)
reactor.run()
