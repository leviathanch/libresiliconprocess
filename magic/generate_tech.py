#!/usr/bin/python3
import os
import sys
import xml.dom.minidom

class TechGen():
	dom=None
	outfile=None

	def main(self):
		print("This is XML to Tech converter")

	def run(self):
		print("Running XML to Tech converter")
		try:
			self.dom=xml.dom.minidom.parse("ls1u.xml")
		except Exception as e:
			print(e)

		if(self.dom!=None):
			self.outfile=open("ls1u.tech","w+")
			if(self.outfile!=None):
				self.write_tech_header()
				self.write_planes()
				self.write_types()
				self.outfile.write("contact\n")
				self.outfile.write("end\n\n")
				self.write_styles()
				self.outfile.write("compose\n")
				self.outfile.write("end\n\n")
				self.outfile.write("connect\n")
				self.outfile.write("end\n\n")
				self.outfile.write("cifoutput\n")
				self.outfile.write("\tstyle generic\n")
				self.outfile.write("\tscalefactor 1\n")
				self.outfile.write("end\n\n")
				self.outfile.write("cifinput\n")
				self.outfile.write("\tstyle generic\n")
				self.outfile.write("\tscalefactor 1\n")
				self.outfile.write("end\n\n")
				self.outfile.write("drc\n")
				self.outfile.write("end\n\n")
				self.write_extract()
				self.outfile.write("plot\n")
				self.outfile.write("end\n\n")
				self.write_aliases()

	def write_tech_header(self):
		self.outfile.write("tech\n")
		self.outfile.write("\tformat 33\n")
		self.outfile.write("\tls1u\n")
		self.outfile.write("end\n\n")
		self.outfile.write("version\n")
		self.outfile.write("\tversion 8.2.8\n")
		self.outfile.write("\tdescription \"LibreSilicon CMOS Technology for 1um\"\n")
		self.outfile.write("end\n\n")

	def write_planes(self):
		planes=self.dom.getElementsByTagName('plane')
		self.outfile.write("planes\n")
		for n in planes:
			try:
				plane_name=n.getElementsByTagName('name')[0].firstChild.data
				try:
					plane_shortname=n.getElementsByTagName('shortname')[0].firstChild.data
					plane_name=plane_name+","+plane_shortname
				except:
					print("no shortname defined for "+plane_name)
				self.outfile.write("\t"+plane_name+"\n")
			except:
				print("no name defined")
		self.outfile.write("end\n\n")

	def write_types(self):
		layers=self.dom.getElementsByTagName('layer')
		self.outfile.write("types\n")
		for n in layers:
			try:
				layer_name=n.getElementsByTagName('name')[0].firstChild.data
				try:
					layer_type=n.getElementsByTagName('plane')[0].firstChild.data
					self.outfile.write("\t"+layer_type+" "+layer_name+"\n")
				except:
					print("no layer type defined for "+layer_name)
			except:
				print("no name defined")
		self.outfile.write("end\n\n")

	def write_styles(self):
		layers=self.dom.getElementsByTagName('layer')
		self.outfile.write("styles\n")
		self.outfile.write("\tstyletype mos\n")
		for n in layers:
			try:
				layer_name=n.getElementsByTagName('name')[0].firstChild.data
				try:
					layer_color=n.getElementsByTagName('dstyle')[0].firstChild.data
					self.outfile.write("\t"+layer_name+" "+layer_color+"\n")
				except:
					print("no layer type defined for "+layer_name)
			except:
				print("no name defined")
		self.outfile.write("end\n\n")

	def write_extract(self):
		planes=self.dom.getElementsByTagName('plane')
		self.outfile.write("extract\n")
		self.outfile.write("\tstyle standard\n")
		self.outfile.write("\tcscale 1\n")
		self.outfile.write("\tlambda 9\n")
		self.outfile.write("\tstep   100\n")
		self.outfile.write("\tsidehalo 8\n")
		i=0
		for n in planes:
			try:
				plane_name=n.getElementsByTagName('name')[0].firstChild.data
				self.outfile.write("\tplaneorder "+plane_name+" "+str(i)+"\n")
				i=i+1
			except:
				print("no name defined")
		self.outfile.write("end\n\n")

	def write_aliases(self):
		layers=self.dom.getElementsByTagName('layer')
		self.outfile.write("aliases\n")
		for n in layers:
			try:
				layer_name=n.getElementsByTagName('name')[0].firstChild.data
				list_of_aliases=[]
				for alias in n.getElementsByTagName('alias'):
					list_of_aliases.append(alias.firstChild.data)
				if(len(list_of_aliases)>0):
					#self.outfile.write("\t"+layer_name+" "+(",".join(list_of_aliases))+"\n")
					for a in list_of_aliases:
						self.outfile.write("\t"+a+" "+layer_name+"\n")
			except:
				print("no name defined")
		self.outfile.write("end\n\n")

app = TechGen()
app.run()
