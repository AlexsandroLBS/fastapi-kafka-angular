from db.database import Database
from api.schema import Notification


class Process:
    def __init__(self, ) -> None:    
        self.db = Database()

    def sendDatabase(self, data: Notification):
        self.db.execAction(data)
        
        