#!/usr/bin/python
import sys
import yaml

class auto_generator:
	beginning = True
	recent_level = "clean"

	def getStepEquipment(self,step):
		try:
			return step['equipment']
		except:
			return "Unknown"

	def getEquipmentDescription(self,code):
		try:
			eq = self.equipment[code]
		except:
			return code
		try:
			return eq["equipment"]
		except:
			return code

	def getStepDescription(self,step):
		try:
			return step['process']
		except:
			return "Unknown"

	def getStepRequire(self,step):
		try:
			return step['requirement']
		except:
			return ""

	def getEquipmentLocation(self,code):
		try:
			eq = self.equipment[code]
		except:
			return code
		try:
			return eq["location"]
		except:
			return code 

	def getEquipmentCleanLevel(self,code):
		try:
			eq = self.equipment[code]
		except:
			return code
		try:
			return eq["level"]
		except:
			return code 

	def getRequiredPreSteps(self,eqcode):
		return ""

	def parseSubStepToStepLaTeXTable(self,step):
		presteps = ""
		eqcode = self.getStepEquipment(step)
		eqloc = self.getEquipmentLocation(eqcode)
		eqdscr = self.getEquipmentDescription(eqcode)
		eqlevel = self.getEquipmentCleanLevel(eqcode)
		stpdscr = self.getStepDescription(step)
		stpreq = self.getStepRequire(step)
		ret = "\\addProcessStep{"+eqdscr+"}{"+eqloc+"}{"+eqlevel+"}{"+stpdscr+"}{"+stpreq+"}\n"
		ret += "\\hline"
		ret += "\n"

		if self.beginning:
			self.beginning = False
		else:
			presteps = self.getRequiredPreSteps(eqcode)

		ret = presteps+ret 
		return ret

	def parseStepToLaTeX(self,step):
		try:
			step_name = step["name"]
			step_picture = step["cross_tikz"]
			step_substeps = step["steps"]
		except:
			return
		self.tables.write("\\newpage\n\\section{"+step_name+"}\n")
		clean_table_content="\n"
		step_table_content="\n"
		for substep in step_substeps:
			clean_table_content+="\\getWaferCleaninessSymbol{"+self.recent_level+"}  \\\\[0.5cm]\\hline\n"
			step_table_content+=self.parseSubStepToStepLaTeXTable(substep)
		self.tables.write("\\makeProcessTable{"+step_picture+"}{"+clean_table_content+"}{"+step_table_content+"}\n")

	def parseProcessYamlToLaTeX(self,tables):
		self.tables = tables
		for step in self.steps: 
			self.parseStepToLaTeX(step)

	def __init__(
		self,
		steps_file,
		repetitive_steps_file,
		cleanliness_levels_file,
		equipment_file):

		with open(cleanliness_levels_file, 'r') as stream:
			self.cleanliness_levels = yaml.load(stream)
		with open(equipment_file, 'r') as stream:
			self.equipment = yaml.load(stream)
		with open(repetitive_steps_file, 'r') as stream:
			self.repetitive_steps = yaml.load(stream)
		with open(steps_file, 'r') as stream:
			self.steps = yaml.load(stream)

		try:
			self.recent_level = self.cleanliness_levels["start"] 
		except:
			print "Error occured"


def generate_latex():
	obj = auto_generator(
		"steps.yaml",
		"repetitive_steps.yaml",
		"cleanliness_levels.yaml",
		"equipment.yaml"
	)
	tables = open("tables_autogen.tex","w")
	obj.parseProcessYamlToLaTeX(tables)
	tables.close()

if len(sys.argv)>1:
	if sys.argv[1]=="check":
		print "Checking for errors"
	else:
		print "Generating LaTeX tables"
		generate_latex()
else:
	print "Generating LaTeX tables"
	generate_latex()
	
