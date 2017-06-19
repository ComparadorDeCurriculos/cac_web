from django.shortcuts import render, render_to_response, redirect
from .forms import CompForm
from .src.plotting import *


def contactus(request):
	return render(request, 'cac_app/contactus.html');

def about(request):
	return render(request, 'cac_app/about.html');

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

	path1 = 'cac_app/cursos/' + i1 + '_' + c1 + '.txt'
	path2 = 'cac_app/cursos/' + i2 + '_' + c2 + '.txt'
	csv2bars = []

	with open('cac_app/static/data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			csv2bars.append(row)
	
	chartDic = {
		"2bars": {
			"labels": str(csv2bars[0]),
			"data1":  str(list(map(int, csv2bars[1]))),
			"data2":  str(list(map(int, csv2bars[2]))),
	  },
		"grafico2": {
			"labels": str(csv2bars[0]),
			"data1":  str(list(map(int, csv2bars[1]))),
			"data2":  str(list(map(int, csv2bars[2]))),
	  }
	}

	print("=======================")
	print(chartDic)
	print("=======================")

	#'cac_app/cursos/icmc/bcc/icmc/bsi_cac_app.txt'

	#plt.plotTwoBar(ufrgs, icmc_bcc);

	return render(request, 'cac_app/result.html', {'2bars': chartDic["2bars"]})