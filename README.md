# Introduction to Building Intelligent Apps

This repository introduces and helps organizations get started with building Intelligent Apps and incorporating Large Language Models (LLMs) into them.

## Workshop Agenda

### 🌅 Morning (9:00 – 12:15)

> *Focus: Introduction, First Steps & Prompt Engineering*

* 📣 Intro (30min)
  * Introductions & Setting Expectations
  * Use Case Ideation & Brainstorming
* 📣 [Intro to Azure OpenAI, Prompt Engineering & Demos (105min)](presentations/README.md)
  * Azure OpenAI Service
  * Demo(s)
  * Break
  * 🧑🏼‍💻 [Lab #1 - Hands-on with Prompt Engineering Exercises](labs/01-prompts/prompts.md)
* 📣 [Intro to AI Orchestration (60min)](presentations/README.md)
  * AI Orchestration
  * Demo(s)

### 🌆 Afternoon (1:15 – 4:30)

> *Focus: Building Intelligent Apps & Incorporating LLMs*

* 📣 [Intro to AI Orchestration Continued (135min)](presentations/README.md)
  * 💻 [Lab #2 - Hands-on with AI Orchestration Exercises](labs/02-orchestrators/README.md)
  * 💻 [Lab #3 - Hands-on with Tokens, Embeddings & Vectors Exercises](labs/03-tbd/README.md)
  * Break
* Wrapping-up (60min)
  * Use Case Validation
  * QnA & Closing Remarks

-------------------

## Preparation

> *This is only required for the hands-on lab. If you are only attending the presentation, you can skip this section.*

### Azure OpenAI Service subscription and deployments

Grant the participant access to the Azure OpenAI Service subscription and create the required deployments.

Ideally, grant the participants access to Azure OpenAI Service service be assigning the `Cognitive Service OpenAI user`. If the participant is a `Cognitive Service OpenAI contributor`, they can create the following deployments themselves.

Otherwise, create 'text-davinci-003' and 'text-embedding-ada-002' deployments (and assign the participant to the deployments).

There are two ways to authenticate (see Jupyter notebooks):

1. (Recommended) Use the Azure CLI to authenticate to Azure and Azure OpenAI Service
2. Using a token (not needed if using the Azure CLI)

Get the Azure OpenAI Service endpoint (and key) from the Azure portal.

### Workspace environment

Choose one of the following options to set up your environment: Codespaces, Devcontainer or bring your own environment (Anaconda). Building the environment can take a few minutes, so please start early.

#### 1️⃣ Codespaces

> 🌟 Highly recommended: *Best option if you already have a Github account. You can develop on local VSCode or in a browser window.*

* Go to Github repository and click on `Code` button
* Create and edit the `.env` file in the base folder including Azure OpenAI Service endpoint and key before starting any notebooks

#### 2️⃣ Devcontainer

> *Usually a good option if VSCode and Docker Desktop are already installed.*

* Install [Docker](https://www.docker.com/products/docker-desktop)
* Install [Visual Studio Code](https://code.visualstudio.com/)
* Install [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
* Clone this repository
* Open the repository in Visual Studio Code
* Click on the green button in the bottom left corner of the window
* Select `Reopen in Container`
* Wait for the container to be built and started
* Create and edit `.env` file in the base folder including Azure OpenAI Service endpoint and key before starting any notebooks
