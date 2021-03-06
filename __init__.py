# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MinimalisticMBTilesGenerator
                                 A QGIS plugin
 Generate XYZ tiles (MBTiles) only around the features of a given vector layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-06-28
        copyright            : (C) 2021 by Francesco Frassinelli/Norsk institutt for naturforskning
        email                : francesco.frassinelli@nina.no
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Francesco Frassinelli/Norsk institutt for naturforskning'
__date__ = '2021-06-28'
__copyright__ = '(C) 2021 by Francesco Frassinelli/Norsk institutt for naturforskning'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MinimalisticMBTilesGenerator class from file MinimalisticMBTilesGenerator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .minimalistic_mbtiles_generator import MinimalisticMBTilesGeneratorPlugin
    return MinimalisticMBTilesGeneratorPlugin()
