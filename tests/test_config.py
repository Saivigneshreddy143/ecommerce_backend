import pytest
from pydantic import ValidationError

from ecommerce_backend.core.config import Settings, get_settings

ENV_KEYS = ("APP_NAME", "APP_VERSION", "APP_ENV", "DEBUG", "API_V1_PREFIX")


def test_settings_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    """Settings should use defaults regardless of existing environment variables."""
    for key in ENV_KEYS:
        monkeypatch.delenv(key, raising=False)

    cfg = Settings(_env_file=None)

    assert cfg.app_name == "Ecommerce Backend API"
    assert cfg.app_version == "0.1.0"
    assert cfg.app_env == "development"
    assert cfg.debug is False
    assert cfg.api_v1_prefix == "/api/v1"


def test_settings_env_override(monkeypatch: pytest.MonkeyPatch) -> None:
    """Environment variables should override default Settings values."""
    monkeypatch.setenv("APP_NAME", "Marketplace Test API")
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("DEBUG", "true")
    monkeypatch.setenv("API_V1_PREFIX", "/api/v2")

    cfg = Settings(_env_file=None)

    assert cfg.app_name == "Marketplace Test API"
    assert cfg.app_version == "1.2.3"
    assert cfg.app_env == "production"
    assert cfg.debug is True
    assert cfg.api_v1_prefix == "/api/v2"


@pytest.mark.parametrize("env_value", ["development", "staging", "production"])
def test_settings_supported_environments(
    monkeypatch: pytest.MonkeyPatch,
    env_value: str,
) -> None:
    """All supported APP_ENV values should be accepted."""
    monkeypatch.setenv("APP_ENV", env_value)

    cfg = Settings(_env_file=None)

    assert cfg.app_env == env_value


def test_settings_invalid_environment_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    """An unsupported APP_ENV value should fail validation."""
    monkeypatch.setenv("APP_ENV", "invalid_env")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_get_settings_is_cached(monkeypatch: pytest.MonkeyPatch) -> None:
    """get_settings should return a cached instance and isolate cache state."""
    for key in ENV_KEYS:
        monkeypatch.delenv(key, raising=False)

    get_settings.cache_clear()
    try:
        first = get_settings()
        second = get_settings()
        assert first is second
    finally:
        get_settings.cache_clear()