#!/usr/bin/python3
import os
import sys
import xml.dom.minidom
dom=xml.dom.minidom.parse("ls1u.xml")
layers=dom.getElementsByTagName('layer')
planes=dom.getElementsByTagName('plane')
outfile=open("ls1u.tech","w+")

outfile.write("tech\n")
outfile.write("\tformat 33\n")
outfile.write("\tls1u\n")
outfile.write("end\n\n")

outfile.write("version\n")
outfile.write("\tversion 8.2.8\n")
outfile.write("\tdescription \"LibreSilicon CMOS Technology for 1um\"\n")
outfile.write("end\n\n")

outfile.write("planes\n")
for n in planes:
	try:
		plane_name=n.getElementsByTagName('name')[0].firstChild.data
		try:
			plane_shortname=n.getElementsByTagName('shortname')[0].firstChild.data
			plane_name=plane_name+","+plane_shortname
		except:
			print("no shortname defined for "+plane_name)
		outfile.write("\t"+plane_name+"\n")
	except:
		print("no name defined")
outfile.write("end\n\n")

outfile.write("types\n")
for n in layers:
	try:
		layer_name=n.getElementsByTagName('name')[0].firstChild.data
		try:
			layer_type=n.getElementsByTagName('plane')[0].firstChild.data
			outfile.write("\t"+layer_type+" "+layer_name+"\n")
		except:
			print("no layer type defined for "+layer_name)
	except:
		print("no name defined")
outfile.write("end\n\n")

outfile.write("contact\n")
outfile.write("end\n\n")

outfile.write("styles\n")
outfile.write("\tstyletype mos\n")
for n in layers:
	layer_gds2=n.getElementsByTagName('gds2')[0].firstChild.data
	layer_name=n.getElementsByTagName('name')[0].firstChild.data
	#outfile.write("\t"+layer_name+" "+layer_gds2+"\n")
outfile.write("end\n\n")

outfile.write("compose\n")
outfile.write("end\n\n")

outfile.write("connect\n")
outfile.write("end\n\n")

outfile.write("cifoutput\n")
outfile.write("\tstyle generic\n")
outfile.write("\tscalefactor 1\n")
outfile.write("end\n\n")

outfile.write("cifinput\n")
outfile.write("\tstyle generic\n")
outfile.write("\tscalefactor 1\n")
outfile.write("end\n\n")

outfile.write("drc\n")
outfile.write("end\n\n")

outfile.write("extract\n")
outfile.write("\tstyle standard\n")
outfile.write("\tcscale 1\n")
outfile.write("\tlambda 9\n")
outfile.write("\tstep   100\n")
outfile.write("\tsidehalo 8\n")
i=0
for n in planes:
	try:
		plane_name=n.getElementsByTagName('name')[0].firstChild.data
		outfile.write("\tplaneorder "+plane_name+" "+str(i)+"\n")
		i=i+1
	except:
		print("no name defined")
outfile.write("end\n\n")

outfile.write("plot\n")
outfile.write("end\n\n")

outfile.write("aliases\n")
outfile.write("end\n\n")

for n in layers:
	layer_color=n.getElementsByTagName('color')[0]
	layer_color_type=n.getElementsByTagName('type')[0].firstChild.data
	layer_color_code=n.getElementsByTagName('code')[0].firstChild.data
