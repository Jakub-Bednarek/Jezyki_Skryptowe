from task_request import TaskRequest
from logger import msg_logger, log_info

msg_logger.init_logger("test.log")

req = TaskRequest()
req.add_cmd("Set jascd in Asia ankmsc from December")
req.add_cmd("Exit")
req.add_cmd("Show")
req.add_cmd("Reset")

print(req.get_execution_sequence())

msg_logger.cleanup_logger()
