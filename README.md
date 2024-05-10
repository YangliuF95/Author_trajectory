# Author_trajectory

## Repository structure
This is the repository for the article "Understanding the scholars' trajectories across scientific periodicals" and contains the following elements:
  
- code: the code we used to wrangle, analyze, and visualize data.
- data: the publication trajectories for relevant authors from the Microsoft Academic Graph (MAG) dataset.

Note that the original record mined from the MAG dataset is too large to be uploaded to our Github repository. However, we have made available the code we used to extract the author trajectory from the MAG dataset.

## Method description

- Construction of author trajectory matrix based on periodical embeddings

![image](https://github.com/YangliuF95/Author_trajectory/assets/60612969/671e26c5-01d3-4eb2-8b07-cec1f8ff83eb)<p style='text-align: justify;'> 
***<sub>Starting from the author publication record—for example, Author 1 published four papers in four periodicals (i.e., P1, P2, P3, and P4), and Author 2 published six papers in the same four periodicals—step 1 generates ordered sequences of periodicals. In step 2, we train the periodical embeddings using the word2vec skip-gram implementation (i.e., to predict the context for a given periodical, as shown in the upper box). In step 3, we construct a trajectory matrix for each author based on the trained embeddings for each periodical. The rows represent the periodicals, and the columns represent the dimension of the embedding. The different colors in the matrix indicate different values.*** </p>

- Periodical embeddings and author trajectories
  
![image](https://github.com/YangliuF95/Author_trajectory/assets/60612969/35a226c7-85ff-4f63-b7f2-01a6c18eb4c6)




**(a)** The two-dimensional (2D) projection of 11909 periodicals using the Pairwise Controlled Manifold Approximation Projection (PaCMAP). 
- An interactive data visualization of [the embedding space](https://yangliu1231.github.io/periodical_embeddings) 🗺️📚

**(b)** <p style='text-align: justify;'>A group of (inter-)disciplinary periodicals. For example, *the International Journal of Urban Sciences*, classified as "Social Sciences", and *IEEE Transactions on Intelligent Transportation Systems*, classified as "Engineering and Technology", are close together and located at the intersection of "Social Sciences", "Engineering and Technology", and "Natural Sciences".   

**(c-d)** <p style='text-align: justify;'> Examples of author trajectory in the 2-d space. Here the blue arrow represents an author from "Engineering and Technology", and the orange arrow represents another author from "Medical and Health Sciences". The lightness of the color indicates the publication sequence. We can see that these two authors with comparable publication counts tend to have different movements in the periodical space. 


## Reference

More information about our method can be found in the following article:

 Yangliu Fan, Anders Blok, Sune Lehmann; Understanding scholar-trajectories across scientific periodicals. *Sci Rep* **14**, 5309 (2024). doi: [https://doi.org/10.1038/s41598-024-54693-7](https://www.nature.com/articles/s41598-024-54693-7)
  
If you use any of the provided material for your work, please cite us as follows:
```
@article{Author_Trajectory_2024,
  author={Fan, Y., Blok, A. & Lehmann, S.},
  doi={10.1038/s41598-024-54693-7}
  journal={Scientific Reports},
  title={Understanding scholar-trajectories across scientific periodicals},
  year={2024}
}
```


## License
![image](https://user-images.githubusercontent.com/60612969/135886472-567c603e-8001-43e3-a808-f020ba14814d.png)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). 

## Contact information
If you have any questions or suggestions, do not hesitate to [contact us](mailto:yangliufan@sodas.ku.dk) 😊
