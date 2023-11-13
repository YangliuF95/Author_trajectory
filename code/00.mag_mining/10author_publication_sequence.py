import pandas as pd
import gc
import glob
print('Starting...')

# get all paperids
ls=glob.glob('author_journal*')
pubs=pd.concat([pd.read_pickle(i) for i in ls]).dropna(subset=['JournalId']).reset_index(drop=True)
pubs['VenueId']=pubs.JournalId
pubs['Type']='Journal'
pubs_1=pd.concat([pd.read_pickle(i) for i in ls]).dropna(subset=['ConferenceSeriesId']).reset_index(drop=True)
pubs_1['VenueId']=pubs_1.ConferenceSeriesId
pubs_1['Type']='Conference'
pub=pd.concat([pubs,pubs_1])
pub=pub[~pub.Year.isna() | ~pub.PaperId.isna() | ~pub.PaperTitle.isna() |~pub.AuthorId.isna() ].reset_index(drop=True)
print('num of publications:', pub.shape)
pub['Date'] = pd.to_datetime(pub['Date'])
pub=pub.sort_values(by=['Date'])

# merge with all authors 
pub_1=pub[['PaperId', 'AffiliationId',  'OriginalAffiliation', 'Rank', 'DOI', 'DocType',
       'PaperTitle', 'OriginalTitle', 'BookTitle', 'Year', 'Date', 'Publisher',
       'JournalId', 'ConferenceSeriesId', 'ConferenceInstanceId', 'Volume',
       'Issue', 'FirstPage', 'LastPage', 'ReferenceCount', 'CitationCount',
       'EstimatedCitation', 'OriginalVenue', 'FamilyId', 'CreatedDate',
       'VenueId', 'Type']]

ls=glob.glob('author_paper*')
papers=pd.concat([pd.read_pickle(i) for i in ls]).reset_index(drop=True)

print('num of publications with authors:', papers.shape)

pub_2=pub_1.merge(papers[['AuthorId','PaperId','AuthorSequenceNumber','OriginalAuthor']], on=['PaperId']).drop_duplicates()

# filter by #publications and year
pub_2.Year=pub_2.Year.astype(float)
pub_2=pub_2[pub_2.Year>1959]

#pub_2=pub_2[pub_2.groupby("AuthorId")['AuthorId'].transform('size') > 1].reset_index(drop=True)

pub_2.VenueId=pub_2.VenueId.astype(float)
pub_2.VenueId=pub_2.VenueId.astype(int)
#groupby authors
pub_2=pub_2.astype(str)
pub_2=pub_2.groupby(['AuthorId']).agg({"OriginalAuthor":'first','Year':'; '.join, 'PaperId':'; '.join, 'VenueId':'; '.join,'PaperTitle':'; '.join, 'OriginalVenue':'$;$ '.join, 'CitationCount':'; '.join}).reset_index()

pub_2.to_pickle('author_sequence.pickle')

print('Finished.')