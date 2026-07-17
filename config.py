from enum import Enum
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel, ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = "webkit"
    CHROMIUM = "chromium"
    FIREFOX = "firefox"


class TestUser(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
        case_sensitive=False
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath


Settings()

