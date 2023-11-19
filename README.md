<h2> Edit 2023: As of 2023, this tool still works, however it is in major need of Code restructure, cleaning and maintenance. Also, we are no longer College students, we don't write Spagghetish code like this anymore lol</h2>


<h2> Intuition </h2>

<h4> Keeping track of the latest openings for a particular role and location might be gruesome. As also, manually reading long JD's to find out whether the skillset/experience required matches your expectations can also add more to the platter. Thus built a bot which automates this entire process, it returns  a csv containing the most matched jobs (along with job apply link) according to skills (Count Vectorizer + Cosine Similarity), sorted by the most recent date of job posting. </h3>
<h3> Sorted by: </h4>
<p1> Job Posting Date--> 1(latest)</p1><br>
<p1> Highest Potential Match with skills--->2 </p1>

<br>
<h2>Run locally on your machine:</h2>

```
git clone https://github.com/ayanatherate/linkedin-job-recommendation.git
cd findmyjobbot
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main.py
```
<br>



<h2> Demo: </h2>

<img width="676" alt="image" src="https://user-images.githubusercontent.com/59755186/197277105-b078c6a2-974e-4c65-a9ee-23189d9bd367.png">
<h3> Edit March 2023: File name changed to main.py from linkedinj.py </h3>
<br>
<img width="673" alt="image" src="https://user-images.githubusercontent.com/59755186/197323873-1fb1eac5-cabb-4c2e-b1cb-990839f0553b.png">


<br>
<h2>Csv returned:</h2>
<img width="758" alt="image" src="https://user-images.githubusercontent.com/59755186/197381899-f15cda41-5ee5-410d-a006-3ff624b96871.png">



