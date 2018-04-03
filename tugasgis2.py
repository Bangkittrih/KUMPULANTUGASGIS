import mapnik
m = mapnik.Map(3840,2160)
m.background = mapnik.Color('steelblue')
# MAP 1 DUNIA
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#7FFF00')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Bangkit',s)
ds = mapnik.Shapefile(file="countries/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Bangkit')
m.layers.append(layer)
# BATAS AKHIR MAP 1 DUNIA

# MAP 2 Negara Afrika
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#D2691E')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('white'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Bangkit2',s)
ds = mapnik.Shapefile(file="mapafrika/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Bangkit2')
m.layers.append(layer)
# BATAS AKHIR MAP 2 Negara Afrika

# MAP 3 Negara Belanda
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#00FFFF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Turquoise'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Bangkit3',s)
ds = mapnik.Shapefile(file="mapbelanda/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Bangkit3')
m.layers.append(layer)
# BATAS AKHIR MAP 3 Negara Belanda

# MAP 4 Negara Egypt
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#00FFFF')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Aqua'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Bangkit4',s)
ds = mapnik.Shapefile(file="mapegypt/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Bangkit4')
m.layers.append(layer)
#BATAS AKHIR MAP 4 Negara Egypt

#MAP 5 Negara France
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#8A2BE2')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Violet'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Bangkit5',s)
ds = mapnik.Shapefile(file="mapfrance/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Bangkit5')
m.layers.append(layer)
#BATAS AKHIR MAP 5 Negara France

#MAP 6 Negara Turkey
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#FF7F50')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('Coral'),1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Bangkit6',s)
ds = mapnik.Shapefile(file="mapturkey/map.shp")
layer = mapnik.Layer('negara')
layer.datasource = ds
layer.styles.append('Bangkit6')
m.layers.append(layer)
#BATAS AKHIR MAP 6 Negara Turkey
 
m.zoom_all()
mapnik.render_to_file(m,'world.jpeg','jpeg')
print "rendered image to 'world.jpeg'"