
import datetime
import os

def run():
	line_dict = {'index': 0, 'line': [], 'time_in': 0, 'time_end': 0}
	lines_stripped = []
	with open("F:\Users\Admin\Downloads\hoshi_subs_om.srt", 'r') as f:
		lines = f.readlines()
		for line in lines:
			lines_stripped.append(line.rstrip())
		for line in lines_stripped:
			if len(line) <= 4 and line.isdigit() == True:
				line_ind = int(line)
				add_index(line_ind)
			if len(line) > 1:
				if ":" in line:
					#it's a number
					add_num(line, line_ind)
				if ":" not in line:
					#it's a script line
					add_line(line, line_ind)
	return

def add_index(line):
	l
	return
def add_num(line, index):
	#print "it's a number!"
	return

def add_line(line, index):
	#print "it's a line!"
	return 
run()