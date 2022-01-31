// TODO: Adapt to Multi-Tenancy
func (c *MongoClient) NewMongoDb() *mongo.Client {
	client, err := mongo.Connect(c.Context, options.Client().ApplyURI(c.MongoURI).SetAuth(c.MongoCredentials))
	if err != nil {
		panic("unable to connect to MongoDB")
	}

	return client
}


