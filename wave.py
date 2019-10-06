import os
import tkinter

def get_all_data():
	"""
	从文件中读取所有的数据
	return: 所有读出的数据
	"""
	frames = int(os.path.getsize("C:/Users/hasee/Desktop/holter.dat") / 16)
	fd = open("C:/Users/hasee/Desktop/holter.dat", "rb")
	a = []
	for i in range(8 * frames):
		a.append(int.from_bytes(fd.read(2), byteorder='big'))
	fd.close()
	return a

def get_line(data, num):
	"""
	获取第num条线的纵坐标数据
	data:   包含所有帧的列表
    num:    第几条线，取值[0, 8)
	return: 第num条线的纵坐标数据
	"""
	b = []
	for i in range(int(len(data) / 8)):
		b.append(data[i * 8 + num] + num * 800)	# 不同的线需要平移
	return b

def zoom_y_coor(data, ratio):
	"""
	缩放data的纵坐标
	data:   一条线的纵坐标列表
	ratio:  缩放系数
	return: 缩放后的纵坐标列表
	"""
	for i in range(len(data)):
		data[i] = data[i] * ratio
	return data

def add_x_coor(data, step):
	"""
	添加横坐标到data
	data:   一条线的纵坐标列表
	step:   横坐标的间隔
	return: 包含一条线横纵坐标的列表
	"""
	a = []
	for i in range(len(data)):
		a.append([i * step, data[i]])
	return a


all_data = get_all_data()

root = tkinter.Tk()
cv = tkinter.Canvas(root)
cv.pack(fill=tkinter.BOTH, expand=tkinter.YES)
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 0), 0.1), 10))
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 1), 0.1), 10))
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 2), 0.1), 10))
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 3), 0.1), 10))
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 4), 0.1), 10))
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 5), 0.1), 10))
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 6), 0.1), 10))
cv.create_line(add_x_coor(zoom_y_coor(get_line(all_data, 7), 0.1), 10))
root.mainloop()
