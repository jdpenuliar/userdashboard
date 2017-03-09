from system.core.model import Model
import re
class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def login (self,info):
		# We write our validations in model functions.
        # They will look similar to those we wrote in Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        
        dictionary_errors = {
            'emailError':'',
            'passwordError':'',
            'invalidCredentialError':''
        }
        errorCount = 0
        if len(info['email']) < 1:
            dictionary_errors['emailError']+='Email cannot be blank\n'
            errorCount+=1
        if not EMAIL_REGEX.match(info['email']):
            dictionary_errors['emailError']+='Email format must be valid!\n'
            errorCount+=1
        if len(info['password']) < 1:
            dictionary_errors['passwordError']+='Password cannot be blank\n'
            errorCount+=1
        if len(info['password']) <= 8:
            dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
            errorCount+=1
        
        if errorCount>0:
            return {"status": False, "errors": dictionary_errors}
        else:
            password = info['password']
            get_login_user_query = "SELECT * FROM users where email = :email"
            get_login_user_data = {
                'email':info['email']
            }
            
            user = self.db.query_db(get_login_user_query, get_login_user_data)

            if len(user) >0:
                if self.bcrypt.check_password_hash(user[0]['password'], password):
                    print user, '<--- this is the logged in user'
                    return { "status": True, 'loggedin_user':user}
                else:
                    dictionary_errors['invalidCredentialError']+='Invalid credentials!\n'
                    return {"status": False, "errors": dictionary_errors}
            else:
                dictionary_errors['invalidCredentialError']+='Invalid credentials!\n'
                return {"status": False, "errors": dictionary_errors}
    def register(self,info):
		emailRegrex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

		PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

		dictionary_errors = {
            'emailError':'',
            'firstNameError':'',
            'lastNameError':'',
            'passwordError':''
        }
		errorCount=0
		
		if len(info['email']) < 1:
			dictionary_errors['emailError']+='Email cannot be blank\n'
			errorCount+=1
		if not emailRegrex.match(info['email']):
			dictionary_errors['emailError']+='Email format must be valid!\n'
			errorCount+=1
		if len(info['first_name']) < 1:
			dictionary_errors['firstNameError']+='First name cannot be blank\n'
			errorCount+=1
		if len(info['last_name']) < 1:
			dictionary_errors['lastNameError']+='Last name cannot be blank\n'
			errorCount+=1
		if len(info['password']) < 1:
			dictionary_errors['passwordError']+='Password cannot be blank\n'
			errorCount+=1
		if len(info['confirm_password']) < 1:
			dictionary_errors['passwordError']+='Confirm cannot be blank\n'
			errorCount+=1
		if str(info['confirm_password']) != str(info['password']):
			dictionary_errors['passwordError']+='Password does not match\n'
			errorCount+=1
		if str(info['first_name']).isalpha() == False:
			dictionary_errors['firstNameError']+='First name must only contain letters\n'
			errorCount+=1
		if str(info['last_name']).isalpha() == False:
			dictionary_errors['lastNameError']+='Last name must only contain letters\n'
			errorCount+=1
		if len(info['password']) <= 8:
			dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
			errorCount+=1
		if PW_REGEX.match(info['password']) == None:
			dictionary_errors['passwordError']+='Password must have atleast 1 upper case, 1 lower case and 1 number!\n'
			errorCount+=1
		query = "SELECT * FROM users where email = :email"
		data = {
			'email': info['email']
		}
		emails = self.db.query_db(query,data)

		if len(emails)>0:
			dictionary_errors['emailError']+='Email already taken\n'
			errorCount+=1


		print 'errorrrrrrrrrr'
		print errorCount
		print dictionary_errors
		if errorCount>0:
			return {"status": False, "errors": dictionary_errors}
		else:
			password = info['password']
			hashed_pw = self.bcrypt.generate_password_hash(password)


			
			print 'haha'
			print 'haha'
			print 'haha'
			print 'haha'
			print 'haha'
			print 'haha'
			print 'haha'
			print 'haha'
			first_admin_check_query = 'SELECT * FROM users'
        	first_admin_check = self.db.query_db(first_admin_check_query)
        	print first_admin_check
        	print len(first_admin_check)
        	if len(first_admin_check) == 0:
        		user_level = 9
    		else:
    			user_level = 1
    		print user_level
    		print 'before insert'
    		print 'before insert'
    		print 'before insert'
    		print 'before insert'
    		print 'before insert'
    		print 'before insert'
    		print 'before insert'
    		register_query = 'INSERT INTO users(first_name, last_name, email, password, user_level, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, :user_level, NOW(), NOW())'
    		register_data = {
    			'first_name': info['first_name'],
    			'last_name': info['last_name'],
    			'email': info['email'],
    			'pw_hash': hashed_pw,
    			'user_level': user_level
    		}
    		self.db.query_db(register_query, register_data)

    		print 'registered'
    		print info['email']
    		get_login_user_query = 'SELECT * FROM users where email = :email'
    		get_login_user_data = {
    			'email':info['email']
    		}
    		user = self.db.query_db(get_login_user_query, get_login_user_data)
    		print user, '<----- this is the regisreterd user'
    		return { "status": True, 'registered_user':user}
    def getallusers(self):
        get_all_users_query = "SELECT * FROM users"
        users = self.db.query_db(get_all_users_query)
        return users
    def showuser(self,id):
        get_user_query = "SELECT * FROM users where id = :id"
        get_user_data = {
            'id':id
        }
        users = self.db.query_db(get_user_query,get_user_data)
        return users[0]
    def adminupdateuser(self,id,info):
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print info
        
        print 'a;lsdkfjas;dlkfjas;dlfkjas;dlfkjasd'
        emailRegrex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

        PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

        dictionary_errors = {
            'emailError':'',
            'firstNameError':'',
            'lastNameError':'',
            'passwordError':''
        }
        errorCount=0
        
        
        if len(info['first_name']) < 1:
            dictionary_errors['firstNameError']+='First name cannot be blank\n'
            errorCount+=1
        if len(info['last_name']) < 1:
            dictionary_errors['lastNameError']+='Last name cannot be blank\n'
            errorCount+=1
        if str(info['first_name']).isalpha() == False:
            dictionary_errors['firstNameError']+='First name must only contain letters\n'
            errorCount+=1
        if str(info['last_name']).isalpha() == False:
            dictionary_errors['lastNameError']+='Last name must only contain letters\n'
            errorCount+=1


        query = "SELECT * FROM users where email = :email and id = :id"
        data = {
            'email': info['email'],
            'id': id
        }
        emails = self.db.query_db(query,data)

        print 'emails'
        print 'emails'
        print 'emails'
        print 'emails'
        print 'emails'
        print emails
        print info
        if info['password'] == '':
            print 'password is noneee?'
        else:
            print 'kabiguan'


        if len(emails)>0:
            print 'eail? is noneee?'
        else:
            print 'kabiguan'

        if errorCount<=0 and len(emails)>0 and (info['password'] == ''):
            #names update
            #name is valid, email is the same as the previous, and no password update
            update_user_query = 'UPDATE users where id = :id set first_name = :first_name, last_name = :last_name, user_level = :user_level, updated_at = NOW()'

            print 'name update'
            update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, user_level = :user_level, updated_at = NOW() where id = :id'
            update_user_info = {
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'user_level':info['user_level'],
                'id':id
            }
            self.db.query_db(update_user_query, update_user_info)
            # return {'status':False, 'errorDictionary':dictionary_errors}
            return{'status':True}
        elif errorCount<=0 and len(emails)<=0 and info['password'] == '':
            #name and new email update with no password
            print 'name, email, password update'
            if len(info['email']) < 1:
                dictionary_errors['emailError']+='Email cannot be blank\n'
                errorCount+=1
            if not emailRegrex.match(info['email']):
                dictionary_errors['emailError']+='Email format must be valid!\n'
                errorCount+=1

            query = "SELECT * FROM users where email = :email and id != :id"
            data = {
                'email': info['email'],
                'id': id
            }
            emails_other = self.db.query_db(query,data)


            if len(emails_other)>0:
                dictionary_errors['emailError']+='Email already taken!\n'
                errorCount+=1




            if errorCount >0:
                return {'status':False, 'errorDictionary':dictionary_errors}
            else:
                update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, email=:email, user_level = :user_level, updated_at = NOW() where id = :id'
                update_user_info = {
                    'first_name': info['first_name'],
                    'last_name': info['last_name'],
                    'email': info['email'],
                    'user_level':info['user_level'],
                    'id':id
                }
                self.db.query_db(update_user_query, update_user_info)
                return{'status':True}
        elif errorCount<=0 and len(emails)>0 and (info['password'] != ''):
            #names update, user level and password
            #name is valid, email is the same as the previous, and with password update
            print 'name update, no email update and password update'
            if len(info['password']) < 1:
                dictionary_errors['passwordError']+='Password cannot be blank\n'
                errorCount+=1
            if len(info['confirm_password']) < 1:
                dictionary_errors['passwordError']+='Confirm cannot be blank\n'
                errorCount+=1
            if str(info['confirm_password']) != str(info['password']):
                dictionary_errors['passwordError']+='Password does not match\n'
                errorCount+=1
            if len(info['password']) <= 8:
                dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
                errorCount+=1

            if errorCount >0:
                return {'status':False, 'errorDictionary':dictionary_errors}
            else:
                hashed_pw = self.bcrypt.generate_password_hash(info['password'])
                update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, password = :password, user_level = :user_level, updated_at = NOW() where id = :id'
                update_user_info = {
                    'first_name': info['first_name'],
                    'last_name': info['last_name'],
                    'password': hashed_pw,
                    'user_level':info['user_level'],
                    'id':id
                }
                self.db.query_db(update_user_query, update_user_info)
                return{'status':True}
        
        elif errorCount<=0 and len(emails)<=0 and (info['password'] != ''):
            #name and new email update with password
            print 'name update, email, userlevel update, password update'
            if len(info['email']) < 1:
                dictionary_errors['emailError']+='Email cannot be blank\n'
                errorCount+=1
            if not emailRegrex.match(info['email']):
                dictionary_errors['emailError']+='Email format must be valid!\n'
                errorCount+=1
            #select email from other users to see if they have the email this current user want
            query = "SELECT * FROM users where email = :email and id != :id"
            data = {
                'email': info['email'],
                'id': id
            }
            emails_other = self.db.query_db(query,data)
            if len(emails_other) > 0:
                dictionary_errors['emailError']+='Already taken\n'
                errorCount+=1
            if len(info['password']) < 1:
                dictionary_errors['passwordError']+='Password cannot be blank\n'
                errorCount+=1
            if len(info['confirm_password']) < 1:
                dictionary_errors['passwordError']+='Confirm cannot be blank\n'
                errorCount+=1
            if str(info['confirm_password']) != str(info['password']):
                dictionary_errors['passwordError']+='Password does not match\n'
                errorCount+=1
            if len(info['password']) <= 8:
                dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
                errorCount+=1
            if PW_REGEX.match(info['password']) == None:
                dictionary_errors['passwordError']+='Password must have atleast 1 upper case, 1 lower case and 1 number!\n'
                errorCount+=1


            if errorCount >0:
                return {'status':False, 'errorDictionary':dictionary_errors}
            else:
                hashed_pw = self.bcrypt.generate_password_hash(info['password'])
                update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, email=:email, user_level = :user_level, password = :password, updated_at = NOW() where id = :id'
                update_user_info = {
                    'first_name': info['first_name'],
                    'last_name': info['last_name'],
                    'email': info['email'],
                    'password': hashed_pw,
                    'user_level':info['user_level'],
                    'id':id
                }
                self.db.query_db(update_user_query, update_user_info)
                return{'status':True}
        else:
            print 'this is else?'
            return{'sataus':True}
    def adminremove(self,id):
        delete_user_query = 'DELETE from users where id = :id'
        delete_user_data = {
            'id':id
        }
        self.db.query_db(delete_user_querdescriptiony, delete_user_data)
        return {'status':True}

    def userupdate(self,id,info):
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print 'admin update'
        print info
        
        print 'a;lsdkfjas;dlkfjas;dlfkjas;dlfkjasd'
        emailRegrex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

        PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

        dictionary_errors = {
            'emailError':'',
            'firstNameError':'',
            'lastNameError':'',
            'passwordError':''
        }
        errorCount=0
        
        
        if len(info['first_name']) < 1:
            dictionary_errors['firstNameError']+='First name cannot be blank\n'
            errorCount+=1
        if len(info['last_name']) < 1:
            dictionary_errors['lastNameError']+='Last name cannot be blank\n'
            errorCount+=1
        if str(info['first_name']).isalpha() == False:
            dictionary_errors['firstNameError']+='First name must only contain letters\n'
            errorCount+=1
        if str(info['last_name']).isalpha() == False:
            dictionary_errors['lastNameError']+='Last name must only contain letters\n'
            errorCount+=1


        query = "SELECT * FROM users where email = :email and id = :id"
        data = {
            'email': info['email'],
            'id': id
        }
        emails = self.db.query_db(query,data)

        print 'emails'
        print 'emails'
        print 'emails'
        print 'emails'
        print 'emails'
        print emails
        print info
        if info['password'] == '':
            print 'password is noneee?'
        else:
            print 'kabiguan'


        if len(emails)>0:
            print 'eail? is noneee?'
        else:
            print 'kabiguan'

        if errorCount<=0 and len(emails)>0 and (info['password'] == ''):
            #names update
            #name is valid, email is the same as the previous, and no password update
            update_user_query = 'UPDATE users where id = :id set first_name = :first_name, last_name = :last_name, user_level = :user_level, updated_at = NOW()'

            print 'name update'
            update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, description = :description, updated_at = NOW() where id = :id'
            update_user_info = {
                'first_name': info['first_name'],
                'last_name': info['last_name'],
                'description':info['description'],
                'id':id
            }
            self.db.query_db(update_user_query, update_user_info)
            # return {'status':False, 'errorDictionary':dictionary_errors}
            return{'status':True}
        elif errorCount<=0 and len(emails)<=0 and info['password'] == '':
            #name and new email update with no password
            print 'name, email, password update'
            if len(info['email']) < 1:
                dictionary_errors['emailError']+='Email cannot be blank\n'
                errorCount+=1
            if not emailRegrex.match(info['email']):
                dictionary_errors['emailError']+='Email format must be valid!\n'
                errorCount+=1

            query = "SELECT * FROM users where email = :email and id != :id"
            data = {
                'email': info['email'],
                'id': id
            }
            emails_other = self.db.query_db(query,data)


            if len(emails_other)>0:
                dictionary_errors['emailError']+='Email already taken!\n'
                errorCount+=1




            if errorCount >0:
                return {'status':False, 'errorDictionary':dictionary_errors}
            else:
                update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, email=:email, description = :description, updated_at = NOW() where id = :id'
                update_user_info = {
                    'first_name': info['first_name'],
                    'last_name': info['last_name'],
                    'email': info['email'],
                    'description':info['description'],
                    'id':id
                }
                self.db.query_db(update_user_query, update_user_info)
                return{'status':True}
        elif errorCount<=0 and len(emails)>0 and (info['password'] != ''):
            #names update, user level and password
            #name is valid, email is the same as the previous, and with password update
            print 'name update, no email update and password update'
            if len(info['password']) < 1:
                dictionary_errors['passwordError']+='Password cannot be blank\n'
                errorCount+=1
            if len(info['confirm_password']) < 1:
                dictionary_errors['passwordError']+='Confirm cannot be blank\n'
                errorCount+=1
            if str(info['confirm_password']) != str(info['password']):
                dictionary_errors['passwordError']+='Password does not match\n'
                errorCount+=1
            if len(info['password']) <= 8:
                dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
                errorCount+=1

            if errorCount >0:
                return {'status':False, 'errorDictionary':dictionary_errors}
            else:
                hashed_pw = self.bcrypt.generate_password_hash(info['password'])
                update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, password = :password, description = :description, updated_at = NOW() where id = :id'
                update_user_info = {
                    'first_name': info['first_name'],
                    'last_name': info['last_name'],
                    'password': hashed_pw,
                    'description':info['description'],
                    'id':id
                }
                self.db.query_db(update_user_query, update_user_info)
                return{'status':True}
        
        elif errorCount<=0 and len(emails)<=0 and (info['password'] != ''):
            #name and new email update with password
            print 'name update, email, userlevel update, password update'
            if len(info['email']) < 1:
                dictionary_errors['emailError']+='Email cannot be blank\n'
                errorCount+=1
            if not emailRegrex.match(info['email']):
                dictionary_errors['emailError']+='Email format must be valid!\n'
                errorCount+=1
            #select email from other users to see if they have the email this current user want
            query = "SELECT * FROM users where email = :email and id != :id"
            data = {
                'email': info['email'],
                'id': id
            }
            emails_other = self.db.query_db(query,data)
            if len(emails_other) > 0:
                dictionary_errors['emailError']+='Already taken\n'
                errorCount+=1
            if len(info['password']) < 1:
                dictionary_errors['passwordError']+='Password cannot be blank\n'
                errorCount+=1
            if len(info['confirm_password']) < 1:
                dictionary_errors['passwordError']+='Confirm cannot be blank\n'
                errorCount+=1
            if str(info['confirm_password']) != str(info['password']):
                dictionary_errors['passwordError']+='Password does not match\n'
                errorCount+=1
            if len(info['password']) <= 8:
                dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
                errorCount+=1
            if PW_REGEX.match(info['password']) == None:
                dictionary_errors['passwordError']+='Password must have atleast 1 upper case, 1 lower case and 1 number!\n'
                errorCount+=1


            if errorCount >0:
                return {'status':False, 'errorDictionary':dictionary_errors}
            else:
                hashed_pw = self.bcrypt.generate_password_hash(info['password'])
                update_user_query = 'UPDATE users set first_name = :first_name, last_name = :last_name, email=:email, description = :description, password = :password, updated_at = NOW() where id = :id'
                update_user_info = {
                    'first_name': info['first_name'],
                    'last_name': info['last_name'],
                    'email': info['email'],
                    'password': hashed_pw,
                    'description':info['description'],
                    'id':id
                }
                self.db.query_db(update_user_query, update_user_info)
                return{'status':True}
        else:
            print 'this is else?'
            return{'sataus':True}
    