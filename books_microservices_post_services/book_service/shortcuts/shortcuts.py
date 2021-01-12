import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from sqlalchemy.orm import exc
from werkzeug.exceptions import abort


def get_object_or_404(model, *criterion):
    try:
        rv = model.query.filter(*criterion).one()
    except exc.NoResultFound, exc.MultipleResultsFound:
        abort(404)
    else:
        return rv