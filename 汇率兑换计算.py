"""

    # 美元与人民币货币兑换计算实现
    # 作者：owen
    # 汇率兑换程序

"""

# 汇率
USD_VS_RMB = 6.77

#带单位的货币输入
currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q):')
print(currency_str_value)
i = 0
while currency_str_value !='Q':
	# 获取货币单位,保留后三位
	unit = currency_str_value[-3:]
	""""
	if 
  	  	pass
	elif
    	pass
	"""
	if unit == 'CNY':
    	# 输入的是人民币，排除后三位，取其他所有数值
		rmb_str_value = currency_str_value[:-3]
    	# 将字符串转换为数字
		rmb_value = eval(rmb_str_value)
    	# 汇率计算
		usd_value = rmb_value / USD_VS_RMB

    	# 输出结果
		print('美元(USD)金额是：', usd_value)
	elif unit == 'USD':
    	# 输入的是美元
		usd_str_value = currency_str_value[:-3]
		# 将字符串转换为数字
		usd_value = eval(usd_str_value)
		# 汇率计算
		rmb_value = usd_value * USD_VS_RMB

		# 输出结果
		print('人民币(CNY)金额是：', rmb_value)

	else:
		# 其他情况
		print('目前版本尚不支持该种货币！')
	i = i + 1
	print('循环次数', i)
	print('***************************************************')
	currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q):')

print("程序已经退出")

