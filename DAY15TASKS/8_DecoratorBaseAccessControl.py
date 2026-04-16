users = {
    "admin_user": "admin",
    "normal_user": "user"
}
def require_role(role):
    def decorator(func):
        def wrapper(username, *args, **kwargs):
            if users.get(username) == role:  
                return func(username, *args, **kwargs)
            else:
                print("Access Denied!")
        return wrapper
    return decorator
@require_role("admin")
def delete_data(username):
    print(f"{username} deleted data")

@require_role("user")
def view_data(username):
    print(f"{username} viewed data")
delete_data("admin_user")   
delete_data("normal_user")  

view_data("normal_user")    
view_data("admin_user")     
