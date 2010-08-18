import logging
from persistent.list import PersistentList

from zope.interface import implements
from zope.component import getUtility
from persistent import Persistent
from zope.app.container.contained import Contained
from zope.intid.interfaces import IIntIds

from interfaces import ITimeline

logger = logging.getLogger('allen.catalog.timeline')

class Timeline(Persistent, Contained):
    """ Timeline utility
    """
    _timeline = ()
    maxitems = 5000
    datefield = u'updated'
    implements(ITimeline)

    def __init__(self, *args):
        self._timeline = PersistentList([])
        super(Timeline, self).__init__(*args)

    @property
    def timeline(self):
        return self._timeline

    def index(self, doc):
        util = getUtility(IIntIds)
        intid = util.queryId(doc)
        if not intid:
            logger.warn('No intid found for %s', doc)
            return

        for index, name in enumerate(self.timeline):
            if name == intid:
                logger.warn('Intid %s already in timeline', intid)
                return

            brain = util.queryObject(name, None)
            if not brain:
                continue

            doc_date = getattr(doc, self.datefield, None)
            brain_date = getattr(brain, self.datefield, None)

            try:
                if doc_date >= brain_date:
                    self._timeline.insert(index, intid)
                    if len(self._timeline) > self.maxitems:
                        self._timeline.pop()
                    return
            except Exception, err:
                logger.exception(err)
                return

        # Add it at the end of timeline
        if len(self._timeline) < self.maxitems:
            self._timeline.append(intid)

    def unindex(self, doc):
        util = getUtility(IIntIds)
        intid = util.queryId(doc)
        if intid in self._timeline:
            self._timeline.remove(intid)

    def reindex(self, doc=None):
        if doc:
            # Notingh to do
            return

        # Reindex everything
        self._timeline = PersistentList([])
        util = getUtility(IIntIds)
        for intid in util:
            doc = util.queryObject(intid)
            if not doc:
                continue
            self.index(doc)

    def __iter__(self):
        util = getUtility(IIntIds)
        for intid in self._timeline:
            doc = util.queryObject(intid, None)
            if not doc:
                continue
            yield doc

    def __len__(self):
        return len(self._timeline)
