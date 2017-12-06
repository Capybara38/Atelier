
import os

decoup = "gdalwarp -of GTiff -ot Int16 -t_srs EPSG:2154 -r cubic -dstnodata 0 -tap -cutline 'Limites-PNR-Vercors.shp' -tr 250.0 250.0 -crop_to_cutline {} decoup/{}"
convert = "gdal_translate -of AAIGrid -ot Int16 {} {}"


dirlist = os.listdir('./')
listFile = os.system("touch liste.txt")

for directory in dirlist:
	os.system("cd {}/pheno.format(directory)")
	os.system("cp ../../../limte.shp ./")
	filelist = os.system("./*.tif")
	for modisFile in filelist:
		os.system(decoup.format(modisfile))
		ascFileName = modisFile.split('.')[0] + '.asc'
		os.system(convert.format(modisFile, ascFileName))
		filePath = os.path.abspath(os.path.dirname (_file_)) ## UNSURE 
		liste = open(filePath, "a")
		liste.write(ascFileName)

		# Une ligne de commentaire




