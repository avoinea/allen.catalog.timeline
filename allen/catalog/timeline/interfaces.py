from zope import schema
from zope.interface import Interface

class ITimeline(Interface):
    """ Timeline utility
    """
    maxitems = schema.Int(title=u'Max items', default=5000)
    datefield = schema.TextLine(title=u'Date field', default=u'updated')

    def index(doc):
        """ Add doc intid to timeline
        """

    def unindex(doc):
        """ Delete doc intid from timeline
        """

    def reindex(doc):
        """ Reindex doc of all intids
        """

    def __len__():
        """ Timeline length
        """
