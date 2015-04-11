# -*- coding: utf-8 -*-
import xlrd


def read_file_name():
	rd = open('file_name.txt', 'r')
	file_name = rd.readlines()
	return file_name


def process(str):
	f_1 = xlrd.open_workbook(str[0])
	data_1 = f_1.sheet_by_name(str[1])
	d1_nrows = data_1.nrows
	d1_ncols = data_1.ncols

	f_2 = xlrd.open_workbook(str[3])
	data_2 = f_2.sheet_by_name(str[4])
	d2_nrows = data_2.nrows
	d2_ncols = data_2.ncols

	for i in range(0, d1_nrows):
		key_1 = data_1.cell(i, str[2]).value.encode('utf-8')
		for j in range(0, d2_nrows):
			key_2 = data_2.cell(j, str[5]).value.encode('utf-8')
			if (cmp(key_1, key_2) == 0):
				print key_1, key_2
				print cmp(key_1, key_2)
			




file_name = read_file_name()
for i in range(0, len(file_name)):
	length = len(file_name[i])
	file_name[i] = file_name[i][0: length-1]

file_name[2] = int(file_name[2]) - 1
file_name[5] = int(file_name[5]) - 1

# print file_name
process(file_name)
