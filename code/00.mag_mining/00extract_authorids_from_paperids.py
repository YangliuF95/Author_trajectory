## get author id from the publication lists 
import pandas as pd
import gc
print('Starting...')
data=pd.read_csv('id_drop1.csv')#paper ids
print(data.shape)
n=12
while True:
    df = pd.read_csv('PaperAuthorAffiliations.txt', sep='\t', iterator=True, nrows=50000000, skiprows=n*50000000, chunksize=1000000,names=['PaperId','AuthorId','AffiliationId','AuthorSequenceNumber','OriginalAuthor','OriginalAffiliation'])
    chunk_list = []
    for chunk in df:  
        chunk_list.append(chunk)
    df_concat = pd.concat(chunk_list)
    if len(df_concat) <1:
        print('No more data')
        break 
    part=pd.merge(data,df_concat,on=['PaperId'])
    part.to_pickle('paper_author'+str(n)+'.pickle') # write to pickles
    n+=1
    print(str(n) +' Finished.')
    del df_concat
    gc.collect()