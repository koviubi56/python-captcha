# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.3] - 2021-03-27
### Fixed
- Fixed the `Unnecessary "else" after "return"` and the `Unnecessary "elif" after "return"` issues.
- Fixed the `Comparison 'day() == True' should be 'day() is True' if checking for the singleton value True` issue.

## [1.4.2] - 2021-03-25
### Fixed
- Fixed the #9 issue

## [1.4.1] - 2021-03-24
### Changed
- Changed the all function (https://tknk.io/kWFf)
### Fixed
- Fixed a bug in animal captcha (https://tknk.io/uNhI)

## [1.4.0] - 2021-03-23
### Fixed
- Fixed an issue in the animal captcha.

## [1.3.1] - 2021-03-12
### Added
- New words
- New questions
### Fixed
- A "bug" at the biggest captcha

## [1.3.0] - 2021-02-03
### Added
- Daycaptcha
### Fixed
- The digit captcha

## [1.2.0] - 2021-01-30
### Added
- Color captcha
- New question to digit captcha (What is the ~th digit in ~>)
- New question to biggest captcha (Enter the ~ number of ~ and ~ >)

## [1.1.0] - 2021-01-24
### Added
- Digit captcha
- Biggest captcha
- Smallest captcha
- Name captcha
- There is now a way to run every captcha (`captcha.all(mathnummax)`)
### Changed
- Lastword now has more question types
- Math now has more plus types.
### Removed
- Captcha class
### Fixed
- If you need to enter a number, and you enter a string, now the program send you an error messsage.

## [1.0.0] - 2021-01-23
