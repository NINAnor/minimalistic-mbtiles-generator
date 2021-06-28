# Instruction for users

1. Download the asset named `minimalistic_mbtiles_generator.zip` from the [latest release](https://github.com/NINAnor/minimalistic-mbtiles-generator/releases) page
2. Install the plugin in QGIS using the function named `Install from ZIP`

# Instructions for developers

```bash
git clone https://github.com/NINAnor/minimalistic-mbtiles-generator.git
cd minimalistic-mbtiles-generator/
export PYTHONPATH=/usr/share/qgis/python
pb_tool deploy -p $HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```
