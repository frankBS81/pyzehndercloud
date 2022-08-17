import logging
from abc import ABC, abstractmethod

from aiohttp import ClientSession

_LOGGER = logging.getLogger(__name__)

#OAUTH2_CLIENT_ID = 'df77b1ce-c368-4f7f-b0e6-c1406ac6bac9' # Documentation
OAUTH2_CLIENT_ID = '76c86940-8437-4819-9449-8b7e2a372a07' # Home Assistant

class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(self, websession: ClientSession):
        """Initialize the auth."""
        self.websession = websession

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
