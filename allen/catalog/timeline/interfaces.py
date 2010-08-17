from zope import schema
from zope.interface import Interface

class ITimeline(Interface):
    """ Timeline utility
    """
    def index(doc):
        """ Add doc intid to timeline
        """

    def unindex(doc):
        """ Delete doc intid from timeline
        """

    def reindex(doc):
        """ Reindex doc of all intids
        """
