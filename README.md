# Text Analyzer
Flask project for text analytics. 
* Counting words, characters and sentences from text. 
* Detecting top 5 words and ignoring stop-words

### Running with Docker
1. ```git clone https://github.com/pochlib/test_task_analyzer```
2. Build docker image ```docker build -t test_task_analyzer.```
3. Run docker container ```docker run -p 5000:5000 test_task_analyzer```

Project should be accessible at http://127.0.0.1:5000.

## Answers
### What would you improve if you had more time?
I would add cases such parentheses, smiles, etc. and make frontend more visually appealing.
### What problems could arise when processing a 1,000,000-character text? How would you address them?
I have tested this case and somehow it works. But if let's say it starts to break with 10 billion characters I would first find a place where it breaks 
and depending on a problem I would break it into chunks, process them in parallel, merge results into dict and then search for top 5.
![Screenshot 2026-03-03 at 15.52.04.png](Screenshot%202026-03-03%20at%2015.52.04.png)
### How would you scale this application to handle 1,000 concurrent users?
I would use Google Cloud Run because you can set up autoscaling there when a lot if simultaneous requests are coming. 

> `I confirm that I completed this task independently.`