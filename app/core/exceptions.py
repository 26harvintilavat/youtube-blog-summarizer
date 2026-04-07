class AppError(Exception):
    """Base application error."""
    pass

class InvalidURLError(AppError):
    """Raised when the provided URL is invalid or unsupported."""
    pass

class ContentLoadError(AppError):
    """Raised when content could not be loaded from a source."""
    pass

class SummarizationError(AppError):
    """Raised when summarization fails."""
    pass
