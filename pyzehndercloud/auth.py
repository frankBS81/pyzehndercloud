import logging
from abc import ABC, abstractmethod

from aiohttp import ClientSession

OAUTH2_AUTHORIZE_URL = "https://zehndergroupauth.b2clogin.com/zehndergroupauth.onmicrosoft.com/b2c_1_signin_developerportal/oauth2/v2.0/authorize"
OAUTH2_TOKEN_URL = "https://zehndergroupauth.b2clogin.com/zehndergroupauth.onmicrosoft.com/B2C_1_signin_developerportal/oauth2/v2.0/token"

# OAUTH2_REDIRECT_URL = "http://localhost:5000"
OAUTH2_REDIRECT_URL = "https://my.home-assistant.io/oauth/redirect"

# OAUTH2_CLIENT_ID = 'df77b1ce-c368-4f7f-b0e6-c1406ac6bac9' # Documentation
OAUTH2_CLIENT_ID = "76c86940-8437-4819-9449-8b7e2a372a07"  # Home Assistant


class AuthError(Exception):
    """Authentication has failed."""


class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(self, websession: ClientSession):
        """Initialize the auth."""
        self.websession = websession

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
