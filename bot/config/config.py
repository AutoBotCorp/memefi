from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    MIN_AVAILABLE_ENERGY: int = 300
    SLEEP_BY_MIN_ENERGY: int = 300

    ADD_TAPS_ON_TURBO: list[int] = [1300, 2250]

    AUTO_BUY_TAPBOT: bool = True

    AUTO_UPGRADE_TAP: bool = False
    MAX_TAP_LEVEL: int = 5
    AUTO_UPGRADE_ENERGY: bool = False
    MAX_ENERGY_LEVEL: int = 5
    AUTO_UPGRADE_CHARGE: bool = False
    MAX_CHARGE_LEVEL: int = 5

    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_TURBO: bool = True

    RANDOM_TAPS_COUNT: list[int] = [20, 30]
    SLEEP_BETWEEN_TAP: list[int] = [10, 15]

    #AUTO_GENERATE_USER_AGENT_FOR_EACH_SESSION: bool = True

    ENABLE_PROXY: bool = True
    
    REF: bool = True

    EMERGENCY_STOP: bool = False


settings = Settings()
