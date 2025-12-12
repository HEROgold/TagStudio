# Copyright (C) 2025
# Licensed under the GPL-3.0 License.
# Created for TagStudio: https://github.com/CyanVoxel/TagStudio

from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from tagstudio.core.library.alchemy.library import Library
from tagstudio.core.library.refresh import RefreshTracker

CWD = Path(__file__).parent


@pytest.mark.parametrize("exclude_mode", [True, False])
@pytest.mark.parametrize("library", [TemporaryDirectory()], indirect=True)
def test_refresh_new_files(library: Library, exclude_mode: bool):
    library_dir = library.library_dir
    # Given
    library.write_extension_filters(["md"], exclude_mode)
    registry = RefreshTracker(library=library)
    library.included_files.clear()
    (library_dir / "FOO.MD").touch()

    # Test if the single file was added
    list(registry.refresh_dir(library_dir, force_internal_tools=True))
    assert registry.files_not_in_library == [Path("FOO.MD")]
