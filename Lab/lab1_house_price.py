from ibm_watson_machine_learning import APIClient

wml_credentials = {
                   "url": "https://us-south.ml.cloud.ibm.com",
                   "apikey":"FtC1ZWNjyQqVwds70moYyKF-plLmyrYlL1H0PHqwAg5h",
                  }

client = APIClient(wml_credentials)
client.set.default_space("8986719f-c1c0-48ac-8d9c-cdcbb52ac6ef") 
deployment_id = "11b295ab-15a4-44ed-ae31-7c539456ecac"

# set the input data scheme and input values
array_of_values_to_be_scored = [2012.917, 32, 84.87882, 10, 24.98298, 121.54024]
another_array_of_values_to_be_scored = [2012.917, 19.5, 306.5947, 9, 24.98034, 121.53951]

scoring_payload = {client.deployments.ScoringMetaNames.INPUT_DATA: [{"fields": ["X1 transaction date", "X2 house age", "X3 distance to the nearest MRT station", "X4 number of convenience stores", "X5 latitude", "X6 longitude"], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

# make prediction
predictions = client.deployments.score(deployment_id, scoring_payload)
print(predictions)
