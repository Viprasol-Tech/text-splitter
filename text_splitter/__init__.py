"""
text-splitter - Split text intelligently by chunks, sentences, or paragraphs

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import TextSplitter, split, process, main

__all__ = ["TextSplitter", "split", "process", "main"]
