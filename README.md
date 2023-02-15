# Coding Challenge epilot Cologne

### Task

Crawl historic Bitcoin exchange value in USD and visualize in a heatmap similar to the GitHub contribution graph.

### Strategy

1. Find an API to download data
2. Write a python app that downloads the data from the API as files
3. Extract, transform and load the data from the files into a database. Reason: In a dashboard app with interactive clicks (choosing a date), you want to avoid the required computation and the number of system calls, i.e. you don't want to read the json file every time, decode the data into python-memory and start computing. Ideally, you can cache all that in a database, maybe sqlite.
4. Use Seaborn to visualize the data as a heatmap
5. Present the result either in a Jupyter Notebook or in a Streamlit app

### How to run the app

#### Get The Data

You need to get a key from [coinapi.com](https://docs.coinapi.io/) and export the key as the env variable "COINAPI_API_KEY". The python app gets the value with `os.environ.get`.

Once you have done that, execute `python src/crypto_api_client/crypto_api_client.py`

The script requires the `requests` package as dependency, so make sure you have it available in your Python.


### Journal

#### Wed 15. February 2023, 00:30

Interesting task, I think coding a solid solution will take more than half a day though. Sadly, I have quite a full schedule, and I could only start very late working on this challenge today (it's 00:30 now).

Finding an api that provides the data was pretty straightforward. I have found [`coinapi`](https://docs.coinapi.io/). You create a key and can call the API for free for 100 times within 24 hours. Nice.

I have written an app that requests the api and saves the output as json files in the directory `data`.

A little challenge in such a task is usually the pagination. I have saved all the data from 1.01.2010 to today, and an api will usually cap the max number of data per request. In the case of coinapi, you will get maximum 100 rows per request. Luckily, this was fairly easy to handle.

These is a compressed view of the logs of the app:

```
1: Getting data from 2022-11-07 to 2023-02-15
2: Getting data from 2022-07-30 to 2022-11-07
...
47: Getting data from 2010-04-04 to 2010-07-13
```

It's late now, so I will stop working on this now, but I am looking forward to continue on it tomorrow. The 

#### Wed 15. February 2023, 23:20

Today I finished step 3. The data is in a sqlite database and retrieval works like a charm. Final part is the visualisation. I will take care of that tomorrow.

