"""
配置文件
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """应用配置"""

    SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY", "")
    SILICONFLOW_API_URL = os.getenv("SILICONFLOW_API_URL", "https://api.siliconflow.cn/v1/chat/completions")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "deepseek-ai/DeepSeek-V2.5")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


config = Config()