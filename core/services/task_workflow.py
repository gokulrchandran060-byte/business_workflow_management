import logging
from django.utils import timezone
from core.models import Task

logger = logging.getLogger(__name__)


class InvalidStatusTransition(Exception):
    pass


ALLOWED_TRANSITIONS = {
    Task.STATUS_CREATED: [Task.STATUS_IN_PROGRESS],
    Task.STATUS_IN_PROGRESS: [Task.STATUS_DONE],
    Task.STATUS_DONE: [],
}


def change_task_status(task: Task, new_status: str) -> Task:
    current_status = task.status

    logger.info(
        f"Attempting status change: task_id={task.id}, "
        f"{current_status} -> {new_status}"
    )

    if new_status not in ALLOWED_TRANSITIONS[current_status]:
        logger.warning(
            f"Invalid transition blocked: task_id={task.id}, "
            f"{current_status} -> {new_status}"
        )
        raise InvalidStatusTransition(
            f"Cannot change status from {current_status} to {new_status}"
        )

    # ORM-centric update (NO full object save)
    Task.objects.filter(id=task.id).update(
        status=new_status,
        updated_at=timezone.now()
    )

    logger.info(
        f"Status updated successfully: task_id={task.id}, "
        f"new_status={new_status}"
    )

    task.status = new_status
    return task
