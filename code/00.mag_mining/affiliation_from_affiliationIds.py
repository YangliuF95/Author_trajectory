import pandas as pd
import gc
import glob
print('Starting...')
author=pd.read_csv('author_back.csv')
author=author.dropna(subset=['LastKnownAffiliationId'])
author.columns=['AuthorId', 'OriginalAuthor_x', 'DOI', 'PaperId', 'Title',
       'NowAffiliationId', 'OriginalAffiliation', 'AuthorSequenceNumber', 'Rank',
       'NormalizedName', 'AffiliationId', 'PaperCount',
       'CitationCount', 'CreatedDate', 'AcademicAge', 'FirstId', 'Level',
       'score', 'CategoryName', 'Background', 'Age']
n=0
while True:
    df = pd.read_csv('Affiliations.txt', sep='\t', iterator=True, nrows=20000000, skiprows=n*20000000, chunksize=1000000,low_memory=False, names=['AffiliationId','Rank','NormalizedName','DisplayName','GridId','OfficialPage','Webpage','PaperCount','CitationCount', 'Latitude', 'Longitude', 'CreatedDate'])
    chunk_list = []
    for chunk in df:  
        chunk_list.append(chunk)
    df_concat = pd.concat(chunk_list)
    if len(df_concat) <1:
        print('No more data')
        break 
    df_concat.AffiliationId =  df_concat.AffiliationId.astype(float)
    part=pd.merge(author[['AuthorId','AffiliationId']],df_concat,on=['AffiliationId'])
    part.to_pickle('affilication_detail'+str(n)+'.pickle') # write to pickles
    n+=1
    print(str(n) +' Finished.')
    del df_concat
    gc.collect()
    