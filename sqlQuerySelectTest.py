def sqlExecutor(sql):
	databaseConnection = sqlite3.connect(databaseFile)
	localCursor = databaseConnection.cursor()
	localCursor.execute(*sql)
	fetchedData = localCursor.fetchall()
	databaseConnection.commit()
	databaseConnection.close()
	return(fetchedData)
####
def loginFunction(userdata):
	sqlCode = ["SELECT user_ID FROM zooAppDB_userdata WHERE user_name == ? AND user_password == ?", userdata]
	fetchedData = sqlExecutor(sqlCode)
	try:return(fetchedData[0][0])
	except:return(False)
####
while True:
	username = input("username: ")
	password = input("password: ")
	print(loginFunction((username, password)))
