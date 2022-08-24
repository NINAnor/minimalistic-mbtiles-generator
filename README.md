`mbtiles` files are useful to locally store base maps to be used for surveys when no internet connection is available. Sometimes, users are interested in more than one area, but generating a `mbtiles` which contains all of them can result in long processing time and large files.

This QGIS plugin address the issue by generating a single `mbtiles` file which only contains the tiles for the relevant areas, instead of downloading all the tiles within the overall bounding box.

# Instruction for users

1. Download the asset named `minimalistic_mbtiles_generator.zip` from the [latest release](https://github.com/NINAnor/minimalistic-mbtiles-generator/releases) page
2. Install the plugin in QGIS using the function named `Install from ZIP`
3. Open `Minimalistic MBTiles Generator` located inside `NINA` from the processing toolbox
4. Select the layer containing the polygon as input layer and the other parameters
5. Compute

# Instructions for developers

```bash
git clone https://github.com/NINAnor/minimalistic-mbtiles-generator.git
cd minimalistic-mbtiles-generator/
export PYTHONPATH=/usr/share/qgis/python
pb_tool deploy -p $HOME/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```
