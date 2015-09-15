import tkinter 
from collections import defaultdict
from scrolled_text import ScrolledText
from sources_table import SourcesTable
from icon_path import icon_path
from tooltip import Tooltip

class SimilarSourcesView():
    """Provides a view for sources that match the selected hash.

    Attributes:
      frame(Frame): the containing frame for this view.
    """

    def __init__(self, master, identified_data, filters, offset_selection):
        """Args:
          master(a UI container): Parent.
          identified_data(IdentifiedData): All data related to the block
            hash scan.
          filters(Filters): The filters that controll the view.
        """
        # variables
        self._identified_data = identified_data
        self._offset_selection = offset_selection

        # make the containing frame
        self.frame = tkinter.Frame(master)

        # the title
        tkinter.Label(self.frame, text='Similar Matched Sources') \
                                            .pack(side=tkinter.TOP)

        # the sources table
        self._sources_table = SourcesTable(self.frame, identified_data, filters,
                                                        height=16, width=88)
        self._sources_table.frame.pack(side=tkinter.TOP, anchor="w")

        # register to receive offset selection events
        offset_selection.set_callback(self._handle_offset_selection)

    def _handle_offset_selection(self, *args):
        # get the selected hash
        if self._offset_selection.offset == -1 or \
                          self._offset_selection.block_hash not in \
                                     self._identified_data.hashes:

            # no selection
            self._sources_table.set_data(set())

        else:
            # select sources associated with this block hash
            block_hash = self._offset_selection.block_hash

            # get the source IDs associated with the selected hash
            sources = self._identified_data.hashes[block_hash]
            source_id_set = set()
            for source in sources:
                # add source_id to set
                source_id_set.add(source["source_id"])

            # set the table based on the source IDs
            self._sources_table.set_data(source_id_set)
