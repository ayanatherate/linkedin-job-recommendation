<h2> Intuition </h2>

<h3> Keeping track of the latest openings for a particular role and location might be gruesome. As also, manually reading long JD's to find out whether the skillset/experience required matches your expectations can also add more to the platter. Thus built a bot which automates this entire process, it returns  a csv containing the most matched jobs according to skills (Count Vectorizer + Cosine Similarity), sorted by the most recent date of job posting. </h3>
<h3> Sorted by: </h3>
<p1> Job Posting Date--> 1(latest)</p1><br>
<p1> Highest Potential Match with skills--->2 </p1>

<br>
<h2>Run locally on your machine:</h2>

```
git clone https://github.com/ayanatherate/findmyjobbot.git
cd findmyjobbot
pip install -r requirements.txt
python linkedinj.py
```
<br>



<h2> App Demo: </h2>

<img width="676" alt="image" src="https://user-images.githubusercontent.com/59755186/197277105-b078c6a2-974e-4c65-a9ee-23189d9bd367.png">
<br>
<img width="673" alt="image" src="https://user-images.githubusercontent.com/59755186/197323873-1fb1eac5-cabb-4c2e-b1cb-990839f0553b.png">


<br>
<h2>Csv returned:</h2>
<img width="757" alt="image" src="https://user-images.githubusercontent.com/59755186/197377696-b79c5355-d906-4a3c-8ad7-3f96c47616d4.png">


