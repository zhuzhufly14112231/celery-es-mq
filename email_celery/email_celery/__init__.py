from __future__ import absolute_import
# 保证celery app总能在django应用启动时启动
from .celery import app

__all__ = ['app']









