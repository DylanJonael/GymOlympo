import os
from functools import lru_cache
from urllib.parse import quote_plus

import pyodbc
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Gym Olympo API"
    sqlserver_host: str = Field(default=os.getenv("IP_SERVIDOR", ""), alias="IP_SERVIDOR")
    sqlserver_password: str = Field(default=os.getenv("SA_PASSW", ""), alias="SA_PASSW")
    sqlserver_user: str = "sa"
    sqlserver_database: str = "GimnasioDB"
    cors_origins: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]

    model_config = SettingsConfigDict(populate_by_name=True, extra="ignore")

    @property
    def preferred_driver(self) -> str:
        candidates = [
            "ODBC Driver 18 for SQL Server",
            "ODBC Driver 17 for SQL Server",
            "SQL Server Native Client 11.0",
            "SQL Server",
        ]
        installed = set(pyodbc.drivers())
        for driver in candidates:
            if driver in installed:
                return driver
        return candidates[0]

    @property
    def database_url(self) -> str:
        if not self.sqlserver_host:
            raise ValueError("Falta la variable de entorno IP_SERVIDOR.")
        if not self.sqlserver_password:
            raise ValueError("Falta la variable de entorno SA_PASSW.")
        driver = quote_plus(self.preferred_driver)
        password = quote_plus(self.sqlserver_password)
        return (
            f"mssql+pyodbc://{self.sqlserver_user}:{password}@{self.sqlserver_host}/"
            f"{self.sqlserver_database}?driver={driver}&TrustServerCertificate=yes&Encrypt=no"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
