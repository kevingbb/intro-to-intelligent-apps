# Orchestrators

In this document you will find exercises for building large language models (LLMs) into applications. For each orchestrator you will see how to setup a sample project and turn a prompt into a callable API endpoint. Your task will be to call the API endpoint using curl or Postman to achieve the expected result.

-------------------

## Orchestrator - Semantic Kernel

### Getting Started

Let's get started by creating an out of the box Semantic Kernel project based on Azure Functions template. This will provide a base structure for you to build upon and learn a few steps at a time.

1. Open repo in Codespaces, VS Code devcontainer or setup your own environment.
2. Use SK Extension to create a new default C# or Python Azure Functions based Project
3. Before starting the Function App, take a look at the following:
    * "skills" folder
    * "config" folder
4. Find the "Excuses" folder under the "skills/FunSkill" directory. What do you see?
5. Before we can successfully start the Functions App, we need to provide it some configuration. Go to the "config" folder and create the appropriate setup/configuration that points to the Azure OpenAI Service created. Use the README.ms and the example files in the "config" folder for clues.
6. Start the Function App and take note of the URL, you will need this later

<details>
  <summary>:white_check_mark: Sample URL</summary>

  http://localhost:7071/api/skills/{skillName}/functions/{functionName}
  
</details>

7. Invoke the "Excuses" function under the "FunSkill" skill using curl or postman. Check out the following [sample payload](payload-excuses.json) if you need a hint.

### Add Custom Semantic Skill

Now that you have seen it in action, let's add a custom semantic skill. Use one of the prompts from the earlier exercise or feel free to use your own. The prompt should have at least one variable, {{$input}}, to help demonstrate how to make a prompt dynamic versus just being static.

1. Add a new skill directory along with function directory in the "skills" folder.
2. Add "config.json" and "skprompt.txt" files to the function directory, be sure to use your own **prompt** and configuration.
3. Restart your function so the new skill will be loaded.
4. Invoke the "YOUR_NEWLY_CREATED_FUNCTION" function under the "YOUR_NEW_SKILL" skill using curl or postman.

Assuming all the above executes correctly, you have now turned your OpenAI prompt into a rest-based API that can be leveraged across the Enterprise. Yay!

-------------------

## Orchestrator - LangChain

1. Steps go here.
