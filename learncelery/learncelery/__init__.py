from __future__ import absolute_import
from .celery import app as celery_app

# 保证celery app总能在django应用启动时启动
__all__ = ['celery_app']