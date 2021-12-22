### Context
The majority of review datasets are in English. There are datasets in other languages, but not many. Through this work, I would like to enrich the datasets in the French language and slightly contribute to advancing data science and AI, not only for English NLP tasks but for other languages around the world.

French is an international language and it is gaining ground. In addition, it is the language of love. The richness of the French language, so appreciated around the world, is largely related to the richness of its culture. The most telling example is French literature, which has many world-famous writers, such as [Gustave Flaubert](https://en.wikipedia.org/wiki/Gustave_Flaubert), [Albert Camus](https://en.wikipedia.org/wiki/Albert_Camus), [Victor Hugo](https://en.wikipedia.org/wiki/Victor_Hugo),  [Molière](https://en.wikipedia.org/wiki/Moli%C3%A8re), etc.

The French book reviews is a dataset of a huge number of reader reviews on French books. The data was collected using web scraping (with Scrapy Framework) and subjected to further data processing. For more details, see this notebook, which details the dataset creation process. [Notebook of the Dataset creation](https://www.kaggle.com/abireltaief/scrapyproject-a-to-z-dataset-book-reviews)

The data was retrieved from two French websites: [Babelio](https://www.babelio.com/) and [Critiques Libres](http://www.critiqueslibres.com/)
Like Wikipedia, these two French sites are made possible by the contributions of volunteers who use the Internet to share their knowledge and reading experiences.&nbsp;
**Note**: This dataset will be constantly updated to include the most recent reviews on French books by aggregating the old datasets with the updated ones in order to have a huge dataset over time.

### Content
In this repository, I give a detailed explanation of how to build spiders (one basic spider and one web crawler) to scrape the data you need.
I use the Scrapy Framework.
