# Magisk Web API

A simple magisk web api written in [Python](https://www.python.org) using [FastAPI](https://fastapi.tiangolo.com) to get info of latest [Magisk Files](https://github.com/topjohnwu/Magisk).

## API URL

__Here__: <https://magiskapi.prajjus.site>

## Routes

- `magisk`
  
## Parameters

- `magisk_version_type ["stable", "beta", "canary"]`: To get info of specific magisk version.
- `all`: To get info of all magisk versions.

## Examples

- `{URL}/magisk/stable`

```json
{
  "type": "Stable",
  "version": "25.2",
  "download": "https://cdn.jsdelivr.net/gh/topjohnwu/magisk-files@25.2/app-release.apk",
  "changelog": "https://topjohnwu.github.io/Magisk/releases/25200.md"
}
```

- `{URL}/magisk/all`
  
```json
{
  "Stable": {
    "version": "25.2",
    "download": "https://cdn.jsdelivr.net/gh/topjohnwu/magisk-files@25.2/app-release.apk",
    "changelog": "https://topjohnwu.github.io/Magisk/releases/25200.md"
  },
  "Beta": {
    "version": "26.0",
    "download": "https://cdn.jsdelivr.net/gh/topjohnwu/magisk-files@26.0/app-release.apk",
    "changelog": "https://topjohnwu.github.io/Magisk/releases/26000.md"
  },
  "Canary": {
    "version": "e2545e57",
    "download": "https://cdn.jsdelivr.net/gh/topjohnwu/magisk-files@76a6e7a53b6509dc6c2ae2974a2ea2a8b07d3a12/app-release.apk",
    "changelog": "https://cdn.jsdelivr.net/gh/topjohnwu/magisk-files@76a6e7a53b6509dc6c2ae2974a2ea2a8b07d3a12/notes.md"
  }
}
```
