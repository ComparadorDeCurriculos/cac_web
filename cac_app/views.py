from django.shortcuts import render, render_to_response, redirect
from .forms import CompForm


def compare(request):
	if request.method == "POST":
		form = CompForm(request.POST)

		if form.is_valid():
			return redirect('result', i1=form.cleaned_data['inst1'], c1=form.cleaned_data['curso1'], i2=form.cleaned_data['inst2'], c2=form.cleaned_data['curso2'])

	else:
		form = CompForm()

	return render(request, 'cac_app/compare.html', {'form': form})

def result(request, i1, c1, i2, c2):
	import csv
	import os.path

	csv2chart = []
	
	i1 = i1.upper()
	i2 = i2.upper()
	c1 = c1.upper()
	c2 = c2.upper()

	path = 'cac_app/static/comparison/credAulaNuc-'+i1+'_'+c1+'-'+i2+'_'+c2+'.csv'
	pathVenn = '/static/comparison/venn-'+i1+'_'+c1+'-'+i2+'_'+c2+'.png'
	if (not os.path.isfile(path)):
		path = 'cac_app/static/comparison/credAulaNuc-'+i2+'_'+c2+'-'+i1+'_'+c1+'.csv'
		pathVenn = '/static/comparison/venn-'+i2+'_'+c2+'-'+i1+'_'+c1+'.png'

	with open(path, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			csv2chart.append(row)
	
	labels = []
	
	for l in csv2chart[2]:
		s = l.split(' ')
		
		# make label for each core
		label = []
		if (len(s) == 3):
			label.append(s[0]+' '+s[1])
			label.append(s[2])
		elif (len(s) == 4):
			label.append(s[0]+' '+s[1])
			label.append(s[2]+' '+s[3])
		else:
			label.append(l)

		# inserting label
		labels.append(label)


	chartDic = {
		"credAulaNuc": {
			"title"			: csv2chart[0][0],
			"university1"	: csv2chart[1][0], 
			"course1"		: csv2chart[1][1],
			"university2"	: csv2chart[1][2], 
			"course2"		: csv2chart[1][3],
			'l1'			: str(labels[0]),
			'l2'			: str(labels[1]),
			'l3'			: str(labels[2]),
			'l4'			: str(labels[3]),
			'l5'			: str(labels[4]),
			'l6'			: str(labels[5]),
			"data1"			: str(list(map(int, csv2chart[3]))),
			"data2"			: str(list(map(int, csv2chart[4]))),
	  }
	}

	return render(request, 'cac_app/result.html', {'credAulaNuc': chartDic["credAulaNuc"], 'pathVenn' : pathVenn})