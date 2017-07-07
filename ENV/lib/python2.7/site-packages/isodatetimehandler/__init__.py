import datetime

from jsonpickle.handlers import BaseHandler

import dateutil.parser


class IsoDatetimeHandler(BaseHandler):
    """
    This ``jsonpickle`` handler serializes ``datetime.datetime``
    objects as ISO-8601 formatted strings.  Such strings may be
    treated as a ``DATETIME`` type in a RDBMS such as SQLite
    allowing date-related query clauses to work with serialized
    datetime objects directly.
    """

    def flatten(self, obj, data):
        data['iso'] = obj.isoformat()
        return data

    def restore(self, data):
        return dateutil.parser.parse(data['iso'])


IsoDatetimeHandler.handles(datetime.datetime)
