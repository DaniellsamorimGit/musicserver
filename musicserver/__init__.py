from mutagen._util import MutagenError
from mutagen._file import FileType, StreamInfo, File
from mutagen._tags import Tags, Metadata, PaddingInfo

version = (1, 45, 1)
"""Version tuple."""

version_string = ".".join(map(str, version))
"""Version string."""

MutagenError

FileType

StreamInfo

File

Tags

Metadata

PaddingInfo
