class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

#Method 1
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("Not logged in!")
    return wrapper

#Method 2
def is_authenticated_decorator_2(function):
    def wrapper(user):
        if user.is_logged_in:
            function(user)
        else:
            print("Not logged in!")
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Lucas")
create_blog_post(new_user)
new_user.is_logged_in = True
create_blog_post(new_user)
