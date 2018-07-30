#!/usr/bin/python3
import os
import sys
import xml.dom.minidom
dom = xml.dom.minidom.parse("ls1u.xml")
Topic=dom.getElementsByTagName('xml')

for node in Topic:
	alist=node.getElementsByTagName('layer')
	for a in alist:
		Title=a.firstChild.data
		print(Title)

