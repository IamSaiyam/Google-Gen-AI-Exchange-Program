
# Develop GenAI Apps with Gemini and Streamlit: Google Cloud Challenge Lab Walkthrough

This is a walkthrough of the challenge lab from the course Develop GenAI Apps with Gemini and Streamlit. I’ll show you how to complete the lab, but also help explain concepts along the way.

In this lab, we will be creating a proof-of-concept AI-Based **Chef app**. It will test our ability to:

* Run **Jupyter notebooks** in **Google Vertex AI Workbench**.

* Use the **Gemini Pro **multimodal foundation model.

* Use **cURL to test our Gemini Pro API calls**.

* Use the **Streamlit **framework for our application UI.

* **Containerise **the application and push to the **Google Artifact Registry**.

* **Deploy **our application from Artifact Registry to **Cloud Run**.

It’s a pretty easy lab, and probably takes around 30–40 minutes… Even with the slow image build and deploy steps.

## Intro to Challenge Labs

Google provides an online learning platform called Google [Cloud Skills Boost](https://www.cloudskillsboost.google/), formerly known as QwikLabs. On this platform, you can follow training courses aligned to learning paths, to particular products, or for particular solutions.

One type of learning experience on this platform is called a **quest**. This is where you complete a number of guided hands-on labs, and then finally complete a **Challenge Lab**. The **challenge lab** differs from the other labs in that goals are specified, but very little guidance on *how* to achieve the goals is given.

I occasionally create walkthroughs of these challenge labs. The goal is not to help you cheat your way through the challenge labs! But rather:

* To show you what I believe to be an ideal route through the lab.

* To help you with particular gotchas or blockers that are preventing you from completing the lab on your own.

If you’re looking for help with this challenge lab, then you’ve come to the right place. But I strongly urge you to work your way through the quest first, and to try the lab on your own, before reading further!

With all these labs, there are always many ways to go about solving the problem. I generally like to solve them using the Cloud Shell, since I can then document a more repeatable and programmatic approach. But of course, you can use the Cloud Console too.

## Overview of Technologies in this Lab

### Generative AI

Generative AI refers to types of machine learning algorithms that are able to generate new content. The content is created by a foundation model; i.e. generative AI model that has been trained on a huge amount of existing data.

![Gen AI and Foundation Models](https://cdn-images-1.medium.com/max/2000/0*ZjmNyg3LQYgir5EF)*Gen AI and Foundation Models*

### Gemini Pro

[Gemini](https://deepmind.google/technologies/gemini/#introduction) is a family of generative AI models developed by Google DeepMind, and designed for **multimodal** use cases. Multimodal means: where we can take input in various forms — such as text, image and video — and then generate content in various forms.

![Multimodal Models](https://cdn-images-1.medium.com/max/3098/0*wHcjd47DOxhSYsl5)*Multimodal Models*

There are various Gemini models available, but the one we’ll use in this lab is Gemini Pro. Since v1.5, Gemini Pro provides the ground-breaking 2 million token context window. This is a huge context window, relative to its predecessors.

### Streamlit

Streamlit is an open-source Python framework designed for creating and sharing data-driven web applications quickly and easily. It is particularly popular among data scientists and machine learning engineers, for turning Python data applications into web-based interactive applications.

Typical Streamlit use cases include:

* Rapid prototyping

* Data exploration and visualisation

* ML model demos

* Dashboarding

* Interactive reports

* Education and tutorials

### Google Artifact Registry (GAR)

Google’s general-puspose artifact management service that can store and manage a wide range of software artifacts, such as container images and language packages. (It is the successor to the Google Container Registry.)

### Cloud Run

Google’s serverless container runtime environment, intended for hosting of stateless containers that respond to web requests or other events. We can easily deploy to Cloud Run using a container image stored in a registry, such as Google Artifact Registry. Cloud Run automatically scales, and can scale down to 0. You only pay for what you’re using.

## My Solution to the Lab

### Initial Setup

Let’s start by defining some variables we can use throughout this challenge. The actual variables will be provided to you when you start the lab.

    # authenticate
    gcloud auth list
    
    # Set environment variables
    export PROJECT=$DEVSHELL_PROJECT_ID
    export REGION=<ENTER ZONE>

### Task 1 — Use cURL to test a prompt with the API

* First, navigate to Vertex AI → Workbench → User-Managed Notebooks.

![Open User-Managed Notebooks in Vertex AI Workbench](https://cdn-images-1.medium.com/max/4136/1*kTTKVd56gFyTzaqgIIid8Q.png)*Open User-Managed Notebooks in Vertex AI Workbench*

* Click on Open Jupyterlab.

![Jupyter Lab](https://cdn-images-1.medium.com/max/3524/1*dkGv4dGY9BnVT8HfLxMbQA.png)*Jupyter Lab*

* Open a terminal from the Jupyter Lab environment, and then copy the provided Jupyter notebook from Google Cloud Storage, using the instruction provided. This notebook is where we’ll test our Gemini Pro API calls.

    gsutil cp gs://spls/gsp517/prompt.ipynb .

* The notebook will appear in the navigation menu on the left. Open this notebook.

![Opening the notebook](https://cdn-images-1.medium.com/max/3940/1*4XhNRd465V8CW48H2MSG2A.png)*Opening the notebook*

* Provide your project ID and region.

* Replace the prompt, using the lengthy prompt supplied in the lab.

* Now run all the cells. The last cell runs a cURL command to the Gemini Pro API, as a bash command. The output looks a bit like this:

![Running the notebook cells](https://cdn-images-1.medium.com/max/2886/1*AQfYOB0wYU-qH_3vUjF1jg.png)*Running the notebook cells*

* Save the modified prompt.ipynb.

### Task 2 — Complete chef.py

From Cloud Shell, clone the GitHub repo, and then download the chef.py from the supplied GCS bucket:

    # clone repo and change to this directory
    git clone https://github.com/GoogleCloudPlatform/generative-ai.git
    cd generative-ai/gemini/sample-apps/gemini-streamlit-cloudrun
    
    # Download chef.py from GCS
    gsutil cp gs://spls/gsp517/chef.py .

* Now we examine chef.py from the Cloud Shell Editor. It is a Python Streamlit application that uses Gemini to generate content.

![chef.py](https://cdn-images-1.medium.com/max/3710/1*z01wY6O2EJTmQTCzSOpbAA.png)*chef.py*

* We’re asked to add a radio button to select Red, White, or None for wine, and we’re asked to substitute the new prompt supplied in the lab:

![Modifying chef.py](https://cdn-images-1.medium.com/max/2348/1*hwf2k5wYT-AXyhtQSvhWzA.png)*Modifying chef.py*

* Now upload the modified chef.py back to GCS, from Cloud Shell. (Note that your directory will be different.) We’re only doing this, because it’s required to validate step completion in the challenge lab.

    gcloud storage cp chef.py gs://qwiklabs-gcp-01-d2f0e6cd7ad5-generative-ai/

### Task 3 — Test the Application

Now we’ll test the application.

First, let’s setup our Python virtual environment and install application dependencies. In case this is new to you: a Python virtual environment is a Python context where we can install Python packages in a manner that is isolated from any other Python runtime environment. In short: they isolate Python project dependencies.

Our current folder already contains a requirements.txt, so we can easily install our required Python packages into our newly created virtual environment.

    # Setup Python env
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

And now we run our Streamlit chef.py application locally:

    streamlit run chef.py \
      --browser.serverAddress=localhost \
      --server.enableCORS=false \
      --server.enableXsrfProtection=false \
      --server.port 8080

![](https://cdn-images-1.medium.com/max/2576/1*O80fivMorxVV7S-KS2GVNA.png)

We can test it in the browser:

![Running the Streamlit app locally](https://cdn-images-1.medium.com/max/2740/1*ewTLyeqwKQiatrnlKnKM-Q.png)*Running the Streamlit app locally*

Let’s try it out:

![](https://cdn-images-1.medium.com/max/2568/1*C1MWTwkfc6_ZPZLiAz2FMw.png)

Ooh, that’s sounds delicious. I might have to make that later!

We can now press Ctrl-C in Cloud Shell to terminate the application.

### Task 4 — Containerise and Push to Artifact Registry

First, we’re told to modify the existing Dockerfile to use our chef.py. This is trivial to do. Just edit the Dockerfile in the same folder, using Cloud Shell Editor:

![Update Dockerfile to use chef.py](https://cdn-images-1.medium.com/max/3628/1*QQA2GbdpUvbZRnlE8fuu7w.png)*Update Dockerfile to use chef.py*

Now we’re told to set new two environment variables. Do this from Cloud Shell. These environment variables will be used when we build our image and deploy to Cloud Run.

    export AR_REPO=chef-repo
    export SERVICE_NAME=chef-streamlit-app

Now create a repository in Google Cloud Artefact Registry, and then build our Docker image and push it to GAR:

    # Create a GAR repo
    gcloud artifacts repositories create "$AR_REPO" \
      --location="$REGION" --repository-format=Docker
    
    # Build to GAR - this takes a few minutes
    gcloud builds submit \
      --tag "$REGION-docker.pkg.dev/$PROJECT/$AR_REPO/$SERVICE_NAME"

So far, so good!

![Build result](https://cdn-images-1.medium.com/max/2900/1*JpL4U5iZpIQ-UxG0w5cgyQ.png)*Build result*

### Task 5 — Deploy to Cloud Run and Test

Finally, we’re ready to deploy to Cloud Run:

    # Deploy to Cloud Run - this takes a couple of minutes
    gcloud run deploy "$SERVICE_NAME" \
      --port=8080 \
      --image="$REGION-docker.pkg.dev/$PROJECT/$AR_REPO/$SERVICE_NAME" \
      --allow-unauthenticated \
      --region=$REGION \
      --platform=managed  \
      --project=$PROJECT \
      --set-env-vars=GCP_PROJECT=$PROJECT,GCP_REGION=$REGION

Note how we’re setting environment variables for our Cloud Run instance, passing in the environment variables we defined previously.

![gcloud run deploy](https://cdn-images-1.medium.com/max/3538/1*m38fgFbIG0baGzRI9pVBxg.png)*gcloud run deploy*

Let’s open the Cloud Run URL, and check the app works:

![Our Chef application running in Cloud Run](https://cdn-images-1.medium.com/max/3160/1*0t5FyQgNwMh9tEtrpdRS4g.png)*Our Chef application running in Cloud Run*

Now I fancy a Mexican dish… And I’ll avoid paprica, as it gives me migraines!

![Recipe created by Gemini Pro](https://cdn-images-1.medium.com/max/2684/1*ipQTmQ8vPtBh5k5QbOqxTw.png)*Recipe created by Gemini Pro*

## Wrap Up

Hurrah!! All done!

***Isn’t it amazing how easy it is to build a GenAI-based recipe application and deploy it to Cloud Run?***

![Mind… Blown!](https://cdn-images-1.medium.com/max/2000/0*XoCAEF_EX16aQrbr.gif)*Mind… Blown!*

## Useful Links

* [Streamlit.io](http://streamlit.io)

* [Develop GenAI Apps with Gemini and Streamlit](https://partner.cloudskillsboost.google/course_templates/978)

* [https://ai.google.dev/gemini-api](https://ai.google.dev/gemini-api)

* [Gemini Streamlit code samples on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/sample-apps/gemini-streamlit-cloudrun)

* [Sample Streamlit Chef application](https://github.com/derailed-dash/gcp-challenge-labs/tree/master/src/gemini/gemini-streamlit-cloudrun)

## Before You Go

* **Please share** this with anyone that you think will be interested. It might help them, and it really helps me!

* Please **give me claps**! You know you clap more than once, right?

* Feel free to **leave a comment** 💬.

* **Follow** and **subscribe, **so you don’t miss my content. Go to my [Profile Page](https://medium.com/@derailed.dash), and click on these icons:

![Follow and Subscribe](https://cdn-images-1.medium.com/max/2000/0*gQblq-Bl0KxWNFuA.png)*Follow and Subscribe*
