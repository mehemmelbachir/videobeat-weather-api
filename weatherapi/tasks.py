from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .services import get_initial_data, calculate_output_data
from weather.settings import OUTPUT_INTERVAL

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="task_get_initial_data",
    ignore_result=True
)
def task_get_initial_data():
    """
    Get Input Data from API
    """
    get_initial_data()
    logger.info("Data loaded from API")


@periodic_task(
    run_every=(crontab(minute='*/{}'.format(OUTPUT_INTERVAL))),
    name="task_calculate_output_data",
    ignore_result=True
)
def task_calculate_output_data():
    """
    Calculate output data...
    """
    calculate_output_data()
    logger.info("Output data calculated successfully...")

