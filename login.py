import os

import instaloader


def login_to_instagram(username, password, session_file='my_session'):
    """
    Logs into Instagram using the provided username and password. 
    If a session file exists, it loads the session. Otherwise, it logs in and saves the session.

    Parameters:
    - username: Instagram username
    - password: Instagram password
    - session_file: The session file name to save/load the session (default is 'my_session')
    """
    # Delete the session file if it exists
    if os.path.exists(session_file):
        os.remove(session_file)
        print(f"{session_file} has been deleted successfully.")
    
    L = instaloader.Instaloader()

    # Load the session if it exists
    if os.path.exists(session_file):
        L.load_session_from_file(username, session_file)

    if not L.context.is_logged_in:
        try:
            L.login(username, password)
            L.save_session_to_file(session_file)
            print("Login successful and session saved.")
        except instaloader.exceptions.BadCredentialsException:
            print("Login error: Wrong username or password.")
        except instaloader.exceptions.ConnectionException as e:
            print(f"Connection error: {e}")
        except Exception as e:
            print(f"An error occurred during login: {e}")
    else:
        print("Already logged in.")

login_to_instagram('sahminvests', 'dumju1-cyjvyb-gybJin')
 