#how to use kwargs
def report_status(**kwargs):

    print('\nBEGIN: REPORT\n')

    for key, value in kwargs.items():
        print(key + ": " + value)
    
    print("\nEND REPORT")

report_status(name='luke', affiliation='jedi', status='missing')

#sequential re-index 
def re_index(seriesObject):
	seriesObject.index = np.arange(0, len(combined))
	return seriesObject


seriesObject([0.469112, -0.282863, -1.509059])