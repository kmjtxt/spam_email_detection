## Location of Raw Datasets
Raw datasets are located in this Google Drive due to the large-sized files: https://drive.google.com/drive/folders/11juebPd9DGK0v2lUr5O6eddafeY73Ryk?usp=sharing

## Location of Processed Datasets
Processed dataset is located in this Google Drive due to its size: https://drive.google.com/drive/folders/1gexy0lphv7drQL4hYstczXB9ze7Ef8ei?usp=sharing

Note: full_df was trained with POS tagging previously. The features may appear in some notebooks when initially loaded, but are not used for any form of analysis or modelling.

## Description of dataset sources
The datasets we used were from public sources - Kaggle and Zenodo.

### Enron Corpus 

This dataset was released by the Federal Energy Regulatory Commission during the investigation of the Enron Corporation and were collected directly from Enron’s internal mail servers (Klimt & Yang, 2004). 

### Ling Spam Dataset 

The Ling-Spam corpus was created by Mark A. Giagrandi and Ion Androutsopoulos (2000) by collecting messages from a moderated mailing list (Linguist List) focused on linguistic topics then concatenating them with spam emails from public spam archives and known spam traps. 

### Spam Assassin Corpus 

The SpamAssassin Public Corpus was developed by the Apache SpamAssassin project. Non-spam messages were obtained from public mailing lists and personal inboxes with permission, while spam messages were gathered from online spam traps and user donations (SpamAssassin, 2006).  

### TREC, CEAS, Nazario – General Spam Corpus 

TREC and CEAS were compiled as part of research competitions (NIST and CEAS) which aggregate spam emails via honeypots and public spam reporting systems, while non-spam emails were obtained from publicly accessible mailing lists or corporate datasets. The Nazario corpus, assembled by Joseph Nazario (2008), harvested spam emails submitted to security research groups and spam traps. 


## Extra information on the datasets

These datasets include a collection of labelled emails, where each entry minimally contains the email body and a binary label indicating spam (1) or non-spam (0).  

To ensure data consistency, we excluded additional features like timestamps which are found only in some datasets. Hence, we only retain and examine label and body columns. 

To ensure data integrity, we performed random manual checks to verify the labels based on our understanding of spam. While these data are valuable for our project, we acknowledge potential biases. As observed from the table above, the spam to non-spam ratio varies across datasets – ranging from almost 1:1 to 1: 3. This can be attributed to the following factors: 


### Source bias due to different sources used 

There is a possible over-representation of specific types of spam or non-spam content such as corporate materials. Consequently, the models trained on these data may perform poorly on other types of messages underrepresented in the training set.  

 
### Temporal bias from older emails 

Some emails are from decades ago. With spam patterns constantly evolving, including the recent surge of AI-generated spam content (Ferrara, 2019), our models may not effectively account for these changes. 

 

While we acknowledge these limitations, we determine that our datasets remain effective in supplementing our spam classification models, provided we account for these caveats during preprocessing and model evaluation. 
