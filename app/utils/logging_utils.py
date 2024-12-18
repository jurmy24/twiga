import logging
import httpx

logger = logging.getLogger(__name__)


def log_httpx_response(response: httpx.Response) -> None:
    # ANSI escape code mapping
    ANSI_COLOR_CODES = {
        "green": "32",
        "cyan": "36",
        "yellow": "33",
        "red": "31",
        "reset": "0",
        "magenta": "35",
    }

    # Extracting necessary details from the response
    url = response.url
    status_code = response.status_code
    body = response.text

    # Color formatting based on the status code
    if 200 <= status_code < 300:
        status_color = ANSI_COLOR_CODES["green"]
        log_method = logger.debug
    elif 300 <= status_code < 400:
        status_color = ANSI_COLOR_CODES["cyan"]
        log_method = logger.info
    elif 400 <= status_code < 500:
        status_color = ANSI_COLOR_CODES["yellow"]
        log_method = logger.warning
    else:
        status_color = ANSI_COLOR_CODES["red"]
        log_method = logger.error
    from app.config import settings

    if log_method != logger.info:
        log_method(f"Current app ID: {settings.meta_app_id}")
        log_method(f"Current api version: {settings.meta_api_version}")
        log_method(f"Current cloud number ID: {settings.whatsapp_cloud_number_id}")
        log_method(
            f"Current whatsapp api token: {settings.whatsapp_api_token.get_secret_value()}"
        )
        log_method(f"Current app secret: {settings.meta_app_secret.get_secret_value()}")
    log_method(f"Response URL: {url}")
    log_method(f"Response Status: \033[{status_color}m{status_code}\033[0m")
    log_method(f"Response Body: \033[35m{body}\033[0m")
