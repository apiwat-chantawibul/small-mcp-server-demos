import requests
from fastmcp import FastMCP
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix = 'SEARCH_API_',
    )

    key: str = Field(
        description = 'API key for www.searchapi.io',
    )


settings = Settings()
mcp = FastMCP(name = 'search-api')


@mcp.tool
async def search_google_scholar(query: str) -> dict:
    url = 'https://www.searchapi.io/api/v1/search'
    params = {
      'engine': 'google_scholar',
      'q': query,
      'api_key': settings.key,
    }
    response = requests.get(url, params = params)
    return response.json()


if __name__ == '__main__':
    mcp.run()

