#!/usr/bin/python
import sys
import yaml

class auto_generator:
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

	def getRepetitiveJob(self,task_id):
		try:
			return self.repetitive_steps[task_id]
		except:
			return []

	def getRequiredPreSteps(self,eqcode):
		try:
			eq = self.equipment[eqcode]
		except:
			return ""
		try:
			step_id = eq["pre"]
		except:
			return []

		if self.beginning:
			step_id="initial_"+step_id

		return self.getRepetitiveJob(step_id)

	def getRequiredPostSteps(self,eqcode):
		try:
			eq = self.equipment[eqcode]
		except:
			return ""
		try:
			step_id = eq["post"]
		except:
			return []

		return self.getRepetitiveJob(step_id)

	def getRequiredPreStepsLaTeX(self,eqcode):
		ret = ""
		pre_steps = self.getRequiredPreSteps(eqcode)
		print pre_steps
		for step in pre_steps:
			eqcode = self.getStepEquipment(step)
			eqloc = self.getEquipmentLocation(eqcode)
			eqdscr = self.getEquipmentDescription(eqcode)
			eqlevel = self.getEquipmentCleanLevel(eqcode)
			stpdscr = self.getStepDescription(step)
			stpreq = self.getStepRequire(step)
			ret+="\\addProcessStep{"+eqdscr+"}{"+eqloc+"}{"+eqlevel+"}{"+stpdscr+"}{"+stpreq+"}\n"
			ret+="\\hline"
			ret+="\n"
		return ret

	def getRequiredPostStepsLaTeX(self,eqcode):
		ret = ""
		for step in self.getRequiredPostSteps(eqcode):
			eqcode = self.getStepEquipment(step)
			eqloc = self.getEquipmentLocation(eqcode)
			eqdscr = self.getEquipmentDescription(eqcode)
			eqlevel = self.getEquipmentCleanLevel(eqcode)
			stpdscr = self.getStepDescription(step)
			stpreq = self.getStepRequire(step)
			ret+="\\addProcessStep{"+eqdscr+"}{"+eqloc+"}{"+eqlevel+"}{"+stpdscr+"}{"+stpreq+"}\n"
			ret+="\\hline"
			ret+="\n"
		return ret

	def parseSubStepToStepLaTeXTable(self,step):
		presteps = ""
		eqcode = self.getStepEquipment(step)
		eqloc = self.getEquipmentLocation(eqcode)
		eqdscr = self.getEquipmentDescription(eqcode)
		eqlevel = self.getEquipmentCleanLevel(eqcode)
		stpdscr = self.getStepDescription(step)
		stpreq = self.getStepRequire(step)
		ret = "\\addProcessStep{"+eqdscr+"}{"+eqloc+"}{"+eqlevel+"}{"+stpdscr+"}{"+stpreq+"}\n"

		presteps = self.getRequiredPreStepsLaTeX(eqcode)
		poststeps = self.getRequiredPostStepsLaTeX(eqcode)

		if self.beginning:
			self.beginning = False

		ret = presteps+ret+poststeps
		ret += "\\hline"
		ret += "\n"
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

		self.beginning = True
		self.recent_level = "clean"

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
	
