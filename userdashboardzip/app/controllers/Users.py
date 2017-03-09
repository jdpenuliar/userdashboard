from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        
        self.load_model('User')
        self.load_model('Message')
        self.db = self._app.db

    def index(self):
        if session.get('userid')!= None:
            print 'session userlevel'
            print 'session userlevel'
            print 'session userlevel'
            print 'session userlevel'
            print 'session userlevel'
            print 'session userlevel'
            print 'session userlevel'
            print 'session userlevel'
            print 'session userlevel'
            print session['userlevel']

            if session['userlevel'] == 9:
                return redirect('/dashboard/admin')
            else:
                return redirect('/dashboard')
        else:
            return redirect('/signin')
    
    def dashboard(self):
        print 'dashboard'
        print 'dashboard'
        print 'dashboard'
        print 'dashboard'
        print 'dashboard'
        print 'dashboard'
        print 'dashboard'
        print 'dashboard'
        print session['userlevel']
        if session.get('userid')!= None:
            if session['userlevel'] == 1:
                users = self.models['User'].getallusers()
                print users
                return self.load_view('/users/dashboard.html',users=users)
            else:
                return redirect('/logout')
        else:
            return redirect('/logout')

    def dashboardadmin(self):

        print 'dashboardadmin'
        print 'dashboardadmin'
        print 'dashboardadmin'
        print 'dashboardadmin'
        print 'dashboardadmin'
        print 'dashboardadmin'
        print 'dashboardadmin'
        print session['userlevel']
        if session.get('userid')!= None:
            if session['userlevel'] == 9:
                
                users = self.models['User'].getallusers()
                print users
                return self.load_view('/users/dashboardadmin.html',users=users)
            else:
                return redirect('/logout')
        else:
            return redirect('/signin')



    def show(self,id):
        if session.get('userid')!= None:
            user = self.models['User'].showuser(id)
            result = self.models['Message'].wall(id)

            return self.load_view('/users/show.html',id = id, user=user, messages=result['messages'], comments = result['comments'])
        else:
            return redirect('/logout')
    def useredit(self):
        if session.get('userid')!= None:
            user = self.models['User'].showuser(session['userid'])
            return self.load_view('/users/useredit.html',user=user)
        else:
            return redirect('/logout')
    def adminedit(self,id):
        if session.get('userid')!= None and session['userlevel'] == 9:
            user = self.models['User'].showuser(id)
            return self.load_view('/users/adminedit.html',user=user)
        else:
            return redirect('/logout')

    def adminupdate(self,id):
        if session.get('userid')!= None and session['userlevel'] == 9:
            print 'admin update'
            # print request.form
            # print 'dictionary'
            # print request.form['first_name']
            # I will put in the dictionary with specific request forms as an argument in the
            #model because if I put in the 'request.form' it returns an Immutable multi dict
            info = {
                'first_name':request.form['first_name'],
                'last_name':request.form['last_name'],
                'email':request.form['email'],
                'user_level':request.form['user_level'],
                'password':request.form['password'],
                'confirm_password':request.form['confirm_password']
            }
            # print info

            updated_user = self.models['User'].adminupdateuser(id,info)
            print updated_user
            print 'admin update finish'
            return redirect('/')
            user = self.models['User'].showuser(id)
            return self.load_view('/users/adminedit.html',user=user)
        else:
            return redirect('/logout')

    def userupdate(self):
        if session.get('userid')!= None:
            print 'admin update'
            # print request.form
            # print 'dictionary'
            # print request.form['first_name']
            # I will put in the dictionary with specific request forms as an argument in the
            #model because if I put in the 'request.form' it returns an Immutable multi dict
            info = {
                'first_name':request.form['first_name'],
                'last_name':request.form['last_name'],
                'email':request.form['email'],
                'description':request.form['description'],
                'password':request.form['password'],
                'confirm_password':request.form['confirm_password']
            }
            # print info

            updated_user = self.models['User'].userupdate(session['userid'],info)
            print updated_user
            print 'admin update finish'
            return redirect('/users/edit')
            # user = self.models['User'].showuser(id)
            # return self.load_view('/users/adminedit.html',user=user)
        else:
            return redirect('/logout')
        
    def adminconfirmremove(self,id):
        if session.get('userid')!= None and session['userlevel'] == 9:
            
            return self.load_view('/users/adminconfirmdelete.html',id=id)
        else:
            return redirect('/logout')
        
    def new(self):
        if session.get('userid')!= None:
            if session['userlevel'] == 9:
                return self.load_view('/users/new.html')
            else:
                return redirect('/logout')
        else:
            return redirect('/logout')

    def edit(self,id):
        #edit
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'
        print 'edit'+id
        return redirect('/users')

    def remove(self,id):
        #remove
        print 'remove'+id
        if request.form['action'] == "Yes":
            self.models['User'].adminremove(id)
        return redirect('/users')

    def message(self,id):
        if session.get('userid')!= None:
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print request.form['message']
            result = self.models['Message'].postmessage(id,message_recipient_user_id = session['userid'],message=request.form['message'])
            print result
            print 'done'
            # return self.load_view('/users/show.html',id = id, user_messenger_id = session['userid'])
            return redirect('/users/show/'+id)
        else:
            return redirect('/logout')
    def comment(self,id):
        if session.get('userid')!= None:
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print 'request asdflkjasd;lfkjasdf'
            print request.form['commentMessageID']
            print request.form['message']
            result = self.models['Message'].postcomment(comment_message_id=request.form['commentMessageID'], commenter_user_id= session['userid'],comment=request.form['message'])
            print 'done'
            # return self.load_view('/users/show.html',id = id, user_messenger_id = session['userid'])
            return redirect('/users/show/'+id)
        else:
            return redirect('/logout')