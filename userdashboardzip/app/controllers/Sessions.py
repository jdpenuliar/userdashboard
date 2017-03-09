from system.core.controller import *

class Sessions(Controller):
    def __init__(self, action):
        super(Sessions, self).__init__(action)
        self.load_model('User')
        self.db = self._app.db
    def index(self):
        if session.get('userid')!= None:
            return redirect('/users')
        else:
            return self.load_view('/sessions/index.html')
    def signin(self):
        return self.load_view('/sessions/signin.html')

    def signup(self):
        if session.get('errors') != None:
            for key, data in session['errors'].iteritems():
                flash(data, key)
            session.pop('errors')
        return self.load_view('/sessions/register.html')

    def register(self):
        result = self.models['User'].register(request.form)
        print result
        if result['status'] == True:
            print 'whyyyyyy'
            print 'whyyyyyy'
            print 'whyyyyyy'
            print 'whyyyyyy'
            print 'whyyyyyy'
            print 'whyyyyyy'
            print 'whyyyyyy'
            if session.get('userid') == None:
                session['userid'] = result['registered_user'][0]['id']
                session['userlevel'] = result['registered_user'][0]['user_level']
            return redirect('/')
        else:
            session['errors'] = result['errors']
            return redirect('/signup')

    def login(self):
        print 'login'
        print 'login'
        print 'login'
        print 'login'
        print 'login'
        print 'login'
        print 'login'
        print 'login'
        login_status = self.models['User'].login(request.form)

        print 'login status'
        print 'login status'
        print 'login status'
        print 'login status'
        print 'login status'
        print 'login status'
        print 'login status'
        print 'login status'
        print 'login status'
        print login_status
        print login_status['status']
        if login_status['status']==False or login_status == None:
            if login_status['errors']['emailError'] != None:
                flash(login_status['errors']['emailError'],'emailError')
            if login_status['errors']['passwordError'] != None:
                flash(login_status['errors']['passwordError'],'passwordError')
            if login_status['errors']['invalidCredentialError'] != None:
                flash(login_status['errors']['invalidCredentialError'],'invalidCredentialError')
            return redirect('/signin')
        else:
            session['userid'] = login_status['loggedin_user'][0]['id']
            session['name'] = login_status['loggedin_user'][0]['first_name']+ ' '+login_status['loggedin_user'][0]['last_name']
            session['userlevel'] = login_status['loggedin_user'][0]['user_level']
            return redirect('/users')
    def logoff(self):
        if session.get('userid') != None:
            session.pop('userid')
        return redirect('/')