import json
import logging


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name
        }

        if hasattr(record, "event"):
            log_data["event"] = record.event

        if hasattr(record, "pais"):
            log_data["pais"] = record.pais

        if hasattr(record, "error_type"):
            log_data["error_type"] = record.error_type

        return json.dumps(log_data, ensure_ascii=False)
