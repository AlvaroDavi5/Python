import pandas as pd # pandas library imported with alias 'pd'

def main():
	dataframe = pd.read_csv("./Chicago_Public_Schools.csv")
	print("\n Header: \n")
	print(dataframe.head()) # printed header of file data with pandas library
	print("\n Names: \n")
	print(dataframe["Name of School"]) # printed all dataframe "Name of School" column
	print("\n Level: \n")
	print(dataframe["Elementary, Middle, or High School"]) # printed all dataframe "Elementary, Middle, or High School" column
	print()

# executar o programa		
if __name__ == "__main__":
	main()
