from custom_components.bluecon.notifications.CallEndNotification import CallEndNotification
from custom_components.bluecon.notifications.CallNotification import CallNotification
from custom_components.bluecon.notifications.INotification import INotification


class NotificationBuilder:
    @classmethod
    def fromNotification(cls, notification: dict, notificationId: str) -> INotification:
        if notification['FermaxNotificationType'] == "Call":
            return CallNotification(notification, notificationId)
        elif notification['FermaxNotificationType'] == "CallEnd":
            return CallEndNotification(notification)
        else:
            raise NotImplementedError