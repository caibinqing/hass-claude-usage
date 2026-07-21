"""Constants for Claude Usage integration."""

DOMAIN = "hass_claude_usage"

# OAuth
OAUTH_CLIENT_ID = "9d1c250a-e61b-44d9-88ed-5944d1962f5e"
OAUTH_AUTHORIZE_URL = "https://claude.ai/oauth/authorize"
OAUTH_TOKEN_URL = "https://console.anthropic.com/v1/oauth/token"
OAUTH_REDIRECT_URI = "https://console.anthropic.com/oauth/code/callback"
OAUTH_SCOPES = "org:create_api_key user:profile user:inference"

# API
USAGE_API_URL = "https://api.anthropic.com/api/oauth/usage"
PROFILE_API_URL = "https://api.anthropic.com/api/oauth/profile"
API_BETA_HEADER = "oauth-2025-04-20"

# Defaults
DEFAULT_UPDATE_INTERVAL = 300  # seconds

# The rolling 5-hour window's `resets_at` drifts by a few seconds on every poll,
# so a timestamp sensor flips its displayed minute back and forth and floods the
# recorder/history with noise. A real reset always jumps by hours (or days), so we
# keep the previously reported value whenever the new one lands within this many
# seconds of it. Comfortably above the observed drift, well below any real reset.
RESET_TIME_JITTER_SECONDS = 300

# Flat timestamp keys subject to that jitter suppression; the resets_at inside
# each limits[] bucket is stabilized separately in _stabilize_reset_times.
RESET_TIME_KEYS = ("session_reset_time", "week_reset_time", "week_sonnet_reset_time")

# Config keys
CONF_ACCESS_TOKEN = "access_token"
CONF_REFRESH_TOKEN = "refresh_token"
CONF_EXPIRES_AT = "expires_at"
CONF_UPDATE_INTERVAL = "update_interval"
CONF_ACCOUNT_ID = "account_id"
CONF_ACCOUNT_NAME = "account_name"
CONF_ACCOUNT_EMAIL = "account_email"
CONF_SUBSCRIPTION_LEVEL = "subscription_level"
# Optional outbound proxy (http://host:port) for every Anthropic request, for
# networks where Home Assistant has no direct egress. Stored in the entry options;
# also collected on the setup form so it is available for the first OAuth exchange.
CONF_PROXY_URL = "proxy_url"

# Sensor definitions: (key, name, unit, icon, device_class)
# key corresponds to a path in the parsed usage data dict
SENSOR_DEFINITIONS = [
    ("session_usage_percent", "Session Usage", "%", "mdi:timer-sand", None),
    (
        "session_reset_time",
        "Session Reset Time",
        None,
        "mdi:timer-refresh",
        "timestamp",
    ),
    ("week_usage_percent", "Week Usage", "%", "mdi:calendar-week", None),
    ("week_usage_pace", "Week Usage Pace", "%", "mdi:speedometer", None),
    ("week_reset_time", "Weekly Reset Time", None, "mdi:calendar-clock", "timestamp"),
    (
        "week_sonnet_usage_percent",
        "Weekly Sonnet Usage",
        "%",
        "mdi:calendar-week",
        None,
    ),
    (
        "week_sonnet_reset_time",
        "Weekly Sonnet Reset Time",
        None,
        "mdi:calendar-clock",
        "timestamp",
    ),
    ("extra_usage_enabled", "Extra Usage Enabled", None, "mdi:toggle-switch", None),
    ("extra_usage_percent", "Extra Usage", "%", "mdi:credit-card", None),
    (
        "extra_usage_credits",
        "Extra Usage Credits",
        "credits",
        "mdi:credit-card-outline",
        None,
    ),
    (
        "extra_usage_limit",
        "Extra Usage Limit",
        "credits",
        "mdi:credit-card-settings",
        None,
    ),
    ("api_error", "API Error", "errors", "mdi:alert-circle", None),
]

# limits[] bucket keys whose meter is already exposed by a static sensor above
# (fed from the dedicated five_hour / seven_day / seven_day_sonnet objects).
# No dynamic bucket sensor is created while the mapped data key has a value.
STATIC_LIMIT_EQUIVALENTS = {
    "session": "session_usage_percent",
    "weekly_all": "week_usage_percent",
    "weekly_scoped_sonnet": "week_sonnet_usage_percent",
}
