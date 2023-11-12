## find all journalids get more paperids
import pandas as pd
import gc
import glob
print('Starting...')

# get all paperids
ls=glob.glob('fullpaper*')
papers=pd.concat([pd.read_pickle(i) for i in ls]).drop_duplicates(subset=['PaperId'])[['PaperId']]
print(papers.shape)

# get the full publication lists from journals 
n=0
while True:
    df = pd.read_csv('PaperReferences.txt', sep='\t', iterator=True, nrows=50000000, skiprows=n*50000000, chunksize=1000000,names=['PaperId','reference'])
    chunk_list = []
    for chunk in df:  
        chunk_list.append(chunk)
    df_concat = pd.concat(chunk_list)
    if len(df_concat) <1:
        print('No more data')
        break 
    part=pd.merge(papers,df_concat,on=['PaperId']) #merge from citing 
    df_concat.columns=['citing','PaperId']
    part_1= pd.merge(papers,df_concat,on=['PaperId']) #merge from reference
    part_1.columns=['PaperId','reference']
    parts=pd.concat([part,part_1]).reset_index(drop=True) #concat the two
    parts.to_pickle('fullcitation'+str(n)+'.pickle') # write to pickles
    n+=1
    print(str(n) +' Finished.')
    del df_concat
    gc.collect()