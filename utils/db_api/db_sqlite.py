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
        pass

    def close(self):
        self.connection.close()


class SQLUser(SQLighter):
    def __init__(self, database):
        super().__init__(database)
        self.youtube_table = SQLYoutube(database)
        self.twitch_table = SQLTwitch(database)

    @staticmethod
    def db_create():
        return """
        CREATE TABLE IF NOT EXISTS "user" (
	    "id"	INTEGER NOT NULL,
	    "status"	BOOLEAN NOT NULL DEFAULT 'True'
        );
        """

    def get_data(self, status=True):
        with self.connection:
            return self.cursor.execute("SELECT user.* FROM `user` LEFT JOIN youtube y on user.id=y.user_id WHERE `status` = ?", (status,)).fetchall()

    def subscriber_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_subscriber(self, user_id, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO `user` (`id`, `status`) VALUES(?, ?)", (user_id, status))

    def update_subscription(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `status` = ? WHERE `id` = ?", (status, user_id))


class SQLYoutube(SQLighter):
    def __init__(self, database):
        super().__init__(database)

    @staticmethod
    def db_create():
        return """
        CREATE TABLE IF NOT EXISTS "youtube" (
	    "user_id"	INTEGER REFERENCES user(id) NOT NULL,
	    "channel_id"	TEXT,
	    "last_video_url"	TEXT,
	    "last_video_title"	TEXT NOT NULL DEFAULT 'None',
	    "send_message"	BOOLEAN DEFAULT False
        );
        """
    
    def insert_youtube_data(self, user_id, channel_id, last_video_title, status=True):
        with self.connection:
            return self.cursor.execute("INSERT INTO `youtube` (`user_id`, `channel_id`, `last_video_title`) VALUES (?, ?, ?)",
                                      (user_id, channel_id, last_video_title))

    def update_video_url(self, user_id, last_video_url, status=True):
        with self.connection:
            return self.cursor.execute("UPDATE `youtube` SET `last_video_url` = ? WHERE `user_id` = ?",
                                      (last_video_url, user_id))

    def change_send_message_status(self, user_id, send_message):
        with self.connection:
            return self.cursor.execute("UPDATE `youtube` SET `send_message` = ? WHERE `user_id` = ?",
                                      (send_message, user_id))


class SQLTwitch(SQLighter):
    def __init__(self, database):
        super().__init__(database)

    @staticmethod
    def db_create():
        return """
        CREATE TABLE IF NOT EXISTS "twitch" (
	    "user_id"	INTEGER REFERENCES user(id) NOT NULL,
	    "channel_name"	TEXT,
	    "send_message"	BOOLEAN DEFAULT False
        );
        """

db = SQLUser("utils/db_api/db.db")