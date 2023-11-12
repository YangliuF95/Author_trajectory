## find all journalids get more paperids
import pandas as pd
import gc
import glob
print('Starting...')

# get all paperids
ls=glob.glob('author_journal*')
journals=pd.concat([pd.read_pickle(i) for i in ls]).drop_duplicates(subset=['JournalId'])[['JournalId']].dropna(subset=['JournalId'])
print(journals.shape)
conferences=pd.concat([pd.read_pickle(i) for i in ls]).reset_index(drop=True).drop_duplicates(subset=['ConferenceSeriesId'])[['ConferenceSeriesId']].dropna(subset=['ConferenceSeriesId'])
print(conferences.shape)
# get the full publication lists from journals 
n=2
while True:
    df = pd.read_csv('Papers.txt', sep='\t', iterator=True, nrows=20000000, skiprows=n*20000000, chunksize=20000000, low_memory=False,names=['PaperId','Rank','DOI','DocType','PaperTitle','OriginalTitle','BookTitle','Year','Date','Publisher','JournalId','ConferenceSeriesId','ConferenceInstanceId','Volume','Issue','FirstPage','LastPage','ReferenceCount','CitationCount','EstimatedCitation','OriginalVenue','FamilyId','CreatedDate'])
    chunk_list = []
    for chunk in df:  
        chunk_list.append(chunk)
    df_concat = pd.concat(chunk_list)
    if len(df_concat) <1:
        print('No more data')
        break 
    part=pd.merge(journals,df_concat,on=['JournalId'])
    try:
        part_1= pd.merge(conferences,df_concat,on=['ConferenceSeriesId'])
        parts=pd.concat([part,part_1]).reset_index(drop=True)
        parts.to_pickle('fullpaper'+str(n)+'.pickle') # write to pickles
    except:
        part.to_pickle('fullpaper'+str(n)+'.pickle') # write to pickles
    n+=1
    print(str(n) +' Finished.')
    del df_concat
    gc.collect()