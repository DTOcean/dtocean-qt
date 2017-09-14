# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Added

- Add change log.
- Added CI files
- Added win64 version of libmagic library.
- Added python-magic as a dependency.

### Fixed

- Fix incorrect use of Pandas ix method which read wrong table rows
- Fix reference to pandasqt in MANIFEST.in which caused crash.
- Fix various bugs with use of QVariant v2 API, which is not default for
  Python 2.
- Fix bugs with comparison of QStrings to Python strings.
- Fix incorrect format (python 3) for validator return value in remove column
  dialog of a DataTable widget.

## [0.9.0] - 2017-02-23

### Added

- Initial import of pandas-qt from SETIS.

### Changed

- Changed package name to dtocean-qt.

