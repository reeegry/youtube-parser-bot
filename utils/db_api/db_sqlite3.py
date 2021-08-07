import sqlite3
import logging

logging.basicConfig(format=u"%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s",
                    level=logging.INFO)


class SQLighter:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.db_create())

    @staticmethod
    def db_create():
        return """
        CREATE TABLE IF NOT EXISTS "subscriptions" (
        "id"	INTEGER,
        "user_id" VARCHAR(255) NOT NULL, 
        "status" BOOLEAN NOT NULL DEFAULT 'True',
        "channel"	TEXT, 
        "last_video_url"	TEXT,
        "last_video_title"	TEXT,
        "send_message"	BOOLEAN DEFAULT 'False',
        PRIMARY KEY("id" AUTOINCREMENT)
        );
        """

    def get_subscriptions(self, status=True):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def get_user_info(self, user_id, status):
        with self.connection:
            return self.cursor.execute("SELECT * FROM `subscriptions` WHERE `status` = ? AND `user_id` = ?", (status,
                                                                                                              user_id))

    def subscriber_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO `subscriptions` (`user_id`, `status`) VALUES(?,?)", (user_id,
                                                                                                         status))
    # TODO: replace all update methods with one

    def update_video_title(self, user_id, last_video_title, status=True):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `last_video_title` = ? WHERE `user_id` = ?",
                                       (last_video_title, user_id))

    def update_video_url(self, user_id, last_video_url, status=True):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `last_video_url` = ? WHERE `user_id` = ?",
                                       (last_video_url, user_id))

    def update_subscription(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def update_channel(self, user_id, channel):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `channel` = ? WHERE `user_id` = ?", (channel,
                                                                                                        user_id))

    def change_send_message_status(self, user_id, send_message):
        with self.connection:
            return self.cursor.execute("UPDATE `subscriptions` SET `send_message` = ? WHERE `user_id` = ?",
                                       (send_message, user_id))

    def close(self):
        self.connection.close()


db = SQLighter("utils/db_api/db.db")
