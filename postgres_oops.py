import psycopg2


class PostGresInfo:

	def __init__(self, config):
		self.host = config['host']
		self.database = config['database']
		self.user = config['user']
		self.password = config['password']
		
	def connect(self):
		self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
		self.cur = self.conn.cursor()
				

	def fetchUserID(self, email):
		user_query="SELECT user_entity_id FROM tscutdb.v2_users WHERE email='"+email+"'"
		self.connect()
		self.cur.execute(user_query)
		usersData = self.cur.fetchall()
		print(usersData)
		return usersData[0][0]


	def fetchSubAccID(self, email):
		subAcc_query = "SELECT subscription_id,tsc_account_id FROM tscutdb.v2_subscriptions WHERE created_for='"+userId+"'"
		self.connect()
		self.cur.execute(subAcc_query)
		subscriptionData = self.cur.fetchall()
		return subscriptionData[0]


	def close(self):
		self.cur.close()
		self.conn.close()


config=dict(host="10.245.1.2",database="tscutdb", user="postgres", password="postgres")

pg = PostGresInfo(config)
email = "tscdevuser+abhi1@gmail.com "

print(pg.fetchUserID(email))
print(pg.fetchSubAccID(email))

pg.close()



