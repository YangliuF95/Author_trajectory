## find all publications from these authors in mag
import pandas as pd
import gc
import glob
print('Starting...')

# get author ids
ls=glob.glob('paper_author*')
authors=pd.concat([pd.read_pickle(i) for i in ls]).reset_index(drop=True).drop_duplicates(subset=['AuthorId']).dropna(subset=['AuthorId'])[['AuthorId']]
print(authors.shape)

# get their publications 
n=0
while True:
    df = pd.read_csv('PaperAuthorAffiliations.txt', sep='\t', iterator=True, nrows=50000000, skiprows=n*50000000, chunksize=1000000,names=['PaperId','AuthorId','AffiliationId','AuthorSequenceNumber','OriginalAuthor','OriginalAffiliation'])
    chunk_list = []
    for chunk in df:  
        chunk_list.append(chunk)
    df_concat = pd.concat(chunk_list)
    if len(df_concat) <1:
        print('No more data')
        break 
    part=pd.merge(authors,df_concat,on=['AuthorId'])
    part.to_pickle('author_paper'+str(n)+'.pickle') # write to pickles
    n+=1
    print(str(n) +' Finished.')
    del df_concat
    gc.collect()