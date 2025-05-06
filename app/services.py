from .repository import repository_create_user, repository_get_all_users


def service_get_all_useres():
    """
    Retrieves all users from the database using the repository.
    """
    return repository_get_all_users()



def service_create_user(data):
    """
    Creates a new user in the database using the repository with the given first name, last name, and email.
    Returns the created user object.
    """ 
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email', "")  # Email is optional

    if not first_name or not last_name:
        raise ValueError('First name and last name are required')
    
    return repository_create_user(first_name, last_name, email)
