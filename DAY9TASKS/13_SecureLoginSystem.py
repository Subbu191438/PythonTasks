def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func(is_logged_in)
        else:
            print("Access Denied. Please login first.")
    return wrapper
@login_required
def view_dashboard(is_logged_in):
    print("Welcome to your dashboard!")
view_dashboard(True)   
view_dashboard(False)  
