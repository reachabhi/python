import psycopg2

conn = psycopg2.connect(host="10.245.1.2",database="tscutdb", user="postgres", password="postgres")
cur = conn.cursor()

def fetchSubAccID():
	#-------Fetch User Data-------
	cur.execute('SELECT * FROM tscutdb.v2_users')
	usersData = cur.fetchall()
	userId = [usersData[i][0] for i in range(len(usersData))]

	#-------Fetch Subscription Data-------
	cur.execute('SELECT * FROM tscutdb.v2_subscriptions')
	subscriptionData = cur.fetchall()
	sub_acc_Id = [(subscriptionData[x][0],subscriptionData[x][2]) for x in range(len(subscriptionData))]
	print(f"SubID and AccID fetched per UserID: \n{dict(zip(userId,sub_acc_Id))}")


def fetchSubAccIDByEmail(email):
	#-------Fetch User Data-------
	user_query="SELECT user_entity_id FROM tscutdb.v2_users WHERE email='"+email+"'"
	cur.execute(user_query)
	usersData = cur.fetchall()
	userId = usersData[0][0]
	print(f"UserId fetched for {email} is {userId}")

	#-------Fetch Subscription Data-------
	subAcc_query = "select subscription_id,tsc_account_id from tscutdb.v2_subscriptions where created_for='"+userId+"'"
	cur.execute(subAcc_query)
	subscriptionData = cur.fetchall()
	sub_acc_Id = subscriptionData[0]
	print(f"Sub and Acc ID fetched for {email} is {sub_acc_Id}")
	d={}
	d[userId]=sub_acc_Id
	print(f"SubID and AccID fetched for {email} is: {d}")
	return d


fetchSubAccID()
fetchSubAccIDByEmail("tscdevuser+abhi1@gmail.com")











