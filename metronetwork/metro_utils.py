import os


INSTALLED_PATH = os.path.dirname(os.path.realpath(__file__))

line_color = {}
line_color['01호선'] = "#0052A4"
line_color['02호선'] = "#00A84D"
line_color['03호선'] = "#EF7C1C"
line_color['04호선'] = "#00A4E3"
line_color['05호선'] = "#996CAC"
line_color['06호선'] = "#CD7C2F"
line_color['07호선'] = "#747F00"
line_color['08호선'] = "#E6186C"
line_color['09호선'] = "#BDB092"
line_color['공항철도'] = "#0090D2"
line_color['경의선'] = "#77C4A3"
line_color['경춘선'] = "#005666"
line_color['수인분당선'] = "#FABE00"
line_color['신분당선'] = "#D31145"
line_color['경강선'] = "#0054A6"
line_color['서해선'] = "#8FC31F"
line_color['인천선'] = "#759CCE"
line_color['인천2호선'] = "#F5A251"
line_color['용인경전철'] = "#56AD2D"
line_color['의정부경전철'] = "#FD8100"
line_color['우이신설경전철'] = "#B7C450"
line_color['김포도시철도'] = "#AD8605"
line_color['신림선'] = "#6789CA"
line_color['응암순환선'] = "#CD7C2F"

def join(path, *paths):
	return os.path.join(path, paths)

def data_path(filename):
	return os.path.join(INSTALLED_PATH, 'data', filename)

def get_color(line):
	return line_color.get(line)