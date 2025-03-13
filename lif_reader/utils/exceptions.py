class InvalidLIFFileError(Exception):
    """Raised when the LIF file is invalid or missing required fields."""
    pass

class NodeNotFoundError(Exception):
    """Raised when a node referenced in an edge or station is not found."""
    pass

class DuplicateNodeError(Exception):
    """Raised when a node with the same ID is added more than once."""
    pass

class DuplicateEdgeError(Exception):
    """Raised when an edge with the same ID is added more than once."""
    pass

class StationNotFoundError(Exception):
    """Raised when a station references a node that does not exist."""
    pass

class GraphError(Exception):
    """Generic error for issues related to graph construction or rendering."""
    pass