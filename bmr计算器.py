def main():
	y_or_n = input('是否退出程序（y/n）？')


	while y_or_n != 'y':
		# 姓名
		#name = (input("请输入姓名："))
		# 性别
		# gender = input("请输入性别：")

		# 年龄
		# age = int(input("请输入年龄："))

		# 身高
		# height = float(input("请输入身高（cm）："))

		# 体重
		# weight = float(input("请输入体重（kg）："))
		print('请输入以下信息，用空格分割')
		input_str = input('性别 体重（kg） 身高（cm） 年龄：')
		str_list = input_str.split(' ')  #字符串分割，用 空格 分割
		try:
			gender = str_list[0]
			weight = float(str_list[1])
			height = float(str_list[2])
			age = int(str_list[3])

			if gender == '男':
				# 男性：
				bmr = (13.7 * weight)+(5.0 * height)-(6.8 * age)+66

			elif gender == '女':
				# 女性
				bmr = (9.6 * weight)+(1.8 * height)-(4.7 * age)+65
			else:
				bmr = -1

			if bmr != -1:
				print('性别：{},体重：{}公斤,身高：{}cm，年龄：{}岁'.format(gender,weight,height,age))
				print('基础代谢率：{}大卡'.format(bmr))  # str.format 字符串格式化输出，使用{}占位

			else:
				print('暂不支持该性别')
		except ValueError:
			print('请输入正确的信息！')
		except IndexError:
			print('请输入完整的信息！')
		except:
			print('程序异常！')


		print() # 输出空行
		y_or_n = input('是否退出程序（y/n）?')
	else:
		print('退出程序')

if __name__ == '__main__':
		main()




