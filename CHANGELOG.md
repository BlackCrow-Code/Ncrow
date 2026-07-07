# Changelog

## [4.0.0] - 2026-07-07
### Added
- JSON output support (`-oj`)
- Plain text output support (`-on`)
- Server header detection (`-s`) replacing old banner grabbing (`-b`)
- Thread-safe Queue for port distribution instead of static slicing
- Graceful KeyboardInterrupt handling (Ctrl+C)
- Hostname/URL parsing via `urlparse` (supports full URLs as targets)

### Changed
- Thread cap enforced at 300 for stability
- Improved DNS error handling

### Fixed
- Service name resolution fallback for unknown ports
