import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)
import multiprocessing    
from gensim.models import word2vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np


# periodical2vec
def train_p2v(journals, num_features, min_word_count, context, negative = 5):
    num_workers = multiprocessing.cpu_count()
    downsampling = 1e-3
    model = word2vec.Word2Vec(journals, workers=num_workers, vector_size=num_features,min_count = min_word_count, window = context, sample = downsampling, sg = 1, negative = negative)
    model_name = "j2v_%dd_%dc_%dm" %(num_features,  context, min_word_count)
    model.save(model_name)
    print("Finished!")

# retrain author2vec based on p2v
def train_a2v(common_texts, model, num_features, min_word_count, context):
    num_workers = multiprocessing.cpu_count()
    sentences = [TaggedDocument(doc, ['SENT_'+str(i)]) for i, doc in enumerate(common_texts)]
    doc2vecmodel = Doc2Vec(sentences, vector_size=num_features, window=context, min_count=min_word_count, workers=num_workers)
    print("Initial word vector")
    index2wordcollection = doc2vecmodel.wv.index_to_key 
    for i in range(len(doc2vecmodel.wv.vectors)):
        if index2wordcollection[i].startswith("SENT_"):
            continue
        wordindex = doc2vecmodel.wv.index_to_key[i]
        wordvectorfromlda = model.wv[wordindex]
        doc2vecmodel.wv.vectors[i] = wordvectorfromlda
    print("Changed word vector")
    doc2vecmodel.train_words = False 
    doc2vecmodel.learn_words = False
    doc2vecmodel.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)
    print("Trained doc vector again")
    return doc2vecmodel

