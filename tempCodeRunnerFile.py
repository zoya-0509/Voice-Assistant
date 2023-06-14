elif 'play series' in query:
            series_path="C:\\Users\\KIIT\\Videos\\ITS OKAY TO NOT BE OKAY"
            eps=os.listdir(series_path)
            os.startfile(os.path.join(series_path,eps[0]))