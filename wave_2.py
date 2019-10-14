import os
import matplotlib.pyplot as plt

# file = 'E:/code_pool/Wave-Display/datas/CIM_ECG_DATAS.dat'
file = './datas/CIM_ECG_DATAS.dat'

def get_s16(val):
    if val < 0x8000:
        return val
    else:
        return (val - 0x10000)

def get_all_data(filepath, ofs, frames):
	"""
	从文件中读取所有的数据
	ofs:	偏移多少帧
	frames:	读取多少帧
	return: 所有读出的数据
	"""
	total_frames = int(os.path.getsize(filepath) / 16)

	if ofs + frames > total_frames:
		return 0

	fd = open(filepath, "rb")
	fd.seek(ofs * 8)

	a = []
	for i in range(frames * 8):
		a.append(get_s16(int.from_bytes(fd.read(2), byteorder='big')))
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
		b.append(data[i * 8 + num])
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

all_data = get_all_data(file, 10000, 250 * 5)
if all_data == 0:
	print('error')
	quit()

ydata = get_line(all_data, 0)
ydata = zoom_y_coor(ydata, 1)
xydata = add_x_coor(ydata, 0.004)

plt.plot(xydata)
plt.show()
