"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Sessions'
# render the sign in and sign up page
routes['/signin'] = 'Sessions#signin'
routes['/signup'] = 'Sessions#signup'

# sign up function
routes['POST']['/register'] = 'Sessions#register'
#sign in function
routes['POST']['/login'] = 'Sessions#login'

# sign out
routes['/logoff'] = 'Sessions#logoff'

#dashbaord

routes['/dashboard/admin'] = 'Users#dashboardadmin'

routes['/dashboard'] = 'Users#dashboard'

#user/dashboard?

routes['/users/edit/<id>'] = 'Users#edit'
routes['/users/new'] = 'Users#new'
routes['/users/show/<id>'] = 'Users#show'
routes['/users/edit/<id>'] = 'Users#adminedit'
routes['/users/edit'] = 'Users#useredit'
routes['/users/confirmremove/<id>'] = 'Users#adminconfirmremove'
routes['POST']['/users/update/<id>'] = 'Users#adminupdate'
routes['POST']['/users/update'] = 'Users#userupdate'
routes['POST']['/users/remove/<id>'] = 'Users#remove'

#<id> is for the person you are posting to
routes['POST']['/users/message/<id>'] = 'Users#message'
routes['POST']['/users/comment/<id>'] = 'Users#comment'

#Messages



"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
