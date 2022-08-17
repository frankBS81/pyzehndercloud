import json
import logging
import urllib.parse
import msal

from pyzehndercloud import OAUTH2_CLIENT_ID

AUTHORITY = "https://{tenant}.b2clogin.com/{tenant}.onmicrosoft.com/{user_flow}".format(
    tenant="zehndergroupauth",
    #user_flow="b2c_1_signin_signup_enduser"
    user_flow="b2c_1_signin_developerportal"
)
#REDIRECT_PATH = "https://localhost:5000/"
REDIRECT_PATH = "https://my.home-assistant.io/redirect/oauth"

SCOPE = []

_LOGGER = logging.getLogger(__name__)



def run():
    # Create the msal app
    msal_app = msal.ConfidentialClientApplication(
        client_id=OAUTH2_CLIENT_ID,
        client_credential='',
        authority=AUTHORITY,
    )

    # Initiate the auth flow
    flow = msal_app.initiate_auth_code_flow(
        scopes=SCOPE,
        redirect_uri=REDIRECT_PATH
    )
    print("Navigate to the following URL in a browser:")
    print(flow["auth_uri"])
    print()

    # Parse the reply
    print('Enter the URL you were redirected to:')
    url = input()
    query_params = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(url).query))
    result = msal_app.acquire_token_by_auth_code_flow(flow, query_params)
    print()

    if result.get("error"):
        print("Error {}:\n{}".format(result.get("error"), result.get("error_description")))
        exit(1)

    # Store the result in a file for later use
    with open('.auth_token.json', 'w') as f:
        f.write(json.dumps(result))

    print("Token acquired. You can now use the token in the auth header of your requests.")


if __name__ == "__main__":
    run()
