import pandas as pd # pandas library imported with alias 'pd'

def main():
	dataframe = pd.read_csv("./Chicago_Public_Schools.csv")
	print("\n Header: \n")
	print(dataframe.head()) # printed all dataframe head

	print("\n Name: \n")
	pdserie_names = dataframe["Name of School"] # dataframe column is a series
	print(pdserie_names)

	# localizate and replace dataframe contents
	dataframe.loc[(dataframe["Elementary, Middle, or High School"] == 'ES'), "Elementary, Middle, or High School"] = 'Elementary'
	dataframe.loc[(dataframe["Elementary, Middle, or High School"] == 'HS'), "Elementary, Middle, or High School"] = 'High'
	dataframe.loc[(dataframe["Elementary, Middle, or High School"] == 'MS'), "Elementary, Middle, or High School"] = 'Middle'
	print("\n Level: \n")
	print(dataframe["Elementary, Middle, or High School"])

	print("\n About First School: \n")
	print(dataframe.iloc[0]) # list of dataframe
	print("\n First School Index: \n")
	print(dataframe.iloc[[0]]) # dataframe row is a series


# executar o programa		
if __name__ == "__main__":
	main()

