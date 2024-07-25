## Analyzing verbal reports with LLMs @ EGPROC 2024

The workshop introduces the use of open-source large language models (LLMs) to identify decisions reasons from verbal reports. 

By [Kamil Fulawka]([https://zak-hussain.github.io/](https://www.mpib-berlin.mpg.de/person/114650/2549)) and [Dirk Wulff](https://www.mpib-berlin.mpg.de/person/93374/2549)

### Schedule

#### Day 1
<font style="font-size:10">09:00 AM - 09:30 AM: Coffee & Registration<br>
09:30 AM - 11:00 AM: Intro to LLMs<br>
11:00 AM - 11:30 AM: Break<br>
11:30 AM - 12:30 PM: Intro to verbal reports in JDM research<br>
12:30 PM - 14:00 PM: Lunch<br>
14:00 PM - 15:30 PM: Identifying decisions in verbal reports incl. exercise<br>
15:30 PM - 16:00 PM: Coffee break<be>
16:00 PM - 17:30 PM: Exercise continued<br>


### Resources
<a href="https://osf.io/preprints/psyarxiv/f7stn">Hussain, Binz, Mata, & Wulff (2024) A tutorial on open-source large language models for behavioral science</a>
[Hugging face documentation](https://huggingface.co/docs)<br>
[Hugging face book](https://transformersbook.com/)<br>
[But what is a GPT (3Blue1Brown)](https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=5)<br>

### Installation Instructions
0. If you do not have a Google account, you will need to create one (this can be deleted after the workshop).
1. Navigate to Google Drive (https://drive.google.com/).
2. In the top-left, click New > More > Colaboratory. If you do not see Colaboratory, you may need to click "Connect more apps", 
search for 'Colaboratory', and install it. Then click New > More > Colaboratory.
3. Copy the following code snipped into the first cell of the notebook. Run it (```shift + enter``` or click &#9658; button) to mount your Google Drive to the Colab environment.
A pop-up will ask you to connect; click through the steps to connect your Google Drive to Colab (you will have to do this
every time you open a new notebook).
```
from google.colab import drive
drive.mount("/content/drive")
```
4. Create a second cell in your notebook using the "+ Code" button that appears when you hover your cursor right under the first cell. Copy and run the following code snippet in the second cell of your notebook to clone the GitHub repository to your Google Drive :
```
%cd /content/drive/MyDrive
!git clone https://github.com/Zak-Hussain/LLM4BeSci_GSERM2024.git
```
5. Go back to your Google Drive and navigate to the folder "LLM4SocBeSci". You should see the directories `day_1`, `day_2`,`day_3`, `day_4`, and `day_5` containing the relevant notebooks (.ipynb files) and data (it may take  a couple of minutes for the files to appear) for the exercises of each day.
6. Open the folder `exercise` and then the `exercise.ipynb` notebook. A new Colab window will open.
7. Run the first cell of the notebook to install the required packages. This may take a few minutes and ask for you to give permission to access your Google Drive. 

You are now ready to start the exercises!
