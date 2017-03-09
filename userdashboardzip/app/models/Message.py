from system.core.model import Model
import re,md5,os,binascii,time,datetime
class Message(Model):
    def __init__(self):
        super(Message, self).__init__()
    
    def wall(self,id):
        print 'weall', id
        messages_query = "SELECT concat(users.first_name, ' ', users.last_name) as postUsername, messages.id, messages.user_id, messages.message_recipient_user_id, messages.message, messages.created_at FROM messages join users on users.id = messages.user_id where messages.message_recipient_user_id = :id order by messages.created_at desc"
        # messages_query = "SELECT * from messages"
        messages_data = {
            'id':id
        }
        messages = self.db.query_db(messages_query, messages_data)


        comments_query = "SELECT concat(users.first_name, ' ', users.last_name) as commentUsername,comments.id, comments.message_id, comments.user_id, comments.comment, comments.created_at FROM comments join users on users.id = comments.user_id order by comments.created_at asc"
        print 'this are the comments'
        comments = self.db.query_db(comments_query)
        print comments

        return {'messages':messages, 'comments':comments}
    
    def postmessage(self,id,message_recipient_user_id,message):
        print 'looool'
        print 'looool'
        print 'looool'
        print id,message_recipient_user_id,message
        messages_query = 'INSERT INTO messages(user_id, message_recipient_user_id, message, created_at, updated_at) VALUES (:user_id, :message_recipient_user_id, :message, NOW(), NOW())'
        messages_data = {
            'user_id':message_recipient_user_id,
            'message_recipient_user_id':id,
            'message':message
        }
        self.db.query_db(messages_query, messages_data)
        return True

    def postcomment(self,comment_message_id,commenter_user_id,comment):
        if len(comment_message_id) <= 0:
            # flash(u'Message cannot be empty\n', 'messageError')
            print 'false'
        else:
            query = "INSERT INTO comments (message_id,user_id, comment, created_at, updated_at) VALUES (:messageid,:userid,:message,NOW(), NOW())"
            data = {
                # 'userid': session['userID'],
                'messageid': comment_message_id,
                'userid': commenter_user_id,
                'message': comment
            }
            self.db.query_db(query, data)
            print 'success'
        return True