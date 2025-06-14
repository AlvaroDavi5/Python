import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%matplotlib inline # para excutar dentro do Jupyter Notebook
sns.set_theme(style="whitegrid")

def read_csv_data(path: str):
	df: pd.DataFrame = pd.read_csv(path)
	# print("\n Header: \n")
	# print(df.head())
	return df

def plot_score_by_study_hours(df: pd.DataFrame):
	dataframe = df.sort_values(by=['study_hours_per_day', 'exam_score'], ascending=[True, True])

	plt.figure(figsize=(80, 40))
	plt.plot(
		dataframe['study_hours_per_day'],
		dataframe['exam_score'],
		marker='.', linestyle='-', color='blue', label='Nota x Estudo')
	plt.title('Relação entre Tempo de Estudo e Notas')
	plt.xlabel('Tempo de Estudo (horas por dia)')
	plt.ylabel('Nota')
	plt.grid(True)
	plt.xticks(sorted(set(dataframe['study_hours_per_day'])))
	plt.tick_params(axis='x', labelrotation=45)
	plt.legend()
	plt.show()

def plot_score_by_attendance_percentage(df: pd.DataFrame):
	plt.figure(figsize=(50, 40))
	plt.scatter(
		df['attendance_percentage'],
		df['exam_score'],
		color='red')
	plt.title('Relação entre Participação nas Aulas e Notas')
	plt.xlabel('Participação (%)')
	plt.ylabel('Nota')
	plt.grid(True)
	plt.show()

def plot_score_by_social_media_and_watch_time(df: pd.DataFrame):
	plt.figure(figsize=(50, 40))
	plt.scatter(
		df['social_media_hours'],
		df['exam_score'],
		color='#0b67e0', label='Redes Sociais', s=100)
	plt.scatter(
		df['netflix_hours'],
		df['exam_score'],
		color='#e00b0b', label='Filmes/Séries', s=100)
	plt.title('Nota x Tempo Gasto em Redes Sociais e Filmes/Séries')
	plt.xlabel('Horas em Redes/Filmes/Séries')
	plt.ylabel('Nota no Exame')
	plt.grid(True)
	plt.legend()
	plt.show()

def plot_study_hours_by_free_time(df: pd.DataFrame):
	plt.figure(figsize=(30, 20))
	sns.scatterplot(
			data=df,
			x='study_hours_per_day',
			y='sleep_hours',
			hue='part_time_job',
			palette='Set2'
	)
	plt.title('Tempo de Estudo x Tempo de Sono e Emprego de Meio Período')
	plt.xlabel('Horas de Estudo por Dia')
	plt.ylabel('Horas de Sono por Dia')
	plt.legend(title='Emprego Meio Período')
	plt.tight_layout()
	plt.show()

def plot_study_hours_by_internet_quality(df: pd.DataFrame):
	plt.figure(figsize=(10, 10))
	sns.boxplot(
			data=df,
			y='study_hours_per_day',
			hue='internet_quality',
			palette='Pastel1'
	)
	plt.title('Horas de Estudo por Qualidade da Internet')
	plt.xlabel('Qualidade da Internet')
	plt.ylabel('Horas de Estudo por Dia')
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()

def plot_age_by_total_leisure_hours(df: pd.DataFrame):
	dataframe = df

	dataframe['leisure_hours'] = dataframe['social_media_hours'] + dataframe['netflix_hours']
	plt.figure(figsize=(20, 10))
	sns.scatterplot(
			data=dataframe,
			x='age',
			y='leisure_hours',
			color='teal', alpha=0.6
	)
	plt.title('Idade x Tempo em Redes Sociais e Filmes/Séries')
	plt.xlabel('Idade')
	plt.ylabel('Horas de Lazer (Redes + Filmes/Séries)')
	plt.grid(True)
	plt.tight_layout()
	plt.show()

def main():
	dataframe = read_csv_data("../database/student_habits_performance.csv")

	plot_score_by_study_hours(dataframe)
	plot_score_by_attendance_percentage(dataframe)
	plot_score_by_social_media_and_watch_time(dataframe)
	plot_study_hours_by_free_time(dataframe)
	plot_study_hours_by_internet_quality(dataframe)
	plot_age_by_total_leisure_hours(dataframe)

if __name__ == "__main__":
	main()

