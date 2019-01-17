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
		elif self.tracking_beginning and self.is_tracking:
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

	def parseSubStepLevelsToStepLaTeXTable(self,step):
		eqcode = self.getStepEquipment(step)
		eqlevel = self.getEquipmentCleanLevel(eqcode)
		stpdscr = self.getStepDescription(step)

		if self.recent_level not in eqlevel.split('/'):
			self.recent_level = eqlevel

		ret = self.subStepLevelsToLaTeX(self.getRequiredPreSteps(eqcode))
		ret += "\\addLevelCell{"+self.recent_level+"} %"+stpdscr+"\n" # LaTeX cell generation macro
		ret += self.subStepLevelsToLaTeX(self.getRequiredPostSteps(eqcode))

		if self.tracking_beginning:
			self.tracking_beginning = False

		return ret


	def parseSubStepToStepLaTeXTable(self,step):
		eqcode = self.getStepEquipment(step)
		eqloc = self.getEquipmentLocation(eqcode)
		eqdscr = self.getEquipmentDescription(eqcode)
		eqlevel = self.getEquipmentCleanLevel(eqcode)
		stpdscr = self.getStepDescription(step)
		stpreq = self.getStepRequire(step)

		ret = self.parseSubStepsToLaTeX(self.getRequiredPreSteps(eqcode))
		ret += "\\addProcessStep{"+eqdscr+" ("+eqcode+")}{"+eqloc+"}{"+eqlevel+"}{"+stpdscr+"}{"+stpreq+"}\n" # LaTeX cell generation macro
		ret += self.parseSubStepsToLaTeX(self.getRequiredPostSteps(eqcode))

		if self.beginning:
			self.beginning = False

		return ret

	def extractSubSteps(self,substep):
		ret=[]
		if isinstance(substep, dict):
			ret.append(substep)
		else:
			if substep in self.repetitive_steps:
				steps=self.repetitive_steps[substep]
				if isinstance(steps, dict):
					ret.append(steps)
				elif isinstance(steps, list):
					for step in steps:
						ret+=self.extractSubSteps(step)
				else:
					print(steps)
		return ret

	def parseSubStepsToLaTeX(self,step_substeps):
		ret=""
		for substep in step_substeps:
			for stps in self.extractSubSteps(substep):
				ret+=self.parseSubStepToStepLaTeXTable(stps)

		return ret

	def subStepLevelsToLaTeX(self,step_substeps):
		ret=""
		for substep in step_substeps:
			for stps in self.extractSubSteps(substep):
				ret+=self.parseSubStepLevelsToStepLaTeXTable(stps)
		return ret

	def parseStepToLaTeX(self,step):
		try:
			step_name = step["name"]
			step_picture = step["cross_tikz"]
			step_substeps = step["steps"]
			step_mask = step["mask"]
		except:
			return "" # no valid step definition

		ret="\\makeProcessTable{"
		ret+=step_name
		ret+="}{"
		ret+=step_picture
		ret+="}{"
		ret+=step_mask
		ret+="}{"
		self.is_tracking = True
		ret+=self.subStepLevelsToLaTeX(step_substeps)
		self.is_tracking = False
		ret+="}{" #clean_table_content
		ret+=self.parseSubStepsToLaTeX(step_substeps)
		ret+="}\n"

		return ret

	def parseProcessYamlToLaTeX(self,tables):
		latex=""
		for step in self.steps: 
			latex+=self.parseStepToLaTeX(step)
		tables.write(latex)

	def __init__(
		self,
		steps_file,
		repetitive_steps_file,
		cleanliness_levels_file,
		equipment_file):

		self.beginning = True
		self.tracking_beginning = True
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


def generate_latex(filename):
	obj = auto_generator(
		filename,
		"repetitive_steps.yaml",
		"cleanliness_levels.yaml",
		"equipment.yaml"
	)
	tables = open(filename.replace(".yaml","")+".tex","w")
	obj.parseProcessYamlToLaTeX(tables)
	tables.close()

if '-f' in sys.argv:
	if len(sys.argv) >= sys.argv.index('-f')+2:
		filename=sys.argv[sys.argv.index('-f')+1]
		if "check" in sys.argv:
			print "Checking for errors"
		print "Generating LaTeX tables for "+filename
		generate_latex(filename)
	else:
		print "No file name given (-f)"
else:
	print "No filename given (-f)"
