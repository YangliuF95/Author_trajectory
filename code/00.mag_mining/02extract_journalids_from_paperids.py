## find all journalids from paperids
import pandas as pd
import gc
import glob
print('Starting...')

# get all paperids
ls=glob.glob('author_paper*')
papers=pd.concat([pd.read_pickle(i) for i in ls]).reset_index(drop=True).drop_duplicates(subset=['PaperId']).dropna(subset=['PaperId'])
print(papers.shape)


# get the meta information for papers
n=0
while True:
    df = pd.read_csv('Papers.txt', sep='\t', iterator=True, nrows=20000000, skiprows=n*20000000, chunksize=1000000,low_memory=False, names=['PaperId','Rank','DOI','DocType','PaperTitle','OriginalTitle','BookTitle','Year','Date','Publisher','JournalId','ConferenceSeriesId','ConferenceInstanceId','Volume','Issue','FirstPage','LastPage','ReferenceCount','CitationCount','EstimatedCitation','OriginalVenue','FamilyId','CreatedDate'])
    chunk_list = []
    for chunk in df:  
        chunk_list.append(chunk)
    df_concat = pd.concat(chunk_list)
    if len(df_concat) <1:
        print('No more data')
        break 
    part=pd.merge(papers,df_concat,on=['PaperId'])
    part.to_pickle('author_journal'+str(n)+'.pickle') # write to pickles
    n+=1
    print(str(n) +' Finished.')
    del df_concat
    gc.collect()