from celery import Celery

parser = Celery('tasks',
                broker='redis://localhost:6379/0',
                include=['parser.tasks'])
